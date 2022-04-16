def SecretChat(message):
    command = input()
    while command != "Reveal":
        command = command.split(":|:")

        if command[0] == "InsertSpace":
            index = int(command[1])
            if 0 <= index <= len(message):
                message = message[:index] + " " + message[index:]
                print(message)
        elif command[0] == "Reverse":
            substring = command[1]
            if substring in message:
                message = message.replace(substring, "", 1)
                substring = substring[::-1]
                message += substring
                print(message)
            else:
                print("error")

        elif command[0] == "ChangeAll":
            substring = command[1]
            replacement = command[2]

            message = message.replace(substring, replacement)
            print(message)

        command = input()

    print(f"You have a new text message: {message}")


data = input()
SecretChat(data)
