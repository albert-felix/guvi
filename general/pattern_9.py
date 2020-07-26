n = int(input())

for i in range(1,n+1):
    if i == n:
        for k in range(n,0,-1):
            print('*'*k,end="")
            print()
    else:
        for j in range(i):
            print('*',end="")
        print()
