n = int(input())
num = [int(x) for x in input().split(" ")]
rep ={}

for i in range(len(num)):
    count = 1
    temp = num.pop(i)
    for j in num:
        if temp == j:
            count += 1
    num.insert(i,temp)
    rep[num[i]] = count
    
sort = {a:b for a,b in sorted(rep.items(), key=lambda item: item[1])}
value = []
for k in sort:
    value.append(k)

for i in range(len(value)-1):
    if sort[value[i]] == sort[value[i+1]]:
        if value[i] > value[i+1]:
            value[i],value[i+1] = value[i+1], value[i]
print(*value,sep=" ")
