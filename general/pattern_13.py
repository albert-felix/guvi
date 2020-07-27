n = int(input())
x = (n//2) +1
for i in range(1,n+1):
    if i <= x:
        for j in range(1,n+1):
            if (j > (x-i) and j < (x+i)):
                print('*',end="")
            else:
                print('b',end="")
        print()
    else:
        for j in range(1,n+1):
            if (j > (x-(n+1-i)) and j < (x+(n+1-i))):
                print('*',end="")
            else:
                print('b',end="")
        print()
