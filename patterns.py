# for  i in range(1, 11):
#     print(i , " x 2 = ", i*2)
    
# a = int(input())
# b = int(input())

# for i in range(a+1,b):
#     print(i)

# count = 0
# for i in range(1, 11):
#     if(i%2 == 0):
#         count+=1
        
# print(count)

# natural numbers 1,2,3... strat from 1 to infinity


# sum = 0
# for i in range (0, 5):
#    a = int(input())
#    sum = sum + a
# print(sum)

# a =[]
# sum = 0
# for i in range(1,6):
#     a.append(i)
#     sum = sum + i
# print(a)
# print(sum)


# pattern
# n = 7
# for i in range(0,n):
#     print()
#     for j in range(0,n-i):
#         print("* ", end="")
        
# n=4
# for i in range(1,n+1):
#     for j in range(i):
#         print("* ", end="")        
#     print()

# pyramid 
# n = 4
# for i in range(1,n+1):
#     for sp in range(1,n-i+1):
#         print(" ",end='')
#     for j in range(1,2*i):
#         print("*",end='')
#     print()

# diamond pattern
# n = 4
# for i in range(1,n+1):
#     for sp in range(1,n-i+1):
#         print(" ",end='')
#     for j in range(1,2*i):
#         print("*",end='')
#     print()
# for i in range(n-1,0,-1):
#     for sp in range(1,n-i+1):
#         print(" ",end='')
#     for j in range(1,2*i):
#         print("*",end='')
#     print()


# n = 4
# for i in range(1,n+1):
#     for sp in range(1,n-i+1):
#         print(" ",end='')
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()
# for i in range(n-1,0,-1):
#     for sp in range(1,n-i+1):
#         print(" ",end='')
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()



# n = 5
# for i in range(1,n+1):
#     for sp in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(i-1,0,-1):
#         print(k,end="")
#     print()
    
        
# n = 5
# num=1
# for i in range(1,n+1):
#     for sp in range(1,n-i+1):
#         print(" ",end="")
#     print(num*num,end="")
#     num = num + pow(10,i)
#     print()


# n = 4
# num=0
# k=n
# r=1
# l=1
# for i in range(1,n+1):
#     for sp in range(1,num+1):
#         print(" ",end="")
#     for j in range(1,k+1):
#         print(l,"*",end="")
#         l+=1
#     for right in range(1,k+1):
#         print((k*k)+r,"*",end = "")
#         r+=1
#     num+=2
#     k-=1
#     print()
        
# n = 4
# count=1
# for i in range(n,0,-1):
#     for sp in range(n-i):
#         print(" ",end="")
#     for j in range(i): 
#         print(count,end="") 
#         count+=1
#     print()
    
# n=4 
# count=1
# for i in range(n,0,-1):
#     for space in range(n-i):
#         print(" ",end="")
        
#     for j in range(i):
#         print(count,end="")
#         count+=1
#     print()


# n = 5
# num = 1
# spiral = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(0)  
#     spiral.append(row)
# top = 0
# bottom = n - 1
# left = 0
# right = n - 1
# while num <= n * n:
#     for i in range(left, right + 1):
#         spiral[top][i] = num
#         num = num + 1
#     top = top + 1 
#     for i in range(top, bottom + 1):
#         spiral[i][right] = num
#         num = num + 1
#     right = right - 1  
#     for i in range(right, left - 1, -1):
#         spiral[bottom][i] = num
#         num = num + 1
#     bottom = bottom - 1 
#     for i in range(bottom, top - 1, -1):
#         spiral[i][left] = num
#         num = num + 1
#     left = left + 1  
# for i in range(n):
#     for j in range(n):
#         print(spiral[i][j], end="\t")
#     print()


# rows = 5
# triangle = []

# for i in range(rows):
#     row = [1]
#     if i > 0:
#         for j in range(1, i):
#             value = triangle[i - 1][j - 1] + triangle[i - 1][j]
#             row.append(value)
#         row.append(1)
#     triangle.append(row)
# for i in range(rows):
#     for space in range(rows - i - 1):
#         print(" ", end=" ")
#     for num in triangle[i]:
#         print(num, end="   ")
#     print()


# n = 5

# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     for j in range(2 * (n - i)):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     for j in range(2 * (n - i)):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(2*(n-i)+1):
#         print("*",end=" ")
#     for j in range(i):
#         print(" ",end=" ")
#     print()
# for i in range(1,n+1):
#     for j in range((n-i)):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(2*(n-i)+1):
#         print(" ",end=" ")
#     print()
        
