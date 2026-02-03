from collections import deque

def operate(a,b,i):
    if i == "+":
        return a+b
    elif i == "-":
        return b-a
    elif i=="*":
        return a*b
    else:
        return b/a
    
def PrefixEvaluation(str):
    stack = deque()
    for i in str:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(operate(a,b,i))
    return stack.pop()
str = "-3+*4+215"
str = str[ : :-1]
result = PrefixEvaluation(str)
print(result)


    