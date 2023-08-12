import configparser

class Setting:
    def __init__(self):
        self.SETTINGS_INI_PATH = 'settings2.ini'
        self.url: str = ''
        self.start_time: str = ''
        self.end_time: str = ''
        self.except_holidays: bool = False
        self.input_last_month: bool = False
        self.id: str = ''
        self.password: str = ''

        self.config = configparser.ConfigParser()
        self.config.read(self.SETTINGS_INI_PATH)
        self.setting = self.config['YOUR_SETTINGS']
        self.load_settings(self.setting)
    
    # 設定情報取得
    # setattr(オブジェクト, 追加したい属性, 値)
    def load_settings(self, config) -> None:
        for key in ['url', 'start_time', 'end_time', 'id', 'password']:
            setattr(self, key, config.get(key))
        self.except_holidays = config.getboolean('exclude_holidays', False)
        self.input_last_month = config.getboolean('input_last_month', False)
    
    # 設定情報を保存
    def save_settings(self, url: str, start_time: str, end_time: str, except_holidays: bool, input_last_month: bool, user_id: str, password: str) -> None:
        self.url = url
        self.start_time = start_time
        self.end_time = end_time
        self.except_holidays = except_holidays
        self.input_last_month = input_last_month
        self.id = user_id
        self.password = password

        # 設定ファイルの更新
        self.setting['url'] = url
        self.setting['start_time'] = start_time
        self.setting['end_time'] = end_time
        self.setting['exclude_holidays'] = str(except_holidays)
        self.setting['input_last_month'] = str(input_last_month)
        self.setting['id'] = user_id
        self.setting['password'] = password

        # 設定ファイルの保存
        with open(self.SETTINGS_INI_PATH, 'w') as configfile:
            self.config.write(configfile)
