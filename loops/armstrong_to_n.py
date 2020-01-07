num = int(input('Enter n value : '))
print('Armstrong Numbers')
for i in range(num+1):
    temp = str(i)
    length = len(temp)
    sum_num = 0
    for j in temp:
        sum_num += int(j)**length

    if sum_num == i:
        print(i)
