def list_func(index, list):
    add_num = list[index] # 0 4 3 1
    list[index] = -1
    for i in range(len(list)):
        if list[i] == -1:
            continue

        if add_num < list[i]:
            list[i] -= abs(add_num)
        else:
            list[i] += add_num


numbers = input().split(" ")
numbers = list(map(int, numbers))

line = input()
while line != "End":
    index = int(line)
    if index > len(numbers) - 1:
        pass
    else:
        list_func(index, numbers)

    line = input()

counter = 0

for i in range(len(numbers)):
    if numbers[i] == -1:
        counter += 1

numbers = list(map(str, numbers))
output = " ".join(numbers)
print(f"Shot targets: {counter} -> " + output)

