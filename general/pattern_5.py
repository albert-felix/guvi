n = int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        if j == 1:
            print('*', end="")
        else:
            print('*', end="  ")
    print()
