# king-of-time自動入力スクリプト 
このスクリプトは、King of Timeという勤怠に一括で自動で勤怠情報を入力するためのツールです。CUIとGUIの両方で実行可能であり、以下にスクリプトの使い方と準備手順を説明します。

https://www.kingoftime.jp/
## 準備
1. **Python のインストール**: もし未インストールの場合は、[こちら](https://www.python.org/)から最新版の Python をインストールしてください。

    下記が動作確認済みのpythonバージョンです。
    ```
    >> python --version
    Python 3.11.2
    ```
2. #### 仮想環境の作成と起動:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. #### 必要なパッケージをインストール:
    ```コマンドプロンプト
    pip install -r requirements.txt
    ```  
4. #### 設定値の入力:
    `settings.ini` ファイルに以下の設定値を入力してください。
    | 定数名 | 値 |
    ----|---- 
    | id | ご自身のログインID |
    | password | ご自身のログインパスワード |
    | url | 変更しないでください |
    | start_time | 自動入力したい出勤時間(0900など) |　
    | end_time | 自動入力したい退勤時間（1800など） |
    | except_holiday | 土日祝を除くかどうか（True: 土日祝を除く、False: 土日祝を除かない） |
    | input_last_month | 先月分を入力するかどうか（True: 前月分を入力する、False: 今月分を入力する |    

## 実行手順
### CUIで実行
1. `input-king-of-time.py` を以下のコマンドで実行:
    ```bash
    python input-king-of-time.py
    ```
###
 GUIで実行
1. `auto-input-king-of-time.exe` をダブルクリックして GUI 画面を起動
2. 画面上の実行ボタンをクリックして処理を実行

## 備考
* ChromeDriverManagerは実行時のバージョンと同様の ChromeDriverを使用することが可能。ブラウザーのバージョンアップごとにChromeDriverを再インストールする必要がなくなる。

* README.mdの書き方は下記のサイトを参照しました（自分用メモ）。
  https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa
- CUI、GUIのexe化は開発ディレクトリから、実行ファイルを指定して、pyinstallerでできた。下の記事を参考にする。
    - https://weblog.noanoachan.net/python-pyinstaller/
* Mac OSも、できれば対応したいので、なんとかする。
* バグ報告、機能追加要望はissueに記載ください。
* 機能追加、改良あればお気軽にプルリクください。
* GUIツールの画面の設定情報は頻繁に入力する内容でないため、折りたためるようにする。
* load_settings関数で設定を読み込む必要なし。init関数で設定を読み込めばいい。修正する。
 
## リリースノート
### 現在のバージョン

*1.0.2*

### 更新内容

**Ver.1.0.0からVer1.0.1への変更点**
* [add] 「土日祝を除く」設定を追加
* [fix] ChromeDriverManagerの読み込み時のエラー解消

**Ver.1.0.0からVer1.0.2への変更点**
* [add] GUI機能を作成
* [add] パッケージの一括ダウンロードを作成
* [add] CUI、GUIのexeを作成
* [add] 「前月分を入力する」設定を追加
  
# 作者
kerokeropyu
