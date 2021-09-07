import speake3

engine = speake3.Speake()
engine.set('voice', 'en') # 言語指定
engine.set('speed', '107') # 再生速度
engine.set('pitch', '99') # ピッチ
engine.say("Hello world!") # 音声合成
engine.talkback() # 再生