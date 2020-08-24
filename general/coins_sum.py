n,s = map(int,input().split())
c = [int(x) for x in input().split()]
coins = sorted(c, reverse=True)
flag = True

for i in range(len(coins)):
    if not flag:
        break
    j = 1
    while True:
        if coins[i]*j == s:
            flag = False
            break
        elif coins[i]*j > s:
            rem = s % (coins[i]*(j-1))
            if rem in coins:
                flag = False
                break
        j +=1
        
if j!=1:
    print(j)
else:
    print(-1)
