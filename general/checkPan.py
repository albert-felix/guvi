string = list(input())
flag = True
if len(string) == 10:
    for i in range(len(string)):
        if (i <5 or i == len(string)-1):
            if (string[i].isdigit()):
                flag = False
                break
            if (string[i].islower()):
                flag = False
                break
        elif (i >4 and i< (len(string)-1)):
            if not (string[i].isdigit()):
                flag = False
                break
            if (string[i].isdigit()):
                if i == 0:
                    flag = False
                    break
    if(flag):
        print('pan')
    else:
        print('not pan')
else:
    print('not pan')

