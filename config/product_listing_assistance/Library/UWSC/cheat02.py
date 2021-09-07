# -*- coding: utf-8 -*-
import win32api
import win32gui
import win32con
import win32com.client

##ディスク容量の表示
disks = win32api.GetDiskFreeSpaceEx()
for i in disks:
    r = round(i/(1024**3),1)
    print(str(r)+" GB")

##OKウィンドウの表示
a = win32gui.MessageBox(None,'Contents','Title',1)
print(a) # ok -> 1, cancel -> 2

##IE実行
ie = win32com.client.Dispatch("InternetExplorer.Application")
ie.Visible = True
ie.Addressbar = True
ie.Navigate("https://www.google.com")

##WScript.Shell経由でメモ帳起動
wshShell = win32com.client.Dispatch("WScript.Shell")
wshShell.Run("notepad.exe")

##COMオブジェクト経由でExcel操作 (この辺りは)
xlApp = win32com.client.Dispatch("Excel.Application")
#Excelを表示させる
xlApp.Visible = 1
#Excelファイルを開く
wb = xlApp.Workbooks.Open("開くファイル")
#指定したシートを操作可能にする
sheet = wb.Worksheets("開きたいシート名(左から1,2,3..のように数字で選択でも可)")
#指定したシートを選択状態にする。
sheet.Activate() 
#セルにデータを入力する
sheets.Range("A4").Value = "入力データ"
#行の高さ、列の幅を変更する
sheet.Rows("1:1").RowHeight = 25
sheet.Columns("A:A").ColumnWidth = 15
#上書き保存
wb.Save()
#名前をつけて保存
wb.SaveAs("保存するファイルパスと名前")
#Excelファイルを閉じる。
wb.Close()