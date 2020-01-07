num = input('Enter a number : ')
length = len(str(num))
sum_num = 0

for i in num:
    sum_num += int(i)**length

if sum_num == int(num):
    print('It is an armstrong number')

else:
    print('It is not an armstorng number')
