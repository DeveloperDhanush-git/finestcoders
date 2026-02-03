def isprime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
def alpharange(num):
    return (65<=num<=90) or (97<=num<=122)

ch = input("enter a character: ")

if not ch.isalpha():
    print("invalid input")
else:
    ascii_value = ord(ch)
    if (isprime(ascii_value)):
        print(ch)
    else:
        n=1
        while(True):
            left = ascii_value - n
            right = ascii_value + n
            if(alpharange(left) and isprime(left)):
                print(chr(left))
                break
            if(alpharange(right) and isprime(right)):
                print(chr(right))
                break
            n+=1