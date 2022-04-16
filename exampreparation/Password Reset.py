def PasswordReset(password):
    new_password = ""
    command = input()
    while command != "Done":
        command = command.split(" ")

        if command[0] == "TakeOdd":
            for i in range(1,len(password)+1):
                if i % 2 == 0:
                    new_password = new_password + password[i-1]
            password = new_password
            print(password)

        elif command[0] == "Cut":
            index = int(command[1])
            length = int(command[2])
            password = password[:index] + password[index+length:]
            print(password)

        elif command[0] == "Substitute":
            substring = command[1]
            substitute = command[2]
            if substring in password:
                password = password.replace(substring, substitute)
                print(password)
            else:
                print("Nothing to replace!")

        command = input()

    print(f"Your password is: {password}")


data = input()
PasswordReset(data)
