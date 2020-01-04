number = int(input('Enter n value : '))
factors = []

if number%2 == 0:
    factors.append(2)
    
for i in range(3,int(number/2)+1,2):
    if number%i == 0:
        if len(factors) == 0:
            factors.append(i)
        else:
            for j in factors:
                if i%j == 0:
                    break
            else:
                factors.append(i)

if number%2 != 0:
    factors.append(number)
print(factors)
