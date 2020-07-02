string = list(input())
newString = ""

for i in range(len(string)):
    temp = string.pop(i)
    if temp not in string:
        newString += temp
        string.insert(i,temp)
    else:
        string.insert(i,temp)

print(newString)
