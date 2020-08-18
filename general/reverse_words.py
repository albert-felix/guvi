string = input()
result = string.split()

for i in range(len(result)-1, -1, -1):
    if i == 0:
        print(result[i])
    else:
        print(result[i],end=" ")
