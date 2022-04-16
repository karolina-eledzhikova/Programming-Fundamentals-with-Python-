text = input().split(", ")

line = input()

while line != "Craft!":
    current_line = line.split(" - ")
    command = current_line[0]

    if command == "Collect":
        item = current_line[1]
        if item not in text:
            text.append(item)
        else:
            pass

    elif command == "Drop":
        item = current_line[1]
        if item in text:
            text.remove(item)
        else:
            pass
    elif command == "Combine Items":
        old_item = current_line[0]
        new_item = current_line[0]
        if old_item in text:
            text.insert(text.index(old_item), new_item)
            a = text.index(old_item)
            del text[a]
        else:
            pass

    elif command == "Renew":
        item = current_line[1]
        if item in text:
            if item in text:
                text.remove(item)
                text.append(item)
            else:
                pass

print(", ".join(text))
