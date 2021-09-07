from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, portrait , landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader


class PdfConfig:
    title = "No title" # タイトル
    author = "" # オーナー
    subject = "" # サブタイトル

    default_fontname = "MS Gothic"
    image_resolution = 300 # DPI
    jpeg_quality = 95 # Jpeg 圧縮率
    font_adjustment = 0.85 # フォント間隔
    image_embeded = True # 画像同梱

    def __init__(self):
        pass

config = PdfConfig()
output_filename = 'output_new.pdf' #出力ファイル名固定

#キャンバス作成
newPdfPage = canvas.Canvas(output_filename)

# 用紙 / 向き
# A0,A1,A2,A3,A4,A5,A6
# B0,B1,B2,B3,B4,B5,B6
# LETTER, LEGAL, ELEVENSEVENTEEN
page_size['width'], page_size['height'] = A4
#縦
newPdfPage.setPageSize(portrait(A4))
#横
#newPdfPage.setPageSize(landscape(A4))
#カスタムサイズ(cm指定)
#newPdfPage.setPageSize(page_size['width'], page_size['height'])

newPdfPage.setAuthor(config.author) # オーナー設定
newPdfPage.setTitle(config.title) # タイトル設定
newPdfPage.setSubject(config.subject) #サブタイトル設定

#画像貼り付け(ファイル名,Xoffset,Yoffset,画像幅,画像高さ,アスペクト比維持,アンカー)
newPdfPage.drawImage(imagefilename, 0+image_offset_x, 0+image_offset_y,width=page_size['width'],
height=page_size['height'], preserveAspectRatio=True, anchor='c')

#文字書き込み(座標X,座標Y,文字列)
str_out = "Hello World"
newPdfPage.drawString(100, 730, str_out)

# Canvasに書き込みと改ページ
newPdfPage.showPage()

#そのまま書いていけばOK
pdf_canvas.drawString(100, 700, "２ページ目です。")
pdf_canvas.showPage()

# ファイル保存
newPdfPage.save()