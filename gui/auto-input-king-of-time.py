import flet as ft
import configparser
import datetime
from flet import (
    Page,
    colors
)

# 変数
dt = datetime.datetime.today()
today = str(dt.date())
# url = ''
# start_time = ''
# end_time = ''
# except_holidays = ''
# id = '123'
# password = ''

config = configparser.ConfigParser()
config.read('../settings.ini')
settings = config['DEFAULT']
url = settings.get('url')
start_time = settings.get('start_time')
end_time = settings.get('end_time')
except_holidays = settings.getboolean('exclude_holidays', False)
id = settings.get('id')
password = settings.get('password')

# 設定読み込み
# def load_settings():
#     config = configparser.ConfigParser()
#     config.read('../settings.ini')
#     settings = config['DEFAULT']
#     url = settings.get('url')
#     start_time = settings.get('start_time')
#     end_time = settings.get('end_time')
#     except_holidays = settings.getboolean('exclude_holidays', False)
#     id = settings.get('id')
#     password = settings.get('password')
#     # print(url, start_time, end_time, except_holidays, id, password)

def test():
    print(1)

def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        print("testtest")
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys...")
    )

    page.title = "Auto Input King-Of-Time"
    # page.bgcolor = colors.SECONDARY
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.AUTO_MODE_OUTLINED),
        leading_width=40,
        title=ft.Text("king of time 自動入力"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        # bgcolor=ft.colors.DEEP_PURPLE,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="終了", on_click=test),
                ]
            ),
        ],
    )
    page.add(
        ft.Container(
            content=ft.Text("今日の日付:"+today),
            alignment=ft.alignment.top_right,
            border_radius=10,
        ),
        ft.TextField(label="URL", value=url),
        ft.ResponsiveRow(
            [
                ft.TextField(label="出勤時間", keyboard_type="NUMBER", max_length=4, hint_text="0900", value=start_time, col={"md": 6}),
                ft.TextField(label="退勤時間", keyboard_type="NUMBER", max_length=4, hint_text="1800", value=end_time, col={"md": 6}),
            ],
            run_spacing={"xs": 10},
        ),

        ft.TextField(label="ID", keyboard_type="TEXT", value=id),
        ft.TextField(label="パスワード", keyboard_type="VISIBLE_PASSWORD", password=True, can_reveal_password=True, value=password),
        
        ft.Container(
            content=ft.Checkbox(value=True, label="土日を除く"),
            alignment=ft.alignment.top_right,
            border_radius=10,
        ),
        # ft.label(),
        ft.Container(
            ft.ElevatedButton(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(value="実行", size=20),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=3,
                    ),
                    padding=ft.padding.all(5),
                ),
                style=ft.ButtonStyle(
                    color={
                        ft.MaterialState.HOVERED: ft.colors.WHITE,
                        ft.MaterialState.FOCUSED: ft.colors.BLUE,
                        ft.MaterialState.DEFAULT: ft.colors.GREY_300,
                    },
                    shape=ft.StadiumBorder(),
                ),
                # bgcolor=ft.colors.DEEP_PURPLE,
            ),
            alignment=ft.alignment.top_right,
            border_radius=10,
        ),
    )


ft.app(target=main)