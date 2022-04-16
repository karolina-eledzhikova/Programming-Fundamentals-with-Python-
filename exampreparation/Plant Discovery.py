number = int(input())
plant_dict = dict()

for _ in range(number):
    current_plants = input().split("<->")
    plant = current_plants[0]
    rarity = current_plants[1]

    if plant not in plant_dict.keys():
        plant_dict[plant] = [rarity, 0.0, 0]
    elif plant_dict[plant] == plant:
        plant_dict[plant][0] += int(rarity)

command = input()
while command != "Exhibition":
    command = command.split(" ")
    current_command = command[0]

    if current_command == "Rate:":
        plant = command[1]
        if not plant_dict.__contains__(plant):
            print("error")
        else:
            rating = command[3]
            plant_dict[plant][1] += int(rating)
            plant_dict[plant][2] += 1

    elif current_command == "Update:":
        plant = command[1]
        if not plant_dict.__contains__(plant):
            print("error")
        else:
            new_rarity = command[3]
            plant_dict[plant][0] = new_rarity

    elif current_command == "Reset:":
        plant = command[1]
        if plant_dict.__contains__(plant):
            plant_dict[plant][1] = 0.0
        else:
            print("error")
    else:
        print("error")
    command = input()
print("Plants for the exhibition:")
for data in plant_dict:
    current_data = data
    current_rarity = int(plant_dict[data][0])
    if plant_dict[data][2] != 0:
        current_average = int(plant_dict[data][1])/int(plant_dict[data][2])
    else:
        current_average = int(plant_dict[data][1])
    print(f"- {current_data}; Rarity: {current_rarity}; Rating: {current_average:.2f}")
