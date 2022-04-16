def sum_func(first_word, secont_word):
    total_sum = 0
    for i in range(len(first_word)):
        if i < len(secont_word):
            total_sum += ord(first_word[i]) * ord(secont_word[i])
        else:
            total_sum += ord(first_word[i])
    return total_sum


def char_multiplair(first_word, secont_word):
    result =0

    if len(first_word) > len(secont_word):
        result = sum_func(first_word, secont_word)
    else:
        result = sum_func(secont_word, first_word)
    print(result)


data = input().split(" ")
char_multiplair(data[0], data[1])