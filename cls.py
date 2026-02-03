# class laptop:
#     name = ""
#     price = 0
#     proc = ""

# dell = laptop()
# hp = laptop()

# dell.name = "dell"
# dell.price = 2000
# dell.proc = "ckldk"


# hp.name = "hp"
# hp.price = 3000
# hp.proc = "hbjb"

# print(dell.name)
# print(dell.price)
# print(dell.proc)
# print(hp.name)
# print(hp.price)
# print(hp.proc)

# class goa:
#     name = "rehdfhgrh"
#     drink = ""
#     def party(self):
#         print("party in goa")
#     def beach(self):
#         print("beach in goa")
        
# ramesh = goa()
# suresh = goa()

# ramesh.name = "ramesh"
# suresh.name = "suresh"

# print(ramesh.name)
# print(suresh.name)

# class numfunction:
#     def add(self, a, b):
#         return a + b
    
#     def sub(self, a, b):
#         return a - b
    
#     def mul(self, a, b):
#         return a * b
    
#     def div(self, a, b):
#         return a / b
    
# num = numfunction()
# print(num.add(10, 20))
# print(num.sub(10, 20))
# print(num.mul(10, 20))
# print(num.div(10, 20))

# class laptop:
#     def __init__ (self):
#         print("constructor called")
#     def display(self):
#         print("display function called")
        
# dell = laptop()
# dell.display()


# class student:
#     def __init__ (self):
#         self.name = "wsdcfvb"
#         self.reg = "123"
#     def display(self):
#         print(self.name)
#         print(self.reg)
        
# s1 = student()
# s1.name = "dedhjc"
# s1.reg = "1"
# s1.display()

# class fruit:
#     def __init__(self, col):
#         self.color = col

# apple = fruit("red")

# print(apple.color)
        
        
# class teacher:
#     def __init__ (self,name,regno):
#         self.name = name
#         self.regno = regno
#     def display(self):
#         print(self.name)
#         print(self.regno)
        
# t1 = teacher("log","2")
# t2 = teacher("cow","3")


# t1.display()
# t2.display()

# class calc():
#     def __init__(self,a,b):
#         self.num1 = a
#         self.num2 = b
#     def add(self):
#         print(self.num1+self.num2)
        
# kut = calc(2,4)
# kut.add()

# class calc():
#     def add(self,num1,num2):
#         print(num1 + num2)
        
# kut = calc()
# kut.add(2,4)

# def studentGrade(marks):
#     if(marks>=90):
#         return "Grade A"
#     elif(marks>=70):
#         return "Grade B"
#     elif(marks>=50):
#         return "Grade C"
#     elif(marks>=35):
#         return "Grade D"
#     else:
#         return "Fail"
    
# marks = int(input())
# print(studentGrade(marks))

# def weekday(num):
#     match num:
#         case 1:
#             return "Monday"
#         case 2:
#             return "Tuesday"
#         case 3:
#             return "Wednesday"
#         case 4:
#             return "Thursday"
#         case 5:
#             return "Friday"
#         case 6:
#             return "Saturday"
#         case 7:
#             return "Sunday"
#         case default:
#             return "Invalid"
# num = int(input())
# print(weekday(num))


# N = int(input())
# listval = []

# for i in range(N):
#     action = input().strip().split()
    
#     if action[0] == "insert":
#         pos = int(action[1])
#         val = int(action[2])
#         listval.insert(pos, val)
#     elif action[0] == "print":
#         print(listval)
#     elif action[0] == "remove":
#         val = int(action[1])
#         listval.remove(val)
#     elif action[0] == "append":
#         val = int(action[1])
#         listval.append(val)
#     elif action[0] == "sort":
#         listval.sort()
#     elif action[0] == "pop":
#         listval.pop()
#     elif action[0] == "reverse":
#         listval.reverse()
