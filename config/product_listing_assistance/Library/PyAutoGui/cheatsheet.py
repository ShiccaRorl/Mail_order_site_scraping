
#画面解像度の取得
#要素別にとる
max_x,max_y = pyautogui.size()
#配列にとる
pos         = pyautogui.size()

#マウス現在位置取得
cur_x,cur_y = pyautogui.position()
pos         = pyautogui.position()

# 画像認識
img_x,img_y = pyautogui.locateCenterOnScreen('search.png')
pos         = pyautogui.locateCenterOnScreen('search.png')

#マウス移動、移動先の(x,y)と移動にかける時間(duration)を秒で指定
#注意点としては、左上の頂点は(0,0)ではなく(1,1)なのを忘れない
pyautogui.moveTo(img_x, img_y, duration=2)

#現在位置からの相対移動、かける時間(duration)を秒で指定は同じ
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)

#ドラッグ&ドロップ
#マウス移動、ドラッグ元の(x,y)と移動にかける時間(duration)を秒で指定
#もう一回指定すると、ドロップする
pyautogui.dragTo(x, y, duration=num_seconds)

#現在位置からの相対移動、ドラッグ&ドロップする位置を指定
#もう一回指定すると、ドロップする
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)

#マウスクリック通常設定であれば、左クリック、システムに依存するので、右手用設定時は要注意
pyautogui.click(x,y)

#マウスクリック、連射設定、場所の指定以外にクリック数、クリック間隔、ボタンの指定ができる
pyautogui.click(x,y, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

#その他のマウスクリック
pyautogui.rightClick(x, y)
pyautogui.middleClick(x, y)
pyautogui.doubleClick(x, y)
pyautogui.tripleClick(x, y)

#マウスホイール
pyautogui.scroll(amount_to_scroll, x, y)

#押しっぱなしと解放
pyautogui.mouseDown(x, y, button='left')
pyautogui.mouseUp(x, y, button='left')

# ショートカットを設定するとき
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

# キーを押下・押上するとき
pyautogui.keyDown(key_name)
pyautogui.keyUp(key_name)

#■■■■記述サンプル■■■■

# 画像が画面内にあるか
if pyautogui.onScreen(img_x, img_y):
    pyautogui.moveTo(img_x, img_y, duration=2)
    # pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)

if pyautogui.locateCenterOnScreen('search.png'):
    # 画像があったらD&D
    pyautogui.dragTo(x, y, duration=num_seconds)
    #pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)

if pyautogui.locateCenterOnScreen('search.png'):
    # 画像があったらクリック
    pyautogui.click(img_x, img_y)
    #pyautogui.click(x, y, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

#pip install opencv_python でopencvモジュールがインストールされている場合に限り
#閾値(confidence)が指定できる、以下の場合95%同じだったらTrue
#また、grayscale=Trueを指定すると、グレースケールによる判定を実施し30%前後速度が向上する
if pyautogui.locateCenterOnScreen('search.png',grayscale=True,confidence=0.950):
    # 画像があったらクリック
    pyautogui.click(img_x, img_y)

#2.5秒待ちを入れる
pyautogui.PAUSE = 2.5

#スクリーンの[0,0]座標にカーソルを持っていくと、FailSafeExceptionを任意に発生させることができる
pyautogui.FAILSAFE = True

#マウス移動
pyautogui.moveTo(700, 500) #X, Y
pyautogui.moveTo(None, 100, 2) #700, 500へ2秒で
pyautogui.moveRel(-50, 0) #相対座標
pyautogui.dragTo(415, 508, button = 'left')

#現在地から指定座標までドラッグして離す
pyautogui.dragRel(-20, -20, button = 'left')
pyautogui.click()
pyautogui.click(button='right', clicks=2, interval=0.25)
pyautogui.doubleClick()
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left')
pyautogui.scroll(10)
pyautogui.hscroll(10)

# インターバル0.5秒でshiftを2回押す
pyautogui.press('shift', presses=2, interval=0.5)
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl','c') #同時押し
pyautogui.typewrite('hello world!')

#指定できるキー名
KEYBOAD_KEYS = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
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

## メッセージボックス操作
alert(text='', title='', button='OK')
confirm(text='', title='', buttons=['OK', 'Cancel'])
prompt(text='', title='' , default='')
password(text='', title='', default='', mask='*')

## スクリーンショット作成
# 全体
pyautogui.screenshot('my_screenshot.png')
# 矩形範囲指定
pyautogui.screenshot(region=(0,0, 300, 400))

## 画像認識
#それぞれの要素をとる
pos_x,pos_y,size_x,size_y = pyautogui.locateOnScreen('target.png')
#配列に格納してとる
pos                       = pyautogui.locateOnScreen('target.png')

#画像の中心座標を取る
pos_x,pos_y = pyautogui.center('target.png')

## サーチ範囲(region)指定
# pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400))

## 色の無視(grayscale)
# pyautogui.locateOnScreen('someButton.png', grayscale=True, region=(0,0, 300, 400))

## マッチ誤差(tolerance)[0-100%]
# pyautogui.locateOnScreen('someButton.png', grayscale=True,tolerance=10 ,region=(0,0, 300, 400))
