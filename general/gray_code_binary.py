// Binary base gray code

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

// No base gray code

n = int(input())

result = ['0', '1']

if n > 1:
    for i in range(n-1):
        for j in result[::-1]:
            result.append(j)
    
    for k in range(0,int(len(result)/2)):
        result[k] = "0" + result[k]
    
    for l in range(int(len(result)/2), len(result)):
        result[l] = "1" + result[l]

print(*result, sep=" ")
