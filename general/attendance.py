n = int(input())
attendance = [x for x in input().split(" ")]
p = 0
for i in attendance:
    if i == 'P':
        p += 1
if ((p/n) <= 0.25) :
    print("Blacklisted")
else:
    print("Not Blacklisted")
