days = int(input())
numbers_players = int(input())
energy_group = float(input())
water_for_one_person = float(input())
food_for_one_person = float(input())
energy_loss = float(input()) # количеството енергийна загуба, за всеки от дните

total_energy_loss = 0
current_energy = 0
current_total_food = 0
current_total_water = 0

while energy_group <= 0:
    total_water = days * numbers_players * water_for_one_person
    total_food = days * numbers_players * food_for_one_person
    lost_energy_on_the_first_day = energy_group - energy_loss

    for day in range(1, days + 1):
        if day % 2 == 0:
            total_energy_loss = lost_energy_on_the_first_day - (5/100*lost_energy_on_the_first_day)
            current_total_water = total_water - (30/100*total_water)
        if day % 3 == 0:
            current_total_food = total_food / numbers_players
            current_energy = total_energy_loss + (10/100 * total_energy_loss)
        if not current_energy <= 0:
            print(f"You are ready for the quest. You will be left with - {current_energy} energy!")
        else:
            print(f"You will run out of energy. You will be left with {current_total_food} food and {current_total_water} water.")



