# number = input().split(" ")
# number = list(map(int, number))
#
# line = input()
#
# while line != "end":
#     if line == "decrease":
#         number = list(map(lambda n: n-1, number))
#     else:
#         explode = line.split(" ")
#         command = explode[0]
#         index1 = int(explode[1])
#         index2 = int(explode[2])
#
#         if command == "swap":
#             number[index1], number[index2] = number[index2], number[index1]
#         elif command == "multiply":
#             number[index1] = number[index1] * number[index2]
#
#     line = input()
#
# number = list(map(str, number))
# output = ", ".join(number)
# print(output)
#




numbers = input().split(" ")
# на всяко от елементите в този списък ми ги направи числа, а с лист ми го конвертира обратно в лист
numbers = list(map(int, numbers))

line = input()


while line != "end":

    if line == "decrease":
        numbers = list(map(lambda n: n-1, numbers))
    else:
        explode = line.split(" ")
        command = explode[0]
        index1 = int(explode[1])
        index2 = int(explode[2])

        if command == "swap":
            numbers[index1] , numbers[index2] = numbers[index2] , numbers[index1]
        elif command == "multiply":
            numbers[index1] = numbers[index1] * numbers[index2]

    line = input()

numbers = list(map(str, numbers))
output = ", ".join(numbers)
print(output)

