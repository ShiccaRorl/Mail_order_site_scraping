import openpyxl

excel_path1 = "C:/Users/user/Downloads/バックアップ/プログラム/バックアップ/保存/2020年9月在庫表.xlsx"
excel_path2 = "./2020年9月在庫表.xlsx"
wb = openpyxl.load_workbook(excel_path2)

ws = wb["マスター"]
wb.copy_worksheet(ws)
wb.save("./Excel_db.xlsx")