number = int(input())

p1_pr = 0
p2_pr = 0
p3_pr = 0
p4_pr = 0
p5_pr = 0

cnt_p1 = 0
cnt_p2 = 0
cnt_p3 = 0
cnt_p4 = 0
cnt_p5 = 0

for i in range(number):
    current_number = int(input())

    if current_number < 200:
        cnt_p1 += 1
    elif 200 <= current_number <= 399:
        cnt_p2 += 1
    elif 400 <= current_number <= 599:
        cnt_p3 += 1
    elif 600 <= current_number <= 799:
        cnt_p4 += 1
    else:
        cnt_p5 += 1

p1_pr = cnt_p1 * 100 / number
p2_pr = cnt_p2 * 100 / number
p3_pr = cnt_p3 * 100 / number
p4_pr = cnt_p4 * 100 / number
p5_pr = cnt_p5 * 100 / number

print(f"{p1_pr:.2f}")
print(f"{p2_pr:.2f}")
print(f"{p3_pr:.2f}")
print(f"{p4_pr:.2f}")
print(f"{p5_pr:.2f}")