n = int(input())
x = n
binary = []
decimal = 0
while x > 1:
    y = x % 2
    binary.insert(0,y)
    x = int(x / 2)
binary.insert(0,x)

for b in range((len(binary)-1),-1,-1):
    if binary[b] == 1:
        binary[b] = 0
    elif binary[b] == 0:
        binary[b] = 1
        break
    else:
        binary.append(1)

for i in range(len(binary)-1,-1,-1):
    decimal += binary[i]*(2**((len(binary)-1) -i))
print(-decimal)
