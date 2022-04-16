current_people = int(input())
lift = input().split(" ")
lift = list(map(int, lift))

for i in range(len(lift)):
    can_load = min(4 - lift[i], current_people)
    lift[i] += can_load
    current_people -= can_load

if current_people > 0:
    print(f"There isn't enough space! {current_people} people in a queue!")
elif len([cart for cart in lift if cart < 4]) > 0:
    print("The lift has empty spots!")

lift = list(map(str, lift))
output = " ".join(lift)
print(output)




