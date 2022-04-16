def miner_task():
    items_dict = dict()

    while True:
        response = input()
        if response == "stop":
            break

        quantity = int(input())

        if response not in items_dict:
            items_dict[response] = quantity
        else:
            items_dict[response] += quantity
    for key, value in items_dict.items():
        print(f"{key} -> {value}")

miner_task()