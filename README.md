# king-of-time自動入力スクリプト 
 
# 準備
* pythonをインストール
下記から最新版のpyhonをインストールください。すでにインストール済みの方は不要。
https://www.python.org/

* seleniumをインストール
以下のコマンドでインストールできます。
```コマンドプロンプト
pip install selenium
```

* ChromeDriverManagerをインストール
実行時のバージョンと同様の ChromeDriverを使用することが可能。
```コマンドプロンプト
pip install webdriver-manager
```

* 以下のinput-king-of-time.pyファイルの定数を入力ください。
・ID：ご自身のログインID
・PASSWORD：ご自身のログインパスワード
・URL：ご自身のking-of-timeのURL（これは個人によって変わらないのですかね？）
・BEGIN_TIME ：自動入力したい出勤時間(0900など)
・FINISH_TIME　：自動入力したい退勤時間（1800など）

# 実行手順
input-king-of-timeフォルダ配下でpythonファイル（input-king-of-time.py）を実行。
下記のコマンドで実行できます。
```コマンドプロンプト
 python input-king-of-time.py
```
 
# Note
バッチファイルは未完成。

ChromeDriverManagerは実行時のバージョンと同様の ChromeDriverを使用することが可能。
ブラウザーのバージョンアップごとにChromeDriverを再インストールする必要がなくなる。

# Author
二課　Oku
 
