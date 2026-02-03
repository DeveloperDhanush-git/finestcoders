# def rotate_list(lst,k):
#     k = k % len(lst)
#     return lst[-k:] + lst[:-k]

# print(rotate_list([1,2,3,4,5,6],8))

# def dupli(lst):
#     result = []
#     for x in lst:
#         if x not in result:
#             result.append(x)
#     result.sort()
#     return result

# print(dupli([1,2,3,3,3,3,4,4,4,5,5,7,6,9]))

# def revarr(lst):
#     return lst[::-1]

# print(revarr([1,2,3,4,4,5]))

# def revarr(lst):
#     if lst[::-1] == lst:
#         return print("yes")
        
# revarr([1,2,2,1])

# def max_min(lst):
#     return max(lst), min(lst)

# print(max_min([5, 2, 8, 1]))


# def count_even_odd(lst):
#     even_count = 0
#     odd_count = 0
#     for x in lst:
#         if x % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return even_count, odd_count

# result = count_even_odd([1, 2, 3, 4, 5, 6])
# print(result)  # Output: (3, 3)

# def seclar(lst):
#     lst.sort()
#     return lst[-2]

# print(seclar([1,2,3,4,6,5]))

# def merge(l1,l2):
#     merged = l1 + l2
#     merged.sort()
#     return merged
# print(merge([9,2,3],[4,5,6]))

# def miss(lst,n):
#     x = []
#     for i in range(1,n+1):
#         if i not in lst:
#             x.append(i)
#     return x
        
# print(miss([1,2,4,5],5))
        
# def samearr(arr1,arr2):
#     arr1.sort()
#     arr2.sort()
#     if arr1 == arr2:
#         return "same"
# print(samearr([1,4,2,4,6],[1,4,2,4,6]))

# def separr(arr1):
#     pos = []
#     neg = []
#     for x in arr1:
#         if x >=0:
#             pos.append(x)
#         else:
#             neg.append(x)
#     return pos,neg
# print(separr([1,2,3,4,-1,-3]))

# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]

# # Example
# string = "hello"
# a=reverse_string(string)  # Output: "olleh"
# print(a)
# if string == a :
#     print("yes pali")
# else:
#     print("no")

# def rev(word):
#     if word == "":
#         return word
#     else:
#         return rev(word[1:]) + word[0]
# string = "hello"
# a= rev(string)
# print(a)
# if string == a:
#     print("pali")
# else:
#     print("no")

# def recfac(num):
#     if num == 0:
#         return 1
#     else:
#         return recfac(num-1) * num
    
# print(recfac(0))

# def vow(s):
#     if len(s)==0:
#         return 0
#     if s[0] in "aeiou":
#         return 1 + vow(s[1:])
#     return vow(s[1:])
    
# print(vow("aeiouthhhsknd"))


# arr = input().lower()
# print(arr)
# vowels = ["a","e","i","o","u"]
# for i in range(0,len(arr)):
#     if arr[i] in vowels:
#         print("vowels",arr[i])
#     else:
#         print("consonants",arr[i])

# def evalid(email):
#     if email.endswith(".com"):
#         return "logged in"
#     else:
#         return "enter correct email"

# emailname = input()
# print(evalid(emailname))