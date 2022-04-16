def world_tour(destinations):
    command = input()
    while command != "Travel":
        command = command.split(":")

        if command[0] == "Add Stop":
            index = int(command[1])
            string = command[2]
            if 0 <= index <= len(destinations):
                destinations = destinations[:index] + string + destinations[index:]

        elif command[0] == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2])
            if 0 <= start_index <= end_index < len(destinations):
                destinations = destinations[:start_index] + destinations[end_index+1:]

        elif command[0] == "Switch":
            old_string = command[1]
            new_string = command[2]
            destinations = destinations.replace(old_string, new_string)

        print(destinations)
        command = input()

    print(f"Ready for world tour! Planned stops: {destinations}")


data = input()
world_tour(data)