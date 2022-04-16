text = input()
digits = ""
letters = ""
symbols = ""

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isupper() or ch.islower():
        letters += ch
    else:
        symbols += ch

print(digits)
print(letters)
print(symbols)