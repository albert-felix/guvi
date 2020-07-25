n = int(input())

global state
state = False

def changeState():
    global state
    state = not state

for i in range(1,n+1):
    changeState()
    if i == n:
        for m in range(1,i+1):
            if m == i:
                print(m)
            else:
                print(m,end=" ")
    else:
        
        for j in range(1,i+1):
            if j == 1:
                for k in range(n-i):
                    print(" ",end="")
                print(1,end="")
            elif j == i:
                print(" " + str(j),end="")
            elif i > 2:
                if state == True:
                    for l in range(((i-2) * 2)):
                        print(" ",end="")
                    changeState()
        print()
