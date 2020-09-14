n = int(input())
sList = []
for i in range(n):
    sList.append(input())
flag = 1
for j in sList:
    if ('a' or 'e' or 'i' or 'o' or 'u') in j:
        continue
    else:
        flag = 0
        break
    
if flag:
    print('yes')
else:
    print('no')
