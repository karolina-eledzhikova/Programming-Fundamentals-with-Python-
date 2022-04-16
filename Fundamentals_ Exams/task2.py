def right(numbers, length):
    return numbers[-length:]


numbers = input().split("|")
numbers = list(map(int, numbers))

player_hp = 0

line = input()

while line != "Game over":
    command_line = line.split("@")
    command = command_line[0]

    if command == "Shoot Left":
        start_index = int(command_line[1])
        length = int(command_line[2])
        if start_index > len(numbers)-1:
            pass
        else:
            index_to_shoot = start_index+length+1
            if index_to_shoot < len(numbers) - 1:
                shoot_attack = numbers[index_to_shoot] - 5
                player_hp+=5
                if shoot_attack < 5:
                    numbers[index_to_shoot] = 0
                else:
                    numbers[index_to_shoot] = shoot_attack

        # if start_index >= 0 and start_index < len(numbers):
        #     current_target = numbers[start_index]
        #     current_target -= lenght
        # da proverq dali ne izliza ot granici....

    elif command == "Shoot Right":
        start_index = int(command_line[1]) #4
        length = int(command_line[2]) # 5
        if start_index > len(numbers) - 1:
            pass
        else:
            right(numbers, length)
            index_to_shoot = start_index - length + 1
            if index_to_shoot < len(numbers) - 1:
                shoot_attack = numbers[index_to_shoot] - 5
                player_hp += 5
                if shoot_attack < 5:
                    numbers[index_to_shoot] = 0
                else:
                    numbers[index_to_shoot] = shoot_attack

    elif command == "Reverse":
            numbers.reverse() ###da go proverq

    line = input()


numbers = list(map(str, numbers))
output = " - ".join(numbers)
print(output)