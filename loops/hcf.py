a = int(input('Enter first number : '))    
b = int(input('Enter second number: '))
fact_a = []
fact_b = []

for x in range(1,int((a/2)+1)):
    if a%x==0:
        fact_a.append(x)
fact_a.append(a)
print('Factors : ',end='')
print(fact_a)

for y in range(1,int((b/2)+1)):
    if b%y==0:
        fact_b.append(y)

fact_b.append(b)
print('Factors : ',end='')
print(fact_b)

for i in fact_a[::-1]:
    if i in fact_b:
        print('HCF : ',end='')
        print(i)
        break
    
