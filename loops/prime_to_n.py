num = int(input('Enter n value : '))
print('The prime numbers are : ')
for i in range(2,num+1):
	for j in range(2,int((i/2)+1)):
		if i%j == 0:
			break
	else:
		print(i)