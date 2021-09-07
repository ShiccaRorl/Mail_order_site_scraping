import pyaudio

#録音
def RecWavFile(FileName,Record_Seconds):
    audiobuff = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 #モノラル
    RATE = 44100 #サンプルレート（録音の音質）
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,channels = CHANNELS,rate = RATE,input = True,frames_per_buffer = audiobuff)
    print("Now Recording...")
    all = []
    for i in range(0, int(RATE / audiobuff * Record_Seconds)):
        data = stream.read(audiobuff) #音声を読み取って、
        all.append(data) #データを追加
    print("Finished Recording.")

    stream.close()
    p.terminate()
    wavFile = wave.open(FileName, 'wb')
    wavFile.setnchannels(CHANNELS)
    wavFile.setsampwidth(p.get_sample_size(FORMAT))
    wavFile.setframerate(RATE)
    wavFile.writeframes(b"".join(all))
    wavFile.close()

#再生
def PlayWavFie(Filename):
    try:
        wf = wave.open(Filename, "r")
    except FileNotFoundError: #ファイルが存在しなかった場合
        print("[Error 404] No such file or directory: " + Filename)
        return 0

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)

    audiobuff = 1024
    data = wf.readframes(audiobuff)
    while data != '':
        stream.write(data)
        data = wf.readframes(audiobuff)
    stream.close()
    p.terminate()

if __name__ is "__main__":
    #録音
    RecWavFile("sample.wav",2)
    #再生
    PlayWavFie("sample.wav")