n = int(input())
numbers = [x for x in input().split()]

count_final = 0
result = numbers[0]

for i in numbers:
    count = 0
    for j in range(len(numbers)):
        if i == numbers[j]:
            count += 1
    if count > count_final:
        count_final = count
        result = i
    
print(result)
