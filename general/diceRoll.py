n = int(input())
dice = [x for x in input().split(" ")]
single = []
for i in range(len(dice)):
    rem = dice.pop(i)
    if rem not in dice:
        single.append(rem)
        dice.insert(i,rem)
    else:
        dice.insert(i,rem)
if (len(dice) == len(single)):
    print(0)
else:
    print(*single,sep=" ")
