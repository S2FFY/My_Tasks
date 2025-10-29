import flet as ft

def main(page: ft.Page):
    page.title = "My Tasks"
    page.theme_mode = ft.ThemeMode.DARK

    def switch_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            sidebar.bgcolor = '#ffffff'
        else:
            page.theme_mode = ft.ThemeMode.DARK
            sidebar.bgcolor = '#000000'
        page.update()

    nav = ft.Column(
        controls=[
            ft.IconButton(ft.Icons.TASK_ALT),
            ft.IconButton(ft.Icons.LOOP),
            ft.IconButton(ft.Icons.GRID_VIEW),
            ft.IconButton(ft.Icons.TIMER),
            ft.IconButton(ft.Icons.SUNNY, on_click=switch_theme),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=0
    )

    sidebar = ft.Container(
        content=nav,
        width=40,
        padding=0,
        bgcolor='#000000',
        alignment=ft.alignment.top_left
    )

    main_area = ft.Container(
        content=ft.Text('Kjk'),
        padding=20,
        expand=True
    )
    page.padding=0
    page.add(ft.Row([sidebar, main_area], expand=True))

ft.app(target=main)
