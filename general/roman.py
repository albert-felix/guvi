roman = {'I':1,'V':5,'X':10,'L':50,'C':100}
string = input()
value = 0
for i in range(len(string)):
    if (i != (len(string) -1) ) :
        if (string[i] == 'I') and ((string[i+1] == 'V') or (string[i+1] == 'X') ):
            value -= 1
        elif (string[i] == 'I'):
            value += 1
        elif (string[i] == 'V'):
            value += 5
        elif (string[i] == 'X'):
            value += 10
        elif (string[i] == 'L'):
            value += 50
        elif (string[i] == 'C'):
            value += 100
    else:
        if (string[i] == 'I'):
            value += 1
        elif (string[i] == 'V'):
            value += 5
        elif (string[i] == 'X'):
            value += 10
        elif (string[i] == 'L'):
            value += 50
        elif (string[i] == 'C'):
            value += 100
if value==0:
    print(-1)
else:
    print(value)
