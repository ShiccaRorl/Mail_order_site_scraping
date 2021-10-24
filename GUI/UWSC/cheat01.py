#ロードモジュール
# -*- coding: utf-8 -*-
import os,sys,re,time,subprocess
import pyautogui

#カレントマウス座標(tuple型)
CUR_MOUSE_POS = pyautogui.position()
X,Y = CUR_MOUSE_POS
#※変数型がわからなくなったら print(type(変数))で確認

#画面解像度(tuple型)
RESOLUTION = pyautogui.size()
X,Y = RESOLUTION

#画面の色深度(2/4/8/16/24/32bitの識別)
im  = pyautogui.screenshot()
colordepth = im.dtype

#座標の存在確認
if pyautogui.onScreen(x, y):
    print("x,yは画面内にあります")

#デフォルト待ち時間(sec)
pyautogui.PAUSE = 2.5

# Fail-Safeモードの有効化(失敗しても中断しなくなる、FailSafeExceptionをキャッチできる)
pyautogui.FAILSAFE = True

# マウス座標移動(絶対座標と移動時間を指定)
pyautogui.moveTo(x, y, duration=num_seconds)

# マウス座標移動(相対座標と移動時間を指定)
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)

# Drag&DropのDrag位置指定(絶対座標と移動時間を指定,ボタン指定)
pyautogui.drag(x, y, duration=num_seconds, button='right')  

# Drag&DropのDrop位置指定(絶対座標と移動時間を指定)
pyautogui.dragTo(x, y, duration=num_seconds)

# Drag&DropのDrop位置指定(相対座標と移動時間を指定)
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)

# マウスクリック(絶対座標とクリック回数、クリック間隔、ボタンを指定)
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks,interval=secs_between_clicks, button='left')
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks,interval=secs_between_clicks, button='right')
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks,interval=secs_between_clicks, button='middle')

# マウスクリック(絶対座標を指定)
pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)

# マウスホイール(ノッチ数と絶対座標を指定[座標は省略可])
#垂直ホイール
pyautogui.scroll(amount_to_scroll,x=moveToX,y=moveToY)
#水平ホイール
pyautogui.hscroll(amount_to_scroll,x=moveToX,y=moveToY) 

# マウスホールド/リリース(絶対座標とボタンを指定)
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

# タイピング(日本語未対応:文字列と入力間隔を指定)
pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)

# タイピング(キー単位で入力、ファンクションキー押下可能、入力間隔も指定)
pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)

# ショートカットキー(特定キーの同時押しを指定)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

# キーホールド/リリース(キー名を指定)
pyautogui.keyDown(key_name)
pyautogui.keyUp(key_name)

# キー押下(キー名を指定)
pyautogui.press(key_name)

# キー名一覧
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']


#メッセージボックス(Info)
pyautogui.alert(text='メッセージ',title='タイトル',button='ボタンの文字')

#メッセージボックス(Confirm)
result = pyautogui.confirm(text='メッセージ', 'タイトル', buttons=['選択1', '選択2'])

#メッセージボックス(Prompt[Input])
result = pyautogui.prompt(text='メッセージ', 'タイトル',default='デフォルト値')

#メッセージボックス(Password[Input])
result = pyautogui.password(text='メッセージ', 'タイトル',default='デフォルト値', mask='*')

# スクリーンショット(全体)
pyautogui.screenshot(Filename)

# スクリーンショット(範囲)
pyautogui.screenshot(Filename,region=(x1,y1,x2,y2))

# 画像識別(指定画像の発見位置の左,上,幅,高さ、が取得できる)
pos = pyautogui.locateOnScreen('looksLikeThis.png')

# 認識後Centerで中央座標を取ることができる、locateCenterOnScreenと同等
centerpos = pyautogui.center(pos)

# 画像識別(グレイスケール化検索,色相を気にせず形状で判別する場合高速化できる)
pos = pyautogui.locateOnScreen('looksLikeThis.png',grayscale=True)

# 画像識別(検索範囲指定)
pos = pyautogui.locateOnScreen('looksLikeThis.png',region=(rx1,ry1,rx2,ry2))

# あいまい画像識別(confidenceで閾値が指定できる、95%合致なら0.95)
pos = pyautogui.locateOnScreen('looksLikeThis.png',confidence=0.95)

# あいまい画像識別(検索範囲指定、confidenceは閾値)
pos = pyautogui.locateOnScreen('looksLikeThis.png',region=(rx1,ry1,rx2,ry2),confidence=0.95)

# 画面認識(画面上に複数ある場合全て検出)
# 順次処理の場合
for pos in pyautogui.locateAllOnScreen('looksLikeThis.png')
    print(pos)

# リスト化して指定個数目(num)を処理する場合
poslist = list(pyautogui.locateAllOnScreen('looksLikeThis.png'))
x,y,h,w = poslist[num]

# 画像識別(指定画像の発見位置の中央X,Y、が取得できる)
# グレースケール(grayscale)、検索範囲(region=)や、あいまい画像認識(confidence)は同様に使える
pos = pyautogui.locateCenterOnScreen('looksLikeThis.png')

# 指定座標のRGB値を取得する(tuple型)
rgb = pyautogui.pixel(x,y)
r,g,b = rgb

# 指定座標のRGB値がマッチするか
if pyautogui.pixelMatchesColor(x, y, (r,g,b)):
    print('Color Matched !!')

# 指定座標のRGB値がマッチするか(誤差指定[tolerance(%)])
if pyautogui.pixelMatchesColor(x, y, (r,g,b),tolerance=num):
    print('Color Matched !!')