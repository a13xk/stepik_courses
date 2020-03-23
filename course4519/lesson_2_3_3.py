import xlrd
from math import floor


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


workbook = xlrd.open_workbook('trekking3.xlsx')
sheet_names = workbook.sheet_names()
sheet_reference = workbook.sheet_by_name(sheet_names[0])
sheet_weights_per_days = workbook.sheet_by_name(sheet_names[1])

ref_products = sheet_reference.col_values(0)[1:39]
ref_calories = sheet_reference.col_values(1)[1:39]
ref_proteins = sheet_reference.col_values(2)[1:39]
ref_fats = sheet_reference.col_values(3)[1:39]
ref_carbohydrates = sheet_reference.col_values(4)[1:39]

reference = list()

for i, proteins in enumerate(ref_products):
    row = dict()
    row['product_name'] = proteins
    row['calories'] = ref_calories[i]
    row['proteins'] = ref_proteins[i]
    row['fats'] = ref_fats[i]
    row['carbohydrates'] = ref_carbohydrates[i]
    reference.append(row)


days = sheet_weights_per_days.col_values(0)[1:100]
weighted_products = sheet_weights_per_days.col_values(1)[1:100]
weights = sheet_weights_per_days.col_values(2)[1:100]


products_per_days = dict()
for i, d in enumerate(days):
    day_name = "day "+str(int(d))
    if products_per_days.get(day_name) is None:
        products_per_days[day_name] = dict()
        products_per_days[day_name]['weighted_products'] = list()
        products_per_days[day_name]['weights'] = list()
    products_per_days[day_name]['weighted_products'].append(weighted_products[i])
    products_per_days[day_name]['weights'].append(weights[i])

for key in products_per_days:

    # Accumulate calories
    if products_per_days.get(key).get("calories") is None:
        products_per_days[key]['calories'] = list()
    for i, weight in enumerate(products_per_days.get(key).get("weights")):
        calories = calculate_value(
            weight=weight,
            value_per_100_weight=get_product_calories(
                product_name=products_per_days.get(key).get("weighted_products")[i],
                ref=reference
            )
        )
        products_per_days[key]['calories'].append(calories)

    # Accumulate proteins
    if products_per_days.get(key).get("proteins") is None:
        products_per_days[key]['proteins'] = list()
    for i, weight in enumerate(products_per_days.get(key).get("weights")):
        proteins = calculate_value(
            weight=weight,
            value_per_100_weight=get_product_proteins(
                product_name=products_per_days.get(key).get("weighted_products")[i],
                ref=reference
            )
        )
        products_per_days[key]['proteins'].append(proteins)

    # Accumulate fats
    if products_per_days.get(key).get("fats") is None:
        products_per_days[key]['fats'] = list()
    for i, weight in enumerate(products_per_days.get(key).get("weights")):
        fats = calculate_value(
            weight=weight,
            value_per_100_weight=get_product_fats(
                product_name=products_per_days.get(key).get("weighted_products")[i],
                ref=reference
            )
        )
        products_per_days[key]['fats'].append(fats)

    # Accumulate carbohydrates
    if products_per_days.get(key).get("carbohydrates") is None:
        products_per_days[key]['carbohydrates'] = list()
    for i, weight in enumerate(products_per_days.get(key).get("weights")):
        carbohydrates = calculate_value(
            weight=weight,
            value_per_100_weight=get_product_carbohydrates(
                product_name=products_per_days.get(key).get("weighted_products")[i],
                ref=reference
            )
        )
        products_per_days[key]['carbohydrates'].append(carbohydrates)


for key in products_per_days:
    total_calories = floor(sum(products_per_days.get(key).get("calories")))
    total_proteins = floor(sum(products_per_days.get(key).get("proteins")))
    total_fats = floor(sum(products_per_days.get(key).get("fats")))
    total_carbohydrates = floor(sum(products_per_days.get(key).get("carbohydrates")))

    # print(f"{key}\ttotal calories: {total_calories}\ttotal proteins: {total_proteins}\ttotal fats: {total_fats}\ttotal carbohydrates: {total_carbohydrates}")
    print(f"{total_calories} {total_proteins} {total_fats} {total_carbohydrates}")

pass
