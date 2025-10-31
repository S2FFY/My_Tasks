from operator import index
import flet as ft

def main(page: ft.Page):
    page.title = "My Tasks"
    page.theme_mode = ft.ThemeMode.DARK

    def switch_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            sidebar.bgcolor = '#ffffff'
            #sidebar_setings.bgcolor = '#ffffff'
        else:
            page.theme_mode = ft.ThemeMode.DARK
            sidebar.bgcolor = '#000000'
            #sidebar_setings.bgcolor = '#000000'
        page.update()

    def navigate(e):
        print(index(e))

    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Column(  # верхнее меню
                    controls=[
                        ft.IconButton(ft.Icons.TASK_ALT, on_click=lambda e: navigate(0)),
                        ft.IconButton(ft.Icons.LOOP, on_click=lambda e: navigate(1)),
                        ft.IconButton(ft.Icons.GRID_VIEW, on_click=lambda e: navigate(2)),
                        ft.IconButton(ft.Icons.TIMER, on_click=lambda e: navigate(3)),
                        ft.IconButton(ft.Icons.SUNNY, on_click=switch_theme),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=0,
                    expand=True
                ),
                ft.IconButton(ft.Icons.SETTINGS, on_click=lambda e: navigate(99)),  # снизу
            ],
            expand=True,
        ),
        width=40,
        bgcolor="#000000",
    )

    main_area = ft.Container(
        expand=True

    )
    page.padding=0
    page.add(ft.Row([sidebar, main_area], expand=True))

ft.app(target=main)
