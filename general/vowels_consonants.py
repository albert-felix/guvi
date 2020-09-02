string = input()
count = 0
result = []
for i in range(len(string)):
    if string[i].lower() in ['a','e','i','o','u']:
        count += 1
        result.insert(count-1,string[i])
    else:
        result.append(string[i])
print(*result,sep="")
