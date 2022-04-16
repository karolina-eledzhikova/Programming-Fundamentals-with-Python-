import re
info = input()
line = ""
for i in range(int(info)):
    info = input()
    pattern = r"([|])(?P<boss>[A-Z]+)\1:([#])(?P<title>[A-zA-z]+ [A-zA-Z]+)\3"
    result = re.findall(pattern, info)

    if result == []:
        print("Access denied!")
    else:
        for match in result:
            print(f"{match[1]}, The {match[3]}")
            print(f">> Strength: {len(match[1])}")
            print(f">> Armor: {len(match[3])}")
