def revnum(n):
    rev=0
    while n>0:
        digit = n%10
        rev = rev*10+digit
        n=n//10
    return rev

def recpali(n,k):
    for i in range(1,k+1):
        s = n+revnum(n)
        if s==revnum(s):
            return [i,s]
        n=s
    return [-1,-1]
                    
print(recpali(89,23))
