a = int(input())    
b = int(input())
i = 1

while a>0 and b>0:
    lcm = a*i
    if lcm%b == 0:
        print(lcm)
        break
    i += 1
