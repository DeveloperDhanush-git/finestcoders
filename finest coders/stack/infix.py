from collections import deque
def operate(a,b,char):
   if char == '+':
       return a+b
   elif char == '-':
       return b-a
   elif char == '*':
       return a*b
   elif char == '/':
       return b/a
def postfixEvaluation(str):
   stack=deque()
   for char in str:
       if char.isdigit():
           stack.append(int(char))
       else:
           a=stack.pop()
           b=stack.pop()
           stack.append(operate(a,b,char))
   return stack.pop()

def precedence(char):
   if char == '+' or char == '-':
       return 1
   elif char == '*' or char == '/':
       return 2
   return 0


def InfixToPostfix(infix):
   stack=deque()
   postfix=""
   for char in infix:
       if char.isdigit():
           postfix+=char
       elif char=='(':
           stack.append(char)
       elif char==')':
           while stack and stack[-1]!='(':
               postfix+=stack.pop()
           stack.pop()
       else:
           while stack and precedence(stack[-1])>=precedence(char):
               postfix+=stack.pop()
           stack.append(char)
   while stack:
       postfix+=stack.pop()
   return postfix

str="5+3-(6*2)+9"

postfix=InfixToPostfix(str)
print(postfix)


result=postfixEvaluation(postfix)
print(result)






