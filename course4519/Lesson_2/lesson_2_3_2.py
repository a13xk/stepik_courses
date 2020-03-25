import xlrd
from math import floor

workbook = xlrd.open_workbook('trekking2.xlsx')
sheet_names = workbook.sheet_names()
sheet_reference = workbook.sheet_by_name(sheet_names[0])
sheet_weights = workbook.sheet_by_name(sheet_names[1])

products = sheet_reference.col_values(0)[1:39]
calories = sheet_reference.col_values(1)[1:39]
proteins = sheet_reference.col_values(2)[1:39]
fats = sheet_reference.col_values(3)[1:39]
carbohydrates = sheet_reference.col_values(4)[1:39]

weighted_products = sheet_weights.col_values(0)[1:13]
weights = sheet_weights.col_values(1)[1:13]


reference = list()

for i, p in enumerate(products):
    row = dict()
    row['product_name'] = p
    row['calories'] = calories[i]
    row['proteins'] = proteins[i]
    row['fats'] = fats[i]
    row['carbohydrates'] = carbohydrates[i]
    reference.append(row)


def calculate_value(weight: float, value_per_100_weight: float) -> float:
    if type(value_per_100_weight) is str:
        value_per_100_weight = 0.0
    res = (value_per_100_weight * weight)/100.0
    return res
#


def get_product_calories(product_name: str, ref: list) -> float:
    for list_item in ref:
        if product_name == list_item.get("product_name"):
            return list_item.get("calories")
    return 0.0
#


def get_product_proteins(product_name: str, ref: list) -> float:
    for list_item in ref:
        if product_name == list_item.get("product_name"):
            return list_item.get("proteins")
    return 0.0
#


def get_product_fats(product_name: str, ref: list) -> float:
    for list_item in ref:
        if product_name == list_item.get("product_name"):
            return list_item.get("fats")
    return 0.0
#


def get_product_carbohydrates(product_name: str, ref: list) -> float:
    for list_item in ref:
        if product_name == list_item.get("product_name"):
            return list_item.get("carbohydrates")
    return 0.0
#


weighted_products_calculated = list()
for i, wp in enumerate(weighted_products):
    wpc = dict()
    wpc['product_name'] = wp
    wpc['weight'] = weights[i]
    wpc['calories'] = calculate_value(
        weight=wpc.get("weight"),
        value_per_100_weight=get_product_calories(
            product_name=wpc.get("product_name"),
            ref=reference
        )
    )
    wpc['proteins'] = calculate_value(
        weight=wpc.get("weight"),
        value_per_100_weight=get_product_proteins(
            product_name=wpc.get("product_name"),
            ref=reference
        )
    )
    wpc['fats'] = calculate_value(
        weight=wpc.get("weight"),
        value_per_100_weight=get_product_fats(
            product_name=wpc.get("product_name"),
            ref=reference
        )
    )
    wpc['carbohydrates'] = calculate_value(
        weight=wpc.get("weight"),
        value_per_100_weight=get_product_carbohydrates(
            product_name=wpc.get("product_name"),
            ref=reference
        )
    )
    weighted_products_calculated.append(wpc)

wpc_calories = [x.get("calories") for x in weighted_products_calculated]
wpc_proteins = [x.get("proteins") for x in weighted_products_calculated]
wpc_fats = [x.get("fats") for x in weighted_products_calculated]
wpc_carbohydrates = [x.get("carbohydrates") for x in weighted_products_calculated]

print(f"Total calories: {floor(sum(wpc_calories))}")
print(f"Total proteins: {floor(sum(wpc_proteins))}")
print(f"Total fats: {floor(sum(wpc_fats))}")
print(f"Total carbohydrates: {floor(sum(wpc_carbohydrates))}")

print(f"{floor(sum(wpc_calories))} {floor(sum(wpc_proteins))} {floor(sum(wpc_fats))} {floor(sum(wpc_carbohydrates))}")
pass
