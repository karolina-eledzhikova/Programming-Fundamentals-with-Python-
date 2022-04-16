def reverse(word):
    return word[::-1]


import re

info = input()
pattern = r"([@|#])(?P<duma1>[A-zA-z]{3,})\1{2}(?P<duma2>[A-zA-z]{3,})\1"
result = re.findall(pattern, info)
items = []
count_words = len(result)


for match in result:
    duma1 = match[1]
    duma2 = match[2]

    if reverse(duma1) == duma2:
        items.append(duma1 + " <=> " + duma2)

if count_words > 0:
    print(f"{count_words} word pairs found!")
else:
    print("No word pairs found!")


if len(items) > 0:
    print("The mirror words are:")
    print(", ".join(items))
else:
    print("No mirror words!")