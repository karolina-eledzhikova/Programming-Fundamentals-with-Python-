numbers = input().split(" ")
numbers = list(map(int, numbers))

numbers_sum = sum(numbers)
average_number = numbers_sum//len(numbers)
list_to_be_printed = []

for i in numbers:
    if i > average_number:
        list_to_be_printed.append(i)
        list_to_be_printed.sort(reverse=True)

if len(list_to_be_printed) == 0:
    print("No")
else:
    print(*list_to_be_printed[:5])

