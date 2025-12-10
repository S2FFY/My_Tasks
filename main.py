from operator import index
import flet as ft

def main(page: ft.Page):
    page.title = "My Tasks"
    page.theme_mode = ft.ThemeMode.DARK


    #кнопки менюшки
    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.IconButton(ft.Icons.HEXAGON_OUTLINED, icon_size=35, icon_color='#ffffff'),
                        ft.IconButton(ft.Icons.TASK_ALT, icon_size=35),
                        ft.IconButton(ft.Icons.CALENDAR_MONTH, icon_size=35),
                        ft.IconButton(ft.Icons.SMART_TOY, icon_size=35),
                        ft.IconButton(ft.Icons.TRACK_CHANGES, icon_size=35),
                        ft.IconButton(ft.Icons.TIMER, icon_size=35)
                    ],
                    expand=1
                ),
                ft.IconButton(ft.Icons.SETTINGS, icon_size=35)
            ],
            spacing=5,
        ),
        width=50,
        bgcolor="#000000",
        expand=1
    )



    page.padding=0
    page.add(sidebar)


ft.app(target=main)
