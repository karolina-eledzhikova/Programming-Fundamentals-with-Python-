text = input().split(" ")

line = input()

while line != "Stop":
    current_line = line.split(" ")
    command = current_line[0]

    if command == "Delete":
        index = int(current_line[1])
        if index+1 < len(text)-1:
            del text[index+1]
        else:
            pass
    elif command == "Swap":
        word1 = (current_line[1])
        word2 = (current_line[2])
        if word1 and word2 in text:
            a = int(text.index(word1))
            b = int(text.index(word2))
            text[a], text[b] = text[b], text[a]

        else:
            pass

    elif command == "Put":
        word = current_line[1]
        index = int(current_line[2])
        if index-1 < len(text) and index-1 > 0:
            text.insert(index-1, word)
        else:
            pass

    elif command == "Sort":
        text.sort(reverse=True)

    elif command == "Replace":
        word1 = current_line[1]
        word2 = current_line[2]
        if word2 in text:
            text.insert(text.index(word2), word1)
            a = text.index(word2)
            del text[a]

        else:
            pass
    line = input()

print(" ".join(text))