string = [x for x in input().split(" ")]
s = input()
count = 0
for i in string:
    if i == s:
        count += 1
if count == 0:
    print(-1)
else:
    print(count)
