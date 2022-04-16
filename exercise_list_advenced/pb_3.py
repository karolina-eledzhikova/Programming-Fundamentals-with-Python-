number = input().split(" ")
condition = True
counter = 0

index_list = input().split(" ")

while condition:
    if not index_list[0] == "end":
        first_index = index_list[0]
        second_index = index_list[1]
        counter += 1

        if int(first_index) < 0 or int(first_index) > len(number) or int(second_index) < 0 or int(second_index) > len(
                number) or int(first_index) == int(second_index):
            print("Invalid input! Adding additional elements to the board")
            middle = int(len(number) / 2)
            text = '-' + str(counter) + 'a'
            number.insert(middle, text)
            number.insert(middle + 1, text)
        elif number[int(first_index)] == number[int(second_index)]:
            remove_first = number[int(first_index)]
            remove_second = number[int(second_index)]
            print(f"Congrats! You have found matching elements - {number[int(second_index)]}!")
            number.remove(remove_first)
            number.remove(remove_second)
            if len(number) == 0:
                print(f"You have won in {counter} turns!")
                break
        else:
            print("Try again!")

    else:
        break

    index_list = input().split(" ")

if len(number) > 0:
    print("Sorry you lose :(")

for i in range(len(number)):
    print(number[i], end=" ")
