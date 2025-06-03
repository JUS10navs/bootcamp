from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        else:
            return "Invalid credentials"

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        image_file = request.files['image']
        name = request.form['name']
        birthday = request.form['birthday']
        address = request.form['address']
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(username=username).first():
            error = "Username already taken. Please choose another one."
            return render_template('register.html', error=error)

        filename = secure_filename(image_file.filename)
        image_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
        image_file.save(image_path)

        new_user = User(
            image=filename,
            name=name,
            birthday=birthday,
            address=address,
            username=username,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    # Calculate age
    try:
        birthdate = datetime.strptime(user.birthday, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    except Exception:
        age = "Unknown"

    return render_template('profile.html', user=user, age=age)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
