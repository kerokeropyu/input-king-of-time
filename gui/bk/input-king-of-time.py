import flet as ft
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    TextField,
    UserControl,
    colors,
    icons,
)
import configparser
import datetime

def close():
     return True
today = 1


class Setting(UserControl):
    def __init__(self, url, start_time, end_time, except_holidays, id, password):
            self.url = url
def save_clicked(self):
    config = configparser.ConfigParser()
    config.read('../settings.ini')
    settings = config['YOUR_SETTINGS']
    # セクション内の値の書き換え
    settings['start_time'] = '1300'
        # 書き込みモードでオープン
    with open('settings.ini', 'w') as configfile:
        # 指定したconfigファイルを書き込み
        settings.write(configfile)
    # self.update()

class AutoInput:
    def auto_input():
        return 1

def main(page: Page):
    today= datetime.datetime.today()
    year=str(today.year)
    month = str(today.month)
    
    config = configparser.ConfigParser()
    config.read('../settings.ini')
    settings = config['DEFAULT']

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
                    ft.PopupMenuItem(text="終了", on_click=close),
                ]
            ),
        ],
    )
    # view=
    page.add(
        # 今日の日付ラベル
        ft.Container(
            # content=ft.Text("今日の日付:"+str(today.date())),
            alignment=ft.alignment.top_right,
            border_radius=10,
        ),
        # 設定内容を保存ボタン
        ft.Row(
            [
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.icons.SAVE_AS_ROUNDED,
                        icon_color="blue400",
                        icon_size=30,
                        tooltip="設定内容を保存します。",
                        on_click=save_clicked,
                    ),
                    alignment=ft.alignment.top_left,
                ),
            ]
        ),
        # 入力対象月
        ft.TextField(label="入力対象月",  disabled=True, keyboard_type="TEXT", value=year+'/'+month),
        # 前月分を入力するチェックボックス
        ft.Container(
            content=ft.Checkbox(value=settings.get('input_last_month'), label="前月分を入力する"),
            alignment=ft.alignment.top_right,
            border_radius=10,
            on_click=test
        ),
        # 出勤時間、退勤時間テキストボックス
        ft.ResponsiveRow(
            [
                ft.TextField(label="出勤時間", keyboard_type="NUMBER", max_length=4, hint_text="0900", value=settings.get('start_time'), col={"md": 6}),
                ft.TextField(label="退勤時間", keyboard_type="NUMBER", max_length=4, hint_text="1800", value=settings.get('end_time'), col={"md": 6}),
            ],
            run_spacing={"xs": 10},
        ),
        # URLテキストボックス
        ft.TextField(label="URL", value="url"),
        # IDテキストボックス
        ft.TextField(label="ID", keyboard_type="TEXT", value=settings.get('id')),
        # パスワードテキストボックス
        ft.TextField(label="パスワード", keyboard_type="VISIBLE_PASSWORD", password=True, can_reveal_password=True, value=settings.get('password')),

        # 土日を除くチェックボックス
        ft.Container(
            content=ft.Checkbox(value=settings.get('exclude_holidays'), label="土日を除く"),
            alignment=ft.alignment.top_right,
            border_radius=10,
        ),
        # 実行ボタン
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
            ),
            alignment=ft.alignment.top_right,
            border_radius=10,
            on_click=self.save_clicked
        ),
    )

ft.app(target=main)
