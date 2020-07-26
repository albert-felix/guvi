n = int(input())

for i in range(1,n+1):
    for j in range(1,(2*n)):
        if (j>(n-i) and j<(n+i)):
            print('*',end="")
        else:
            print('b',end="")
    print()
