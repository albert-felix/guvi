n = int(input())
numbers = [int(x) for x in input().split()]
sum = 0

for i in numbers:
    sum += i

if ((sum %2 == 0) and (sum%3 == 0) and (sum%5 == 0)):
    print(1)
else:
    print(0)
