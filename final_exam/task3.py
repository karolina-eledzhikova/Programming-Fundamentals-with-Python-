capacyty = int(input())
message = input()
mes_dict = dict()

while message != "Statistics":
    current_message = message.split("=")

    if current_message[0] == "Add":
        username = current_message[1]
        sent = int(current_message[2])
        received = int(current_message[3])
        if username not in mes_dict.keys():
            mes_dict[username] = [sent, received]

    elif current_message[0] == "Message":
        sender = current_message[1]
        receiver = current_message[2]
        if sender in mes_dict.keys() and receiver in mes_dict.keys():
            mes_dict[sender][0] += 1
            mes_dict[receiver][1] += 1
            if mes_dict[sender][0] >= capacyty:
                del mes_dict[sender]
                print(f"{sender} reached the capacity!")
            if mes_dict[receiver][1] >= capacyty:
                del mes_dict[receiver]
                print(f"{receiver} reached the capacity!")

    elif current_message[0] == "Empty":
        username = current_message[1]
        if username in mes_dict.keys():
            del mes_dict[username]
        elif username == "All":
            mes_dict = {}
    message = input()

print(f"Users count: {len(mes_dict)}")
for data in mes_dict:
    total_number = data
    sender = int(mes_dict[data][0])
    receiver = int(mes_dict[data][1])
    total_sum = sender+receiver
    print(f"{total_number} - {total_sum}")