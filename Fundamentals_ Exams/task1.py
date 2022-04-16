google_income  = float(input())
number_of_users = int(input())

total_money = 0

for i in range(1, number_of_users+1):
    number_of_searches = int(input())

    if i % 3 == 0:
        total_money += number_of_searches*google_income*3
        if number_of_searches > 5:
          total_money += number_of_searches*google_income*2
        if number_of_searches == 1:
            continue

    if number_of_searches >5:
        total_money += number_of_searches*google_income*2

    if number_of_searches == 1:
        continue




print(f"Total money earned: {total_money:.2f}")