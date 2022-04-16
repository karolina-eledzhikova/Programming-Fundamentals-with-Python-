def electron_distribution(number):
    filled_chells = []
    counter = 1
    while True:
        element = 2 * (counter ** 2)

        if element < number:
            number -= element
            filled_chells.append(element)
        else:
            filled_chells.append(number)
            break
        counter += 1

    print(filled_chells)


data = int(input())
electron_distribution(data)



