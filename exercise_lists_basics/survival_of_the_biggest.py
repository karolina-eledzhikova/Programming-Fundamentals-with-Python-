number = input().split(' ')
copy_nums = list(map(int, number))
n = int(input())

for _ in range(n):
    current_min_element = min(copy_nums)
    number.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(", ".join(number))