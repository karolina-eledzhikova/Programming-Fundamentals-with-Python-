def office_management(number_of_ruums):
    left_chairs = 0
    condiiton = True

    for room_number in range(1, number_of_ruums +1 ):
        data = input().split(" ")
        avanable_chairs = data[0]
        visitor = int(data[1])

        diff = abs(len(avanable_chairs) - visitor)

        if len(avanable_chairs) < visitor:
            condiiton = False
            print(f"{diff} more chairs needed in room {room_number}")

        elif len(avanable_chairs) > visitor:
            left_chairs += diff

    if condiiton:
        print(f"Game On, {left_chairs} free chairs left")


info = int(input())
office_management(info)