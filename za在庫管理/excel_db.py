import openpyxl
wb = openpyxl.load_workbook('C:\\temp\\foo.xlsx')

ws = wb.worksheets[0]
wb.copy_worksheet(ws)
wb.save('C:\\temp\\foo2.xlsx')