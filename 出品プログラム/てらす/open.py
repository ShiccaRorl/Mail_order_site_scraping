# -*- encoding: utf-8 -*-

import subprocess
import webbrowser

# ①ファイルを開く
subprocess.Popen(["start", "", r"開くファイルのpath"], shell=True)

# ②フォルダを開く
subprocess.Popen(["explorer",  r"開くフォルダのpath"], shell=True)

# ③Webページを開く
webbrowser.open("URL")
