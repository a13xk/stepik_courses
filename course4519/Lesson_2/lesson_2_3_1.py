import xlrd

workbook = xlrd.open_workbook('trekking1.xlsx')
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name(sheet_names[0])


products = sheet.col_values(0)[1:39]
calories = sheet.col_values(1)[1:39]

products_calories = dict()

for i, p in enumerate(products):
    products_calories[p] = calories[i]
    products_calories[p] = products_calories[p]
# print(products_calories)

products_calories_sorted = sorted(products_calories.items(), key=lambda x: (-x[1], x[0]))
for p in products_calories_sorted:
    print(p[0])
