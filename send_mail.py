import os
import glob
from smtplib import SMTP
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def sendGmailAttach():
    sender, password = "shicca.rorl.asp@gmail.com", "amourpzaejtpedca" # 送信元メールアドレスとgmailへのログイン情報 
    to = 'shicca.rorl.asp@gmail.com'  # 送信先メールアドレス
    #to = 'bridget111919@yahoo.co.jp'
    sub = 'テストメール送信中' #メール件名
    body = '画像添付しています。'  # メール本文
    host, port = 'smtp.gmail.com', 587

    # メールヘッダー
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = sender
    msg['To'] = to

    # メール本文
    body = MIMEText(body)
    msg.attach(body)

    # 追加部分
    fetch_from_dir = glob.glob(os.getcwd() + "\資料*.*")
    fetch_from_dir_len = len(fetch_from_dir)
    len_cnt = 0
    for target_list in fetch_from_dir:
        print(target_list)

        # 添付ファイルの設定
        attach_file = {
            'name': os.path.basename(target_list),
            'path': target_list
        } # nameは添付ファイル名。pathは添付ファイルの位置を指定
        attachment = MIMEBase('image', 'png')
        file = open(attach_file['path'], 'rb+')
        attachment.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=attach_file['name'])
        msg.attach(attachment)

        # gmailへ接続(SMTPサーバーとして使用)
        gmail=SMTP("smtp.gmail.com", 587)
        gmail.starttls() # SMTP通信のコマンドを暗号化し、サーバーアクセスの認証を通す
        gmail.login(sender, password)
        gmail.send_message(msg)
        len_cnt += 1
        print('メールが' + str(len_cnt) + '/' + str(fetch_from_dir_len) + '件送信されました')


if __name__ == '__main__':
    sendGmailAttach()
    print('メールが全件送信されました')



