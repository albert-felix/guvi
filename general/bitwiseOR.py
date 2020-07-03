n = input()
num = [int(x) for x in input().split(" ")]
result = ''
for i in range(len(num)):
    if i == len(num) -1:
        result += str(num[i])
    else:
        result += str(num[i])+"|"
print(eval(result))

