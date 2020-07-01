string = [x for x in input().split(" ")]

def sort(array):
    for i in range(len(array) -1):
        for j in range(len(array[i])):
            if (ord(array[i][j]) <= ord(array[i+1][j])  ):
                break
            elif (ord(array[i][j]) > ord(array[i+1][j]) ):
                array[i],array[i+1] = array[i+1], array[i]
                sort(array)
                break

sort(string)
print(*string, sep=" ")
