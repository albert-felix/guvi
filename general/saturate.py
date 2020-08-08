number = list(input())
check = []

for i in range(len(number)):
    if i == 0:
        check.append(number[i])
    else:
        if number[i] not in check:
            check.append(number[i])

if len(check) == 2:
    print('Saturated')
else:
    print('Unsaturated')
