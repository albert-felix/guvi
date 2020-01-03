num = int(input('Enter n value : '))
sum = 0
for i in range(2,num+1):
	for j in range(2,int((i/2)+1)):
		if i%j == 0:
			break
	else:
		sum += i
print('Sum of prime numbers : ',end='')
print(sum)