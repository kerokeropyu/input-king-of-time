# coding: utf-8
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.support.select import Select
import datetime
import time
import calendar
import settings
import jpholiday

# 現在の年と月を取得
today = datetime.datetime.now()
year = today.year
month = today.month

# その年と月の日数を取得
num_days = calendar.monthrange(year, month)[1]

# 実行時のバージョンと同様の ChromeDriverをインストール
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
# 指定した要素が見つかるまでの待ち時間を設定（1秒）
driver.implicitly_wait(1)

# 勤怠データ入力
def input_work_data():
    # 打刻種別で「出勤」を選択、出勤時間を入力
    Select(driver.find_element(By.XPATH, '//*[@id="recording_type_code_1"]')).select_by_index(1) 
    driver.find_element(By.XPATH, '//*[@id="recording_timestamp_time_1"]').send_keys(settings.BEGIN_TIME)
    # 打刻種別で「退勤」を選択、退勤時間を入力
    Select(driver.find_element(By.XPATH, '//*[@id="recording_type_code_2"]')).select_by_index(2) 
    driver.find_element(By.XPATH, '//*[@id="recording_timestamp_time_2"]').send_keys(settings.FINISH_TIME)
    # 打刻登録
    driver.find_element(By.XPATH, '//*[@id="button_01"]').click()

# 土日かどうか判定
def is_weekend(dt: datetime.date):
    return dt.weekday() in [5, 6]

# 祝日かどうか判定
def is_japanese_holiday(dt: int):
    return jpholiday.is_holiday(datetime.date(year, month, dt))

try:
    # 勤怠アプリにアクセス
    driver.get(settings.URL)

    # トップページへ戻る
    driver.execute_script("document.getElementsByClassName('htBlock-buttonM htBlock-buttonNormal htBlock-dialog_yes')[0].click()")

    # ID、PASSWORDを入力し、ログインボタンを押下
    driver.find_element(By.XPATH, '//*[@id="login_id"]').send_keys(settings.ID)
    driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys(settings.PASSWORD)
    driver.find_element(By.XPATH, '//*[@id="login_button"]').click()

    # 「土日・祝日を除く」設定を取得
    except_holiday = settings.EXCEPT_HOLIDAY

    # 月初から月末までの勤務データを入力
    for i in range(1, num_days + 1):
        # 「土日祝も除く」設定がTrueの場合、かつ、土日または祝日の場合、forを飛ばす
        date = datetime.date(year, month, i)
        if (except_holiday == True) and (is_weekend(date) or is_japanese_holiday(i)):
            continue
        # トップページから編集画面へ遷移
        Select(driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/div[5]/div[1]/table/tbody/tr[{i}]/td[1]/p/select')).select_by_index(1)
        # 勤怠データ入力
        input_work_data()
except Exception as e:
    print(e)
    print("エラーが発生しました。")
finally:
    # ブラウザを閉じる
    driver.close()
    driver.quit()