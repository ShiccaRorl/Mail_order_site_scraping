import xlrd
import xlwt
from xlutils.copy import copy

#xlsxを開く
rb = xlrd.open_workbook('sample.xlsx',formatting_info=True)

#シート名表示
print(rb.sheet_names())

#シート番号か、シート名で指定
sheet = sheet_by_index(0)
sheet = rb.sheet_by_name('sheet1')

#セルの値を取得、Cellの属性、もしくは、オブジェクトのメソッドCell_Valueで取得できる
cell = sheet.cell(1,2).value
cell = sheet.cell_value(1, 2)

#列指定で取得(xlrd.sheet.Cellで取れる)
col = sheet.col(1)

#列指定の値取得(Listで取れる)
col_values = sheet.col_values(1)

#行指定で取得
row = sheet.row(1)

#行指定の値取得(Listで取れる)
row_values = sheet.row_values(1)

#二次元配列で取り出し
def get_list_2d_all(sheet):
    return [sheet.row_values(row) for row in range(sheet.nrows)]

l_2d_all = get_list_2d_all(sheet)
print(l_2d_all[1][0])

#テンプレートがある場合はxlutilsで書式を複製する
wb = copy(rb)

#新しいシート追加
sheet = wb.add_sheet('sheet3')

#sheet.write(行, 列, '値')で書き込む
sheet.write(0, 0, 'A')
sheet.write(0, 1, 'B')
sheet.write(1, 0, 10)
sheet.write(1, 1, 20)

#書き込み
wb.save('xlwt_sample.xlsx')