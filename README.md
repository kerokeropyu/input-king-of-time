# king-of-time自動入力スクリプト 
 
## 準備
1. #### pythonをインストール

    下記から最新版のpyhonをインストールください。
    すでにインストール済みの方は不要（バージョンはあまり古いものでない限り、おそらく実行可能）。
    
    https://www.python.org/

2. #### seleniumをインストール
   
    以下のコマンドでインストールできます。
    ```コマンドプロンプト
    pip install selenium
    ```

3. #### ChromeDriverManagerをインストール

    実行時のバージョンと同様の ChromeDriverを使用することが可能。
    ```コマンドプロンプト
    pip install webdriver-manager
    ```

4. #### jpholidayをインストール
    「土日祝」を省く設定の動作のために、jpholidayをインストールします。
    ```コマンドプロンプト
    pip install jpholiday
    ```

5. #### 以下のinput-king-of-time.pyファイルの定数を入力ください。
    | 定数名 | 値 |
    ----|---- 
    | ID | ご自身のログインID |
    | PASSWORD | ご自身のログインパスワード |
    | URL | ご自身のking-of-timeのURL |
    | BEGIN_TIME | 自動入力したい出勤時間(0900など) |
    | FINISH_TIME | 自動入力したい退勤時間（1800など） |
    | EXCEPT_HOLIDAY | 土日祝を除くかどうか（True: 土日祝を除く、False: 土日祝を除かない） |

## 実行手順
* Windowsの場合
  
    - 下記のいずれかの手順で実行
      - ~~dist配下の「InputKingOfTime_ver1-0-0.exe」をダブルクリックで実行。~~（こちらメンテナンスしていません。少々お待ちください。）
      - input-king-of-time配下でpythonファイル（input-king-of-time.py）を実行。
       以下のコマンドで実行できます。
        ```コマンドプロンプト
        python input-king-of-time.py
        ```
* ~~Macの場合~~（Macで動作しないことを確認済み。）
    - ~~下記の手順で実行~~
        - ~~input-king-of-time配下でpythonファイル（input-king-of-time.py）を実行。
            以下のコマンドで実行できます。~~
            ```コマンドプロンプト
            python input-king-of-time.py
            ```
 
## 備考
* ChromeDriverManagerは実行時のバージョンと同様の ChromeDriverを使用することが可能。ブラウザーのバージョンアップごとにChromeDriverを再インストールする必要がなくなる。
* pip installが多くなってきたので、**どなたか**まとめてインストールするバッチを作成してくれると助かります。
* コマンドプロンプトで実行するのが手間なので、**GUIツールを鋭意作成中**です。しばらくお待ちください。
* README.mdの書き方は下記のサイトを参照しました（自分用メモ）。
  https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa

## リリースノート
### 現在のバージョン

*1.0.1*

### 更新内容

**Ver.1.0.0からVer1.0.1への変更点**
* [add]「土日祝を除く」設定を追加
* [fix]ChromeDriverManagerの読み込み時のエラー解消

# 作者
kerokeropyu
