number = int(input())

for n in range(1, number+1):

    working_number = n
    digit_sum = 0

    while working_number > 0:
        digit_sum += working_number % 10
        working_number = int(working_number/10)

    is_spacial = digit_sum == 5 or digit_sum == 7 or digit_sum == 11

    print(f"{n} -> {is_spacial}")
