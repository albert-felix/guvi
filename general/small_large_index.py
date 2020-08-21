n = int(input())

numbers = [int(x) for x in input().split()]
small = numbers[0]
large = numbers[0]

for num in numbers:
    if num < small:
        small = num
    if num > large:
        large = num


print(numbers.index(small)+1,end=" ")
print(numbers.index(large)+1)

