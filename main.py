import flet as ft
import Gpt_core



tf_user = ft.TextField(label="User Input",bgcolor='#39914d',color='#080808', width=300, height=300, multiline=True, max_lines=9, min_lines=9,
                       border_radius=15)


text_gpt = ft.TextField(label="GPT Output",bgcolor='#39914d', color='#080808', multiline=True, max_lines=100, min_lines=15,
                        border_radius=25, width=1500, height=500 )

def create_row_1():
    container = ft.Container(
        width=0,
        height=0,
        content=tf_user,
        padding=ft.Padding(-1, -1, -1, -1),
    )
    card = ft.Card(
        elevation=10,
        color='#1fad40',
        width=1500,
        height=100,
        content=container,
    )
    return ft.Row([
        card
    ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

def create_row_3():


    return ft.Row([
        text_gpt
    ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

def main(page: ft.Page):
    # Налаштовуємо властивості сторінки
    page.title = "FletGpt"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = '#1e542b'
    page.window_maximized = True
    r1 = create_row_1()
    r3 = create_row_3()

    def click_button(e):
        from Gpt_core import send_request
        text_gpt.value = send_request(tf_user.value)
        text_gpt.update()
        page.update()

    bt = ft.ElevatedButton(text="Send", bgcolor='#39914d',color='#080808', width=300, height=50,elevation=8, on_click=click_button)
    row = ft.Row([
        bt,
    ],
        alignment=ft.MainAxisAlignment.END,
    )

    container = ft.Container(
        height=140,
        padding=ft.Padding(70, 70, 17, 0),
        content=row,
    )
    column = ft.Column(
        [
            r3,
            container,
            r1,
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page.add(column)
ft.app(target=main)
