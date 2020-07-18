n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        if j == i-1:
            print(1)
        else:
            print(1,end=" ")
