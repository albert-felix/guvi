num = int(input('Enter the number : '))
factors = []
for i in range(1,int(num/2)+1):
    if num%i == 0:
        factors.append(i)
if sum(factors) == num:
    print('It is a perfect number')
else:
    print('It is not a perfect number')
