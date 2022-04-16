word = list(input())
word = list(map(str, word))
message = ""

line = input()

while line != "Decode":
    command_list = line.split("|")
    command = command_list[0]  # tuk izliza komandata
    index = int(command_list[1])  # tuk kolko puti operacii da pravi na dumata
    letters = str(command_list[2])  # bukvata koqto shte tretirame

    if command == "Move":
        current_command = word[:index]
        current_command += str(current_command)
        print(current_command)


    elif command == "Insert":
        current_command = word.insert(index, letters)
        message += current_command
    elif command == "ChangeAll":
        pass

    line = input()

word = list(map(str, word))
print(f"The decrypted message is: {message}]")
