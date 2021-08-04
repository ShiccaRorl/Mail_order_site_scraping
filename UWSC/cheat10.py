import configparser

# 設定ファイルのパス
CONF_FILEPATH = 'sample.conf'

config = configparser.ConfigParser()

config.read( CONF_FILEPATH, 'UTF-8')

# confファイルで[]で囲った場所を指定
config_webserver = config['webserver']
config_proxy     = config['proxy']

# confで[]の下に変数とデータを入れてる内容を取得
HOST      = config_webserver['ipaddress']
PORT      = config_webserver['port']
SSL       = config_webserver['useSSL']

PROXY     = config_proxy['ipaddress']
PROXYPORT = config_proxy['port']
PROTOCOL  = config_proxy['proto']

#新しいセッションディレクティブを作る
section = 'AppServer'
config.add_section(section)
config.set(section, 'host', HOST)
config.set(section, 'port', PORT)
config.set(section, 'proxy_proto', PROTOCOL)
config.set(section, 'proxy', PROXY)
config.set(section, 'proxy_port', PROXYPORT)

#書き込む
with open('server.conf', 'w') as file:
    config.write(file)