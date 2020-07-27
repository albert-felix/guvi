n = int(input())

for i in range(1,n+1):
    if i == n:
        for k in range(1,i+1):
            print(k,end="")
    else:
        for j in range(1,i+1):
            if j == 1:
                print(j,end="")
            elif j == i:
                print(j,end="")
            else:
                print(" ",end="")
        print()
