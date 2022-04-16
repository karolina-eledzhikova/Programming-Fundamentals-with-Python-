import math
num_of_people = int(input())
capacity = int(input())

course = 0

for i in range(1, num_of_people+1):
    result = num_of_people // capacity
    result_two = result * capacity
    course = math.ceil(num_of_people/capacity)
    if result_two <= capacity:
        result_three = num_of_people % capacity
        result_four = result_three * course
print(course)







