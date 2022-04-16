total_price_without_taxes = 0.0
total_amount_of_taxes = 0.0
total_price_with_taxes = 0.0
costumer = input()

while True:
    if costumer == "special":
        break
    elif costumer == "regular":
        break
    price = float(costumer)

    if price < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += price
        total_price_with_taxes = 20/100 * price
        total_amount_of_taxes += total_price_with_taxes
    costumer = input()

total_price = total_price_without_taxes + total_amount_of_taxes
if costumer == "special":
    discount = 10/100*total_price
    total_price -= discount

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

