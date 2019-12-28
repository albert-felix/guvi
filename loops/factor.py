n = int(input())
factors=[]
for i in range(1,(int(n/2)+1)):
    if n%i==0:
        factors.append(i)
factors.append(n)
print (factors)
