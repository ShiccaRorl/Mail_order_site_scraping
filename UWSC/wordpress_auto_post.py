# -*- coding: utf-8 -*-

#モジュール読み込み
import os,sys,re,time,subprocess
import pyautogui
import win32gui
import configparser
import xlrd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

##デスクトップのハイライト
def dhlight(x1, y1, x2, y2):
    hwnd=win32gui.WindowFromPoint((x1,y1))
    hdc=win32gui.GetDC(hwnd)
    rc=(x1, y1, x2, y2)
    win32gui.DrawFocusRect(hdc, rc)
    win32gui.ReleaseDC(hwnd,hdc)

##Html Elementのハイライト
def hhlight(element):
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
    original_style = element.get_attribute('style')
    apply_style("background: white; border: 1px solid blue;")
    time.sleep(.3)
    apply_style(original_style)

# 設定ファイル読み込み
CONF_FILEPATH = 'setting.ini'
config = configparser.ConfigParser()
config.read( CONF_FILEPATH, 'UTF-8')

#confファイルで[]で囲った場所を指定
config_server = config['Server']
config_page   = config['SitePage']
config_excel  = config['WriteFile']

#confで[]の下に変数とデータを入れてる内容を取得
uid = config_server['login_id']
upw = config_server['login_pw']
url = config_server['login_url']
search_button = config_page['write_fourm']
xlsxfile = config_excel['excel_file']

##Chromeを初期化
options = Options()

##Chromeのパス（通常は指定不要、ポータブル版などを使う場合やstable/beta切り替え時）
options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
options.add_argument('--start-maximized')
options.add_argument('--disable-gpu')

## ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome(options=options,executable_path="C:\Python37\chromedriver.exe")

#要素が見つかるまでの待ち時間、ドライバ生成直後にのみ指定可能
driver.implicitly_wait(10) 

#ページが完全にロードされるまで最大で5秒間待つよう指定、ドライバ生成直後にのみ指定可能
driver.set_page_load_timeout(5)

#Javascript実行が終了するまで最大5秒間待つように指定
driver.set_script_timeout(5)

#URL移動
driver.get(url)

#ログイン処理
user_id_elm  = driver.find_element_by_id("user_login")
#エレメントハイライト
hhlight(user_id_elm)
user_id_elm.send_keys(uid)

user_pw_elm  = driver.find_element_by_id("user_pass")
hhlight(post_fourm)
user_pw_elm.send_keys(upw)

login_submit = driver.find_element_by_id("wp-submit")
hhlight(post_fourm)
login_submit.submit()

time.sleep(5)

#投稿
menu_post_elm = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/ul/li[3]/a/div[3]")
hhlight(menu_post_elm)
menu_post_elm.click()

time.sleep(2)

#新規追加
new_post_elm = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/a")
hhlight(new_post_elm)
new_post_elm.click()

time.sleep(2)

#Excelファイルを開く
wb = xlrd.open_workbook(xlsxfile)

#シート指定
sheet = wb.sheet_by_name('sheet1')

#最終行検出
last_row = sheet.nrows

#全行2次元配列に読み込み(メモリに余裕がなければ、1行ずつ読んだ方がいい)
readcells = [sheet.row_values(row) for row in range(sheet.nrows)]

time.sleep(5)

#記事タイトル
card_title_elm = driver.find_element_by_xpath("//*[@id='post-title-0']")

#記事本文
card_body_elm = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div[3]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div/div/div/div/p")

# driverを終了
driver.close()