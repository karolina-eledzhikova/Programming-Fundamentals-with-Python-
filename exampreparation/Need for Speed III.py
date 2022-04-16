number_of_cars = int(input())
car_dict = dict()

for i in range(number_of_cars):
    current_input = input().split("|")
    car = current_input[0]
    mileage = float(current_input[1])
    fuel = float(current_input[2])

    if car not in car_dict.keys():
        car_dict[car] = [mileage, fuel]

command = input()
while command != "Stop":
    command = command.split(" : ")
    current_command = command[0]

    if current_command == "Drive":
        car = command[1]
        distance = float(command[2])
        fuel = float(command[3])
        if car_dict[car][1] <= fuel:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car][0] += distance
            car_dict[car][1] -= fuel
            print(f"{car} driven for {distance:.0f} kilometers. {fuel:.0f} liters of fuel consumed.")
            if car_dict[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del car_dict[car]
    elif current_command == "Refuel":
        car = command[1]
        fuel = float(command[2])
        sum = car_dict[car][1] + fuel
        refueled = 0
        if sum > 75:
            refueled = 75 - car_dict[car][1]
            car_dict[car][1] += refueled
        else:
            car_dict[car][1] += fuel
            refueled = fuel
        print(f"{car} refueled with {refueled:.0f} liters")
    elif current_command == "Revert":
        car = command[1]
        kilometers = float(command[2])
        amount_reverted = car_dict[car][0] - kilometers
        if amount_reverted < 10000:
            car_dict[car][0] = 10000
        else:
            car_dict[car][0] = amount_reverted
            print(f"{car} mileage decreased by {int(kilometers)} kilometers")
    command = input()


for data in car_dict:
    current_car = data
    current_mileage = car_dict[data][0]
    current_fuel = car_dict[data][1]
    print(f"{current_car} -> Mileage: {current_mileage:.0f} kms, Fuel in the tank: {current_fuel:.0f} lt.")
