string = input()
result = ''
count = 0

for i in string:
    if (i.isdigit()):
        count += int(i)
    else:
        result += i
result += str(count)
print(result)
