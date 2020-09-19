n,k = map(int,input().split())
master_array = []
result = []
for i in range(n):
    branch_array = []
    branch_array = [x for x in input().split()]
    master_array.append(branch_array)

for j in master_array[0]:
    for k in range(0,n):
        if j not in master_array[k]:
            break
        elif k == n-1:
            result.append(j)
if (result):      
    print(*result,sep=" ")
else:
    print(-1)
