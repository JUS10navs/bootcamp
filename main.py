import flet as ft

def main(page: ft.Page):
    page.title = "Flet Counter Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def update_value(change):
        txt_number.value = str(int(txt_number.value) + change)
        page.update()

    btn_minus_2 = ft.ElevatedButton("-2", on_click=lambda e: update_value(-2))
    btn_minus_1 = ft.ElevatedButton("-1", on_click=lambda e: update_value(-1))
    btn_plus_1 = ft.ElevatedButton("+1", on_click=lambda e: update_value(1))
    btn_plus_2 = ft.ElevatedButton("+2", on_click=lambda e: update_value(2))

    page.add(
        ft.Row(
            [
                btn_minus_2,
                btn_minus_1,
                txt_number,
                btn_plus_1,
                btn_plus_2,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
