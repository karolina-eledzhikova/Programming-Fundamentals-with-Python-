number_of_pieces = int(input())
input_dict = dict()

for i in range(number_of_pieces):
    composer_and_key = input().split("|")
    piece = composer_and_key[0]
    composer = composer_and_key[1]
    key = composer_and_key[2]

    if piece not in input_dict.keys():
        input_dict[piece] = [composer, key]

commands = input()
while commands != "Stop":
    current_commands = commands.split("|")

    if current_commands[0] == "Add":
        piece = current_commands[1]
        composer = current_commands[2]
        key = current_commands[3]
        if piece not in input_dict:
            input_dict[piece] = [composer, key]

            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif current_commands[0] == "Remove":
        piece = current_commands[1]

        if piece in input_dict:
            input_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif current_commands[0] == "ChangeKey":
        piece = current_commands[1]
        new_key = current_commands[2]
        if piece in input_dict:
            input_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    commands = input()
# да принтирам останалата част от задачата (речник в речник)

for piece in input_dict:
    current_piece = piece
    current_composer = input_dict[piece][0]
    current_key = input_dict[piece][1]
    print(f"{current_piece} -> Composer: {current_composer}, Key: {current_key}")
