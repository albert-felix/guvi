string = input()
string_list = list(string.split())
check = list(string)
repeat = []
result = []
for p in range(len(check)):
    temp = check.pop(p)
    if temp in check:
        if temp not in repeat:
            repeat.append(temp)
            check.insert(p,temp)
        else:
            check.insert(p,temp)
    else:
        check.insert(p,temp)

for i in range(len(string_list)):
    word = ''
    for j in range(len(string_list[i])):
        if string_list[i][j] in repeat:
            word += string_list[i][j].upper()
        else:
            word += string_list[i][j]
    result.append(word)

print(*result,sep=" ")
    
