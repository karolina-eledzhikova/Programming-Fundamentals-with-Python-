import re

text = input()
expresion = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"

matches = re.finditer(expresion, text)

output = list()
for mach in matches:
    output.append(mach.group())
print(" ".join(output))
