n = int(input())

num = [int(x) for x in input().split(" ")]
result = 0
for i in range(len(num)-1):
    if i == 0:
        result = num[i]
    else:
        if num[i] < num[i+1]:
            result = num[i]
print(result)
        
