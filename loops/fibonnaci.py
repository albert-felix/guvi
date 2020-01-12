num = int(input('Enter n value : '))
if num>0:
	print(1)
	first = 0
	second = 1
	for i in range(0,num-1):
		fib = first + second
		print(fib)
		first = second
		second = fib
