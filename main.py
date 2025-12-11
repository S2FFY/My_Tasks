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
<<<<<<< HEAD
                ft.IconButton(ft.Icons.SETTINGS, on_click=lambda e: navigate(4)),  # снизу
=======
                ft.IconButton(ft.Icons.SETTINGS, icon_size=35)
>>>>>>> 0593bc834ad1f13f1489ac46ff72cdc247681a5c
            ],
            spacing=5,
        ),
        width=50,
        bgcolor="#000000",
        expand=1
    )

<<<<<<< HEAD
    main_area = ft.Container(
        ft.TextButton(ft.CheckboxTheme('dsffg')),
        expand=True
=======
>>>>>>> 0593bc834ad1f13f1489ac46ff72cdc247681a5c


    page.padding=0
    page.add(sidebar)


ft.app(target=main)
