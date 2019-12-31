value_1 = int(input('Enter first number : '))    
value_2 = int(input('Enter second number : '))
i = 1

while True:
    lcm = value_1*i
    if lcm%value_2 == 0:
        print('LCM : ',end='')
        print(lcm)
        break
    i += 1
