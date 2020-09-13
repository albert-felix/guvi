string = input()
sList = []
cList = []

for s in string:
    count = 0
    if s not in cList:
        cList.append(s)
        for st in string:
            if s == st:
                count += 1
        sList.append({'char':s, 'count':count})
        
sortList = sorted(sList, key = lambda k: (k['count'], k['char']))
result = ""
for i in range(len(sortList)):
    for j in range(sortList[i]['count']):
        result += sortList[i]['char']
        
print(result)
