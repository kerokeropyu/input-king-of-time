import flet as ft
import datetime
from flet import (
    Page,
    colors
)
from settings import Setting
import subprocess

# 定数
PAGE_TITLE = 'Auto Input King-Of-Time'
APP_BAR_TITLE = 'king of time 自動入力'
FILE_PATH = '../input-king-of-time.py'

# 自動入力
def execute_input_king_of_time(*args):
    subprocess.run(['python', FILE_PATH])

# # 自動入力中止 ボタン配置が難しいので保留
# def stop_input_king_of_time(process: subprocess.Popen):
#     process.terminate()
    
# メイン処理
def main(page: ft.Page):
    # 日付を取得
    today = datetime.datetime.today()
    year = str(today.year)
    month = str(today.month)
    # 設定をインスタンス化
    s = Setting()

    # 画面を閉じる
    def close_window():
        return True
    
    # 設定情報を保存
    def write_settings(e):
        url = url_field.value
        start_time = start_time_txt.value
        end_time = end_time_txt.value
        except_holidays = exclude_weekends_chk.content.value
        input_last_month = chk_last_month.content.value
        id = id_field.value
        password = password_txt.value
        
        # print("URL:", url)
        # print("Start Time:", start_time)
        # print("End Time:", end_time)
        # print("Except Holidays:", except_holidays)
        # print("Input Last Month:", input_last_month)
        # print("ID:", id)
        # print("Password:", password)
        
        # 設定情報を更新する
        s.save_settings(url, start_time, end_time, except_holidays, input_last_month, id, password)
        page.update()
    
    page.title = PAGE_TITLE
    # page.bgcolor = colors.SECONDARY
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.AUTO_MODE_OUTLINED),
        leading_width=40,
        title=ft.Text(APP_BAR_TITLE),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        # bgcolor=ft.colors.DEEP_PURPLE,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="終了", on_click=close_window),
                ]
            ),
        ],
    )

    # 入力対象月
    target_month_month = ft.TextField(label="入力対象月",  disabled=True, keyboard_type="TEXT", value=year+' / '+month)
    # 先月分を入力するチェックボックス
    chk_last_month = ft.Container(content=ft.Checkbox(value=True, label="前月分を入力する"), alignment=ft.alignment.top_right, border_radius=10)

    # 今日の日付ラベル
    today_lbl = ft.Container(content=ft.Text("今日の日付:"+str(today.date())), alignment=ft.alignment.top_right, border_radius=10)

    # 設定内容を保存ボタン
    save_btn = ft.Row([ft.Container(content=ft.IconButton(icon=ft.icons.SAVE_AS_ROUNDED, icon_color="blue400", icon_size=30, tooltip="設定内容を保存します。", on_click=write_settings), alignment=ft.alignment.top_left)])

    # 出勤時間テキストボックス
    start_time_txt = ft.TextField(label="出勤時間", keyboard_type="NUMBER", max_length=4, hint_text="0900", value=s.start_time, col={"md": 6})

    # 退勤時間テキストボックス
    end_time_txt = ft.TextField(label="退勤時間", keyboard_type="NUMBER", max_length=4, hint_text="1800", value=s.end_time, col={"md": 6})

    time_fields = ft.ResponsiveRow([
        start_time_txt,
        end_time_txt
    ], run_spacing={"xs": 10})

    # URLテキストボックス
    url_field = ft.TextField(label="URL", value=s.url)

    # IDテキストボックス
    id_field = ft.TextField(label="ID", keyboard_type="TEXT", value=s.id)

    # パスワードテキストボックス
    password_txt = ft.TextField(label="パスワード", keyboard_type="VISIBLE_PASSWORD", password=True, can_reveal_password=True, value=s.password)

    # 土日を除くチェックボックス
    exclude_weekends_chk = ft.Container(content=ft.Checkbox(value=True, label="土日を除く"), alignment=ft.alignment.top_right, border_radius=10)

    # 実行ボタン
    execute_button = ft.Container(
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
        on_click=execute_input_king_of_time
    )

    page.add(
        today_lbl,
        save_btn,
        target_month_month,
        chk_last_month,
        time_fields,
        url_field,
        id_field,
        password_txt,
        exclude_weekends_chk,
        execute_button,
    )

ft.app(target=main)