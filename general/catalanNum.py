n = int(input())
result = []
def factorial(num):
    fact = 1
    while num>0:
        fact *= num
        num -= 1
    return fact

def catalan(num):
    cat = (factorial(2*num))/((factorial(num+1))*(factorial(num)))
    return int(cat)
    
for i in range(n+1):
    result.append(catalan(i))
    
print(*result,sep=" ")
