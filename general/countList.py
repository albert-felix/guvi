n,k = map(int,input().split(" "))
elements = [int(x) for x in input().split(" ")]
count = -1

for i in elements:
    if i == k:
        count += 1
print(count)
