string_1 = input()
string_2 = input()

if string_1.isalpha() and string_2.isalpha():
    for s in string_2:
        if s in list(string_1):
            print('no')
            break
    else:
        print('yes')

else:
    print('no')
