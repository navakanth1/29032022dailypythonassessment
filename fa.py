def Armstrong(a):
    b = 0
    c = a
    while c > 0:
        digit = c % 10
        b += digit ** 3
        c //= 10
    if a == b:
        return True
    else:
        return False
def divisible(x):
    if x%8==0:
        return True
    else:
        return False
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
def even(a):
    if a%2==0:
        return True
    else:
        return False
def Palindrome(a):
    b = a[::-1]
    if a == b :
        True
    else :
        False

if __name__=="__main__":
    a = int(input("Enter the number armstrong,divisible,even:"))
    b = int(input("Enter the number 1:"))
    c = int(input("Enter the number2:"))
    d = int(input("Enter the number3:"))
    e = input("Enter the string for palindrome:")
    result = Armstrong(a)
    print(result)
    result1 = divisible(a)
    print(result1)
    result2 = largest(b,c,d)
    print(result2)
    result3 = even(a)
    print(result3)
    result4 = Palindrome(e)
    print(result4)