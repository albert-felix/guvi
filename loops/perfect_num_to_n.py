num = int(input('Enter n value : '))
print('Perfect Numbers')
for i in range(1,num+1):
    factors = []
    for j in range(1,int(i/2)+1):
        if i%j == 0:
            factors.append(j)
    if sum(factors) == i:
        print(i)
