my_dict = {}
word = input()

for ch in word:
    if ch not in my_dict:
        my_dict[ch] = 1
    else:
        my_dict[ch] += 1

for key, value in my_dict.items():
    if key != " ":
        print(f"{key} -> {value}")
