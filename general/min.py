num = [int(x) for x in input().split(" ")]
result = 0
for i in range(len(num)):
    if i == 0:
        result = num[i]
    else:
        if num[i] < result:
            result = num[i]
print(result)
