n = int(input())
result = []
flag = True
if n >= 7:
    if (n%3==0):
        prime = n//3
        for j in range(2,n):
            if prime%j ==0:
                break
            else:
                flag = False
                result.append(prime)
                result.append(prime)
                result.append(prime)
                print(*result,sep=" ")
        
    elif flag:
        result = [2,3]
        for i in range(n):
            if sum(result) + i == n:
                result.append(i)
                break
        if len(result) == 3:
            print(*result,sep=" ")
        else:
            print(0)
else:
    print(0)
        
