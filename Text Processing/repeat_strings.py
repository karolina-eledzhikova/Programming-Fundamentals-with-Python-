word = input().split()
output = ""

for wd in word:
    output += wd * len(wd)

print(output)