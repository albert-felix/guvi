string = list(input())

for i in range(0,len(string),2):
    string[i], string[i+1] = string [i+1], string[i]
print(*string,sep="")
