num = input('Enter a number : ')
sum = 0
for i in num:
    fact = 1
    i = int(i)
    while i>0:
        fact *= i
        i -= 1
    sum += fact

if sum == int(num):
    print('It is a Strong Number')
else:
    print('It is not a Strong Number')
