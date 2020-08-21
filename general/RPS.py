rps = [x for x in input().split()]

if (rps == ['R','P']):
    print('P')
elif (rps == ['R','S']):
    print('R')
elif (rps == ['P','S']):
    print('S')
else:
    print('D')
