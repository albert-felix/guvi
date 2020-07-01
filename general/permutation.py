string = list(input())


def permute(string):
    if len(string) ==0:
        return []
        
    if len(string) == 1:
        return [string]
    
    result = []
    for i in range(len(string)):
        first = string[i]
        remaining = string[:i] + string[i+1:]
        for j in permute(remaining):
            result.append([first] + j)
        
    return result

for p in permute(string):
    print(*p,sep="")
