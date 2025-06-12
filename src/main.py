import flet as ft

def main(page: ft.Page):
    page.title = "Justine Navarro"

    profile_section = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Image(src="icon.png", fit=ft.ImageFit.COVER),
                    width=60,
                    height=60,
                    border_radius=30,
                    clip_behavior=ft.ClipBehavior.HARD_EDGE
                ),
                ft.Text("Justine H. Navarro", size=20, weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.only(top=20)
    )

    content = ft.Column(controls=[profile_section], expand=True)

    nav_bar = ft.Container(
        content=ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.CHAT, label="Chat"),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
            ],
            selected_index=0,
            bgcolor="transparent", 
            indicator_color=ft.Colors.BLUE,
        ),
        border=ft.Border(top=ft.BorderSide(1, ft.Colors.GREY)),
        height=70, 
    )

    page.add(
        ft.Column(
            controls=[content, nav_bar],
            expand=True
        )
    )

ft.app(target=main)
