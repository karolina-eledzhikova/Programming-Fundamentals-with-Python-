count = int(input())
herous = dict()

for i in range(count):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hero_HP = int(current_hero[1])
    hero_MP = int(current_hero[2])

    current_hero_dict = dict()
    current_hero_dict["HP"] = hero_HP
    current_hero_dict["MP"] = hero_MP
    herous[hero_name] = current_hero_dict

    # herous[hero_name]["HP"] = hero_HP
    # herous[hero_name]["MP"] = hero_MP

command = input()
while command != "End":
    command_params = command.split(" - ")
    command_name = command_params[0]
    hero_name = command_params[1]
    value = int(command_params[2])

    if command_name == "Heal":
        if herous[hero_name]["HP"] + value > 100:
            value = 100 - herous[hero_name]["HP"]
            herous[hero_name]["HP"] = 100
        else:
            herous[hero_name]["HP"] += value
        print(f"{hero_name} healed for {value} HP!")

    elif command_name == "Recharge":
        if herous[hero_name]["MP"] + value > 200:
            value = 200 - herous[hero_name]["HP"]
            herous[hero_name]["MP"] = 100
        else:
            herous[hero_name]["HP"] += value
        print(f"{hero_name} recharged for {value} MP!")

    elif command_name == "TakeDamage":
        attacker = command_params[3]
        herous[hero_name]["HP"] -= value
        if herous[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {value} HP by {attacker} and now has {herous[hero_name]['HP']} HP left!")
        else:
            herous.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command_name == "CastSpell":
        spell = command_params[3]
        if herous[hero_name]["MP"] >= value:
            herous[hero_name]["MP"] -= value
            print(f"{hero_name} has successfully cast {spell} and now has {herous[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")

    command = input()
for hero in herous:
    print(f"{hero}")
    print(f"  HP: {herous[hero]['HP']}")
    print(f"  MP: {herous[hero]['MP']}")
