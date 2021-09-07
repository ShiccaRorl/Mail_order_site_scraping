import speech_recognition

#音声入力デバイス一覧
def MicCheck():
    for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

#ファイルから入力の場合
#with speech_recognition.AudioFile('sample.wav') as source:
#    audio = r.record(source)

#入力デバイスから直接の場合
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

##Sphinxの場合
#print(r.recognize_sphinx(audio))

##Google Speech Recognitionの場合
#短ければキーなしでもいける
print(r.recognize_google(audio,language='ja-JP'))
#長時間の場合はAPIキーが必要
#print(r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY",language='ja-JP'))

#Google Cloud Speech APIの場合
#GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"jsonファイルの中身をペースト"
#print(r.recognize_google_cloud(audio,credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))

##Wit.aiの場合（日本語未対応）
#WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"
#print(r.recognize_wit(audio, key=WIT_AI_KEY))

##Microsoft Bing Voice Recognitionの場合
#BING_KEY = "INSERT BING API KEY HERE" 
#print(r.recognize_bing(audio, key=BING_KEY))

##Microsoft Azure Speech
#AZURE_SPEECH_KEY = "INSERT AZURE SPEECH API KEY HERE"
#print(r.recognize_azure(audio, key=AZURE_SPEECH_KEY))

##Houndify APIの場合
#HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  
#HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  
#print(r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID,client_key=HOUNDIFY_CLIENT_KEY))

##IBM Speech to Textの場合
#IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"
#IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"
#print(r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))