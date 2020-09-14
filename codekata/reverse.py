n = int(input())

num = [x for x in input().split()]
output = ''
for i in range(n-1,-1,-1):
    if i == 0:
        output += num[i]
    else:
        output += num[i]
        output += '->'
print(output)
    
