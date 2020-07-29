x,y = map(int,input().split(" "))

for i in range(x):
    for j in range(y):
        if j == y-1:
            print('*')
        else:
            print('* ',end="")
        
