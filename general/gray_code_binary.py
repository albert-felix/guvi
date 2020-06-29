n = int(input())
bit = ''

for i in range(n):
    bit += "0";

result = [bit]
for j in range((2**n) -1):
    temp = list(result[len(result)-1])
    for k in range((len(temp)-1), -1,-1):
        if temp[k] == '0':
            temp.pop(k)
            temp.insert(k,'1')
            break
        elif temp[k] == '1':
            temp.pop(k)
            temp.insert(k,'0')
    result.append("".join(temp))

print(*result, sep=" ")
