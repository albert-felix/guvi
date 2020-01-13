def comp():
    num = list(input('Enter binary number : '))
    for i in range(len(num)):
        if num[i] == '0':
            num[i] = '1'
        else:
            num[i] = '0'
    print("One's complement : ",end='')
    print(*num,sep='')

    for j in range(len(num)-1,-1,-1):
        if num[j] == '0':
            num[j] = '1'
            break
        else:
            num[j] = '0'
            if j == 0:
                num.insert(0,'1')
    print("Two's complement : ",end='')
    print(*num,sep='')


comp()
