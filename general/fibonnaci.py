num = int(input('Enter n value : '))
if num>0:
	print(1)
	series = [1]
	first = 0
	second = 1
	for i in range(0,num-1):
		fib = first + second
		series.append(fib)
		print(fib)
		first = second
		second = fib

	print(series)