string,n = input().split()
string_2 = list(string)
n = int(n)
if n == 0:
    print(string)
else:
    for i in range(-1,len(string_2),n):
        string_2[i] = string_2[i].upper()
    print(*string_2,sep="")
