def password_func(word):
    if not 6 <= len(word) <= 10:
        print("Password must be between 6 and 10 characters")

    if not word.isalnum():
        print("Password must consist only of letters and digits")

    # if word.isalnum() and sum(map(lambda x: x.isdigit(), word)) :
    #
    #     print("Password must have at least 2 digits")

    if sum(map(lambda x: x.isdigit(), word)) < 2:
        print("Password must have at least 2 digits")

    if word.isalnum() and sum(map(lambda x: x.isdigit(), word)) > 2 and sum(map(lambda x: x.isalpha(), word)):
        print("Password is valid")


password = input()
password_func(password)
