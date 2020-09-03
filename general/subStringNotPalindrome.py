string = input()

if string != string[::-1]:
    print(string)
else:
    str_list = list(string)
    for i in range(len(string)):
        temp = ""
        str_list.pop()
        if temp.join(str_list) != temp.join(str_list)[::-1]:
            print(temp.join(str_list))
            break
