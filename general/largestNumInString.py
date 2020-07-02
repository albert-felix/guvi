string = input()
digits = ""

for i in string:
    if (i.isdigit()):
        digits += i
    elif (i == " "):
        digits += " "

result = digits.split()
result = [int(x) for x in result]
print(max(result))
