# king-of-time自動入力スクリプト 
 
## 準備
1. #### pythonをインストール

    下記から最新版のpyhonをインストールください。  
    すでにインストール済みの方は不要（バージョンはあまり古いものでない限り、おそらく実行可能）。
    
    https://www.python.org/

    下記が動作確認済みのpythonバージョンです。
    ```
    >> python --version
    Python 3.11.2
    ```
2. #### pythonの仮想環境を作成し、立ち上げる
    コマンドプロンプトで、プロジェクトフォルダ配下に移動し、
    以下のコマンドでpythonの仮想環境を作成する。
    ```コマンドプロンプト
    python -m venv venv
    ```
    以下のコマンドでpythonの仮想環境を立ち上げる。
    ```コマンドプロンプト
    venv\Scripts\activate
    ```

3. #### 必要なパッケージをインストールする。
    以下のコマンドで実行に必要なパッケージをインストールする。
    ```コマンドプロンプト
    pip install -r requirements.txt
    ```  
4. #### settings.iniに設定値を入力ください。
    | 定数名 | 値 |
    ----|---- 
    | id | ご自身のログインID |
    | password | ご自身のログインパスワード |
    | url | 変更しないでください |
    | start_time | 自動入力したい出勤時間(0900など) |
    | end_time | 自動入力したい退勤時間（1800など） |
    | except_holiday | 土日祝を除くかどうか（True: 土日祝を除く、False: 土日祝を除かない） |
    | input_last_month | 先月分を入力するかどうか |    

## 実行手順
* #### CUIで実行
  
    - 下記のいずれかの手順で実行
      - dist配下の「input-king-of-time.exe」をダブルクリックで実行。
      - input-king-of-time配下でpythonファイル（input-king-of-time.py）を実行。
       以下のコマンドで実行できます。
        ```コマンドプロンプト
        python input-king-of-time.py
        ```
* #### GUIで実行
    - 下記の手順で実行
        - dist配下の「auto-input-king-of-time.exe」をダブルクリックで画面が起動する。
        - 画面上の実行ボタンを押下することで処理が実行される。

## 備考
* ChromeDriverManagerは実行時のバージョンと同様の ChromeDriverを使用することが可能。ブラウザーのバージョンアップごとにChromeDriverを再インストールする必要がなくなる。

* README.mdの書き方は下記のサイトを参照しました（自分用メモ）。
  https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa
- CUI、GUIのexe化は開発ディレクトリから、実行ファイルを指定して、pyinstallerでできた。下の記事を参考にする。
    - https://weblog.noanoachan.net/python-pyinstaller/
    - 外部ファイルを参照するときは、下のコマンドで、フォルダを指定しないといけないらしい。
* Mac OSも、できれば対応したいので、なんとかする。
* バグ報告、機能追加要望はissueに記載ください。
* 機能追加、改良あればお気軽にプルリクください。
 
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
