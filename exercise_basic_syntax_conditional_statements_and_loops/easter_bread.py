budget = float(input())
price_for_1kg_flour = float(input())

loaves = 0
colored_eggs = 0
money_left = 0

price_for_1pack_of_eggs = 75 / 100 * price_for_1kg_flour
price_for_1l_milk = price_for_1kg_flour*1.25
price_for_0_250l_milk = price_for_1l_milk * 0.250

bread_price = price_for_1kg_flour + price_for_1pack_of_eggs + price_for_0_250l_milk

# Start Cooking

while budget >= bread_price:
    loaves += 1
    colored_eggs += 3
    budget -= bread_price

    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
