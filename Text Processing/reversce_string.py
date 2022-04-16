# text = input()
#
# while text != "end":
#     rev = reversed(text)
#     for ch in rev:
#         print(ch, end="")
#
#     text = input()
#####################################
text = input()

while text != "end":
    rev = reversed(text)
    reversed_text = "".join(rev)
    print(f"{text} = {reversed_text}")

    text = input()
