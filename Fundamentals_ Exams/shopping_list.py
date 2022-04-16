text = input().split("!")

line = input()

while line != "Go Shopping!":
    current_line = line.split(" ")
    command = current_line[0]

    if command == "Urgent":
        item = current_line[1]
        if item not in text:
            text.insert(0,item)
            # text.append(item)
        else:
            pass

    elif command == "Unnecessary":
        item = current_line[1]
        if item in text:
            text.remove(item)
        else:
            pass

    elif command == "Correct":
        old_item = current_line[1]
        new_item = current_line[2]

        if old_item in text:
            text.insert(text.index(old_item), new_item)
            a = text.index(old_item)
            del text[a]
        else:
            pass

    elif command == "Rearrange":
        item = current_line[1]
        if item in text:
            text.remove(item)
            text.append(item)
        else:
            pass

    line = input()

print(", ".join(text))