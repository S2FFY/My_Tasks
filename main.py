import flet as ft

def main(page: ft.Page):
    page.title = "My Tasks"
    page.theme_mode = "dark"

    navigation = ft.Column(
        controls=[
            ft.IconButton(ft.Icons.HOME),
            ft.IconButton(ft.Icons.SETTINGS)
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=0
    )

    sidebar = ft.Container(
        content=navigation,
        width=50,
        padding=0,
        bgcolor='#000000',
        alignment=ft.alignment.top_left,

    )
    page.padding = 0

    main_area = ft.Container(
        content=ft.Text('Здесь область работы'),
        padding=20
    )

    page.add(ft.Row([sidebar, main_area], expand=True))

ft.app(target=main)
