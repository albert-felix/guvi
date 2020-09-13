a,b = map(int,input().split())

def factorial(x):
    fact = 1
    while x>1:
        fact = fact*x
        x -= 1
    print(fact)


factorial(min(a,b))
