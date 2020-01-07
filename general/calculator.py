def add(a,b):
    result = a+b
    return(result)

def sub(a,b):
    result = a-b
    return(result)

def multiply(a,b):
    result = a*b
    return(result)

def divide(a,b):
    while True :
        try:
            result = round(a/b,2)
        except ZeroDivisionError:
            print('Denominator cannot be zero for division')
            input_2()
            divide(input_1.value_1,input_2.value_2)
            break
        else:
            return(result)
            break

def mod(a,b):
    result = a%b
    return(result)

def option():
    print('1 -- ADD')
    print('2 -- SUBTRACT')
    print('3 -- MULTIPLY')
    print('4 -- DIVIDE')
    print('5 -- MOD')
    operator = int(input('Enter an option : '))
    operators = [1,2,3,4,5]
    while operator in operators:
        if operator == 1:
            print(add(input_1.value_1,input_2.value_2))
            break
        elif operator == 2:
            print(sub(input_1.value_1,input_2.value_2))
            break
        elif operator == 3:
            print(multiply(input_1.value_1,input_2.value_2))
            break
        elif operator == 4:
            print(divide(input_1.value_1,input_2.value_2))
            break
        elif operator == 5:
            print(mod(input_1.value_1,input_2.value_2))
            break
    else:
        print('Invalid Option')
        option()

def input_1():
    while True:
        try:
            input_1.value_1 = float(input('Enter number 1 :'))
        except ValueError:
            print('Invalid input')
            continue
        else:
            break

def input_2():
    while True:
        try:
            input_2.value_2 = float(input('Enter number 2 :'))
        except ValueError:
            print('Invalid input')
            continue
        else:
            break
input_1()
input_2()
option()
