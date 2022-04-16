number = int(input())

positive = list()
negative = list()
odd = list()
even = list()

for i in range(number):
    current = int(input())
    if current % 2 == 0:
        even.append(current)
    else:
        odd.append(current)
    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)

filter_word = input()

print(eval(filter_word))

# тоест той казва отпечатай ми този списък,
# който е с името на променлива като стринга който съм задал

# ###################################### ТОВА Е ДРУГИЯ НАЧИН
# ################################################################

# if filter_word == "even":
#     print(even)
# if filter_word == "odd":
#     print(odd)
# if filter_word == "positive":
#     print(positive)
# if filter_word == "negative":
#     print(negative)
