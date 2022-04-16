def cac_price(produckt, quantity):
    if produckt == "coffee":
        return quantity * 1.5
    elif produckt == "coke":
        return quantity * 1.4
    elif produckt == "water":
        return quantity * 1
    elif produckt == "snacks":
        return quantity * 2


current_produkt = input()
current_quantity = int(input())

final_price = cac_price(current_produkt, current_quantity)
print(f"{final_price:.2f}")