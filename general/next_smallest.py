n = int(input())
array = [int(x) for x in input().split(" ")]
result = []
for i in range(len(array)):
    if i == (len(array) -1):
        result.append(-1)
    else:
        for j in range((i+1), len(array)):
            if array[j] < array[i]:
                result.append(array[j])
                break
        else:
            result.append(-1)

print(*result, sep=" ")
