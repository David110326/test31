

import xlrd
book = xlrd.open_workbook("testdata.xlsx")
sheet = book.sheet_by_index(0)
#sheet = book.sheet_by_name("mydata")
rows = sheet.nrows
cols = sheet.ncols
for r in range(rows):
    r_value= sheet.row_values(r)
    print(r_value)
