def colect_func(data, item):
        if item not in data:
            data.append(item)

        return data


def drop_func(data, item):
    if item in data:
        data.remove(item)
    return data

def combine_func(data, items):
    items =




def inventory(data):

    while True:
        command = input().split("-")
        if command[0] == "Craft!":
            print(', '.join(data))
            break

        current_comand = command[0]
        items = command[1]

        if current_comand == "Collect":
            data = colect_func(data, item)
        elif current_comand == "Drop":
            data = drop_func(data, item)
        elif current_comand == "Combine Items":
            data = combine_func(data, item)
        elif current_comand == "Renew":
            data = renew_func(data, item)

info = input().split(", ")
inventory(info)