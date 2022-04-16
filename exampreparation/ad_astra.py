# def print_output(matches_to_print):
#     for m in matches_to_print:
#         product_to_print = match.group("product")
#         date_to_print = match.group("date")
#         calories_to_print = int(match.group("calories"))
#         print(f"Item: {product_to_print}, Best before: {date_to_print}, Nutrition: {calories_to_print}")
#
#
# import re
#
# text = input()
# # calculate the total calories.
# total_calories = 0
# expression = r"([|#])(?P<product>[A-zA-z]+|([A-zA-z]+ [A-zA-z]+))\1(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]+)\1"
# matches = re.finditer(expression, text)
#
# output = list()
# for match in matches:
#     product = match.group("product")
#     date = match.group("date")
#     calories = int(match.group("calories"))
#     total_calories += calories
#     line_for_print = "Item: {0}, Best before: {1}, Nutrition: {2}\n".format(product,date,calories)
#     output.append(line_for_print)
#
# days = total_calories // 2000
#
# print(f"You have food to last you for: {days} days!")
# print("".join(output))
#
import re

info = input()
pattern = r"\#([a-z A-Z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|\|([a-z A-Z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|"
result = re.findall(pattern, info)
items = []
calories = 0
for item in result:
    current_item = [el for el in item if el != ""]
    items.append(current_item)
    calories += int(current_item[2])
number_of_days = int(calories / 2000)

print(f"You have food to last you for: {number_of_days} days!")

for data in items:
    product = data[0]
    date = data[1]
    current_calories = data[2]
    print(f"Item: {product}, Best before: {date}, Nutrition: {current_calories}")
