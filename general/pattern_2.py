n = int(input())
x = 1
for i in range(1,n+1):
    for j in range(x,x+i):
        if j == x+i-1:
            print(j,end="")
        else:
            print(j,end=" ")
    x = j+1
    print()
