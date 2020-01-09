stack = []
stack_temp = []

def pop(x):
    if len(stack) > 1:
        while len(stack) != 0:
            stack_temp.append(stack.pop())
        first = stack_temp.pop()
        while len(stack_temp) != 0:
            stack.append(stack_temp.pop())
        return first
    else:
        first = stack.pop()
        return first


stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
print(pop(stack))



