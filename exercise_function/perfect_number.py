con = False


def perfect_number(num):
    if num == perfect_number(num):
        a = 2 ** (num - 1)
        b = (2 ** num) - 1
        return a * b
    print("We have a perfect number!")
    con = True


if con:
    print("It's not so perfect.")


number = int(input())
(perfect_number(number))
