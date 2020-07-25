n = int(input())
global state 
state = False
def changeState():
    global state
    state = not state

for i in range(n,0,-1):
    changeState()
    if state == True:
        for j in range(1,i+1):
            print(j,end="")
    elif state == False:
        for k in range(i,0,-1):
            print(k,end="")
    print()
