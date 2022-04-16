def StringGame(message):
    command = input()
    while command != "Done":
        command = command.split(" ")

        if command[0] == "Change":
            char = command[1]
            replacement = command[2]
            if char in message:
                message = message.replace(char,replacement)
            print(message)

        elif command[0] == "Includes":
            substring = command[1]
            if substring in message:
                print("True")
            else:
                print("False")

        elif command[0] == "End":
            substring = command[1]
            if substring in message:
                if message.endswith(substring):
                    print("True")
                else:
                    print("False")

        elif command[0] == "Uppercase":
            message = message.upper()
            print(message)
        elif command[0] == "FindIndex":
            char = command[1]
            index = []
            for i,ch in enumerate(message):
                if ch == char:
                    index.append(i)
            print(index[0])
        elif command[0] == "Cut":
            start_index = int(command[1])
            count = int(command[2])
            message = message[start_index:count+start_index]
            print(message)

        command = input()

data = input()
StringGame(data)
