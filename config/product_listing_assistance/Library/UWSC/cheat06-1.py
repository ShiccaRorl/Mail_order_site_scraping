# モジュールのロード
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

##Chromeを操作
options = Options()
##Chromeのパス（通常は指定不要、ポータブル版などを使う場合やstable/beta切り替え時）
options.binary_location = 'PATH/To/Chrome.exe'
##起動オプション指定[Google Chrome まとめWiki](http://chrome.half-moon.org/43.html)
options.add_argument('--kiosk')
options.add_argument('--disable-gpu')
##ブラウザのオプション指定
options.add_experimental_option("prefs", {
    "download.default_directory": "%DriveRoot%¥temp¥",
    "plugins.always_open_pdf_externally": True
})
## ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome(options=options,executable_path="./chromedriver.exe")

##Firefoxを操作
#options = Options()
##Firefoxのパス(通常は指定不要、ポータブル版などを使う場合や派生ブラウザ時)
#options.binary_location = 'Path/To/Firefox.exe'
##Firefox起動オプション(https://developer.mozilla.org/ja/docs/Mozilla/Command_Line_Options)
#options.add_argument('-browser')
#driver = webdriver.Firefox(options=options,executable_path="geckodriver")

#要素が見つかるまでの待ち時間、ドライバ生成直後にのみ指定可能
driver.implicitly_wait(10) 

#ページが完全にロードされるまで最大で5秒間待つよう指定、ドライバオブジェクト生成直後にのみ指定可能
driver.set_page_load_timeout(5)

#Javascript実行が終了するまで最大5秒間待つように指定
driver.set_script_timeout(5)

#URL移動
driver.get('https://www.google.com/')

#要素がクリックできるようになるまで待つ
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "q")))

## EC.xx の待機条件については、以下のようなものがある、ほぼ単語のままの意味
# title_is # 完全一致
# title_contains # 〜を含む
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be # 要素がチェックONまたはチェックOFFになるまで待機
# element_located_selection_state_to_be
# alert_is_present　# Alertが表示されるまで待機する

## By.xx については以下のようなものが指定できる
# ID
# XPATH
# LINK_TEXT
# PARTIAL_LINK_TEXT
# NAME
# TAG_NAME
# CLASS_NAME
# CSS_SELECTOR

#ページが完全にロードされるまで最大で30秒間待機
driver.set_page_load_timeout(30)

#カレントウインドウのポジション(左上隅の座標)をX座標:100,Y座標:200に設定
driver.set_window_position(100,200)

#カレントウインドウを最大化する
driver.maximize_window()

#カレントウインドウのサイズを幅:100,高さ:200に設定する
driver.set_window_size(100,200)

#カレントウィンドウの座標(左上隅の座標)を取得(Dict型で返る)
coordinate = driver.get_window_position()

#カレントウィンドウのサイズを取得(Dict型で返る)
culSize = driver.get_window_size()

#カレントページのURLを取得
print(driver.current_url)

#カレントページのウィンドウハンドルを取得
print(driver.current_window_handle)

#カレントページのタイトルの取得
print(driver.title)

＃ブラウザを履歴中で一段階戻す
driver.back()

#ブラウザを履歴中で一段階進める
driver.forward()

#ページを更新(ブラウザのリフレッシュ)
driver.refresh()

#カレントページのソースを取得、保存したり、BeautifulSoupに渡して解析したりする
pages = driver.page_source.encode('utf-8')

#全てのウィンドウハンドルを取得(複数のウインドウを開いているとき)
allHandles = driver.window_handles
#ウィンドウハンドルはリスト型
print(allHandles[0])
#switch_to_windowを使って、切り替えできる
driver.switch_to_window(allHandles[0])

#カレントドメインの全てのクッキーを取得する(List型で返る)
allCookies = driver.get_cookies()

#クッキー名からクッキーを検索
cookie = driver.get_cookie("ABC")

#クッキー名を指定して削除
driver.delete_cookie("ABC")

#全てのクッキーを削除
driver.delete_all_cookies()

#表示されたダイアログの文字列を取得する
alertText = Alert(driver).text

#"OK or Cancel"の確認でOKを選択
Alert(driver).accept()

#カレントページのスクリーンショットを取得し保存(取得できた場合はTRUE)
if driver.get_screenshot_as_file("screenshot.png"):
    print("ScreenShot Sucsess")
else:
    print("ScreenShot Failed")

#エレメント取得
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()

## 要素に関しては以下の設定ができる(パブリックメソッド)
## 単一要素
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector
## 複数要素
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
# 複数取得時はforで回す

## 要素から属性操作
TargetElement = driver.find_element_by_name("q")

# クリア
TargetElement.clear()

# 文字列入力
TargetElement.send_keys("STR")

# 仮想キー
TargetElement.send_keys(Keys.ENTER)

# クリック
TargetElement.click()

# 送信
TargetElement.submit()

# 属性値取得
TargetElement.get_attribute("value")

# 要素のタグ名を取得する
TargetElement.tag_name

# 要素のinnerTextを出力
TargetElement.text

# CSSプロパティ名(text-align)からプロパティ値を取得
TargetElement.value_of_css_property("text-align")

# 要素の左上隅の座標を取得(dict)
TargetElement.location

# セレクトタグ内のオプションに含まれるインナーテキストを出力
for i in range(len(TargetElement.options)):
    print(TargetElement.options[i].text)

# 選択状態にあるオプションのインナーテキストを出力
for i in range(len(TargetElement.all_selected_options)):
    print(TargetElement.all_selected_options[i].text)

# 要素の表示状態を判定
if TargetElement.is_displayed():
    print("True:Displaed")
else:
    print("False:IsDisplayed")

# 要素がEnableかどうか判定
if TargetElement.is_enabled():
    print("True:Enable")
else:
    print("False:Disable")

#要素が選択されているかどうか判定
if TargetElement.is_selected():
    print("True:Selected")
else:
    print("False:IsSelected")

#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
select = Select(TargetElement)
    #セレクトタグのオプションをインデックス番号から選択する
    select.select_by_index(indexNum)
    #指定したインデックス番号のオプションを未選択にする
    select.deselect_by_index(indexNum)
    #セレクトタグのオプションをテキストを指定して選択する
    select.select_by_visible_text(text)
    #全て未選択にする
    select.deselect_all()
    #指定したValue属性のオプションを未選択にする
    select.deselect_by_value(value)
    #テキストで指定したオプションを未選択にする
    select.deselect_by_visible_text(text)


##ActionChainsは直前に検索(find_*)した要素に対して操作する
#Controlキーを押下しながらエレメントをクリック(PyAutoGUIと組み合わせる場合、バッティング注意、どちらかのモジュールでpid/handleで操作しているとエラーになる、座標指定なら問題なし)
ViewButton = driver.find_element_by_id("button")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL)
actions.click(ViewButton)
actions.key_up(Keys.CONTROL)
actions.perform()

#Controlキーを押下しながら指定の座標へマウスカーソル移動してクリックする
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL)
actions.move_by_offset(400,320)
actions.click()
actions.perform()

#Shiftキーを押下しながら"abc"を入力し、Shiftキーを押下しないで"de"を入力
actions = ActionChains(driver)
actions.key_down(Keys.SHIFT)
actions.send_keys("abc")
actions.key_up(Keys.SHIFT)
actions.send_keys("de")
actions.perform()

#要素をドラッグした状態でX/Y方向に100ポイントカーソル移動させる
select_element = driver.find_element_by_id("target")
actions = ActionChains(driver)
actions.click_and_hold(select_element)
actions.move_by_offset(100,100)
actions.perform()

#移動元(src)の要素と移動先(dst)の要素を取得
src_element  = driver.find_element_by_id("draggable")
dst_element  = driver.find_element_by_id("droppable")
#3秒間待機してドラッグ前の状態を確認
time.sleep(3)
#移動元の要素をドラッグし移動先の要素へカーソル移動、重ねるだけdropしない
actions = ActionChains(driver)
actions.click_and_hold(src_element)
actions.move_to_element(dst_element)
actions.perform()

#要素をX方向に250ポイント,y方向に200ポイント移動する、ドラッグアンドドロップを実行
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(element,250,200)
actions.perform()

#移動元(src)の要素と移動先(dst)の要素を取得
src_element = driver.find_element_by_id("draggable")
dst_element = driver.find_element_by_id("droppable")
#3秒間待機して移動前の位置を確認
time.sleep(3)
#移動元の要素をドラッグし移動先の要素へドロップ
actions = ActionChains(driver)
actions.drag_and_drop(src_element,dst_element)
actions.perform()

# driverを終了
driver.close()

# 全て終了
driver.quit()