text = input().split("|")
health = 100
bitcoins = 0
have_made_it = True

for command in range(len(text)):
    current_command = text[command].split(" ")
    type = current_command[0]

    number = int(current_command[1])
    sum = 0
    if type == "potion":
        sum = health + number
        if sum >= 100:
            a = 100 - health
            health += a
            print(f"You healed for {a} hp.")
        else:
            health = sum
            print(f"You healed for {number} hp.")

        print(f"Current health: {health} hp.")

    elif type == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {type}.")
        else:
            print(f"You died! Killed by {type}.")
            print(f"Best room: {command+1}")
            have_made_it = False
            break
if have_made_it:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")