x,y = map(int,input().split())
x = abs(x)
y = abs(y)

if x>y:
    smaller = y
else:
    smaller = x

result = 0

for i in range(1,smaller+1):
    if (x%i ==0 and y%i ==0):
        result = i
        
if result == 0:
    print(-1)
else:
    print(result)
