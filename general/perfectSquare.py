n,m = map(int,input().split(" "))
sq = (n*m)**(1/2)

if (sq == int(sq)):
    print('yes')
else:
    print('no')
