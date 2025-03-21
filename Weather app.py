import flet as ft
import  requests

def main(page: ft.Page):
    page.title = "Weather app"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='input city',width=400)
    weather_data = ft.Text('')

    def get_info(e):
        if len(user_data.value) <2:
            return

        API = "cd9e5510a0d76ba2dd246c0b5b463581"
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric"
        res = requests.get(URL).json()
        temp = res['main']['temp']
        weather_data.value = "Weather: " + str(temp)
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text("Weather app")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data]
               , alignment= ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data]
               , alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text = "Get", on_click= get_info)]
               , alignment= ft.MainAxisAlignment.CENTER),
    )

ft.app(target=main)