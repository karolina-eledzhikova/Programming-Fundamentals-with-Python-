# vowels = ["a", "o", "u", "e", "i"]
# text = input()
#
# no_vowels = list()
#
# for ch in text:
#     if ch not in vowels:
#         no_vowels.append(ch)
#
# print("".join(no_vowels))

# LIST COMPREHENTION
vowels = ["a", "o", "u", "e", "i"]
text = input()

no_vowels = [ch for ch in text if ch not in vowels]
print("".join(no_vowels))