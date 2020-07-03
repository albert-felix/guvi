n = int(input())
array = [x for x in input().split(" ")]

for i in range(0,len(array),2):
    if i != (len(array)-1):
        array[i],array[i+1] = array[i+1],array[i]
print(*array,sep=" ")
