a,b = input().split()
flag = True
if len(a) > len(b):
    test_1 = a
    test_2 = b
else:
     test_1 = b
     test_2 = a
     
for char in test_1:
    if char in test_2:
        continue
    else:
        flag = False
        break
    
if flag:
    print('true')
else:
    print('false')
