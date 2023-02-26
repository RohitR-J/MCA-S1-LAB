'''Find gcd of 2 numbers. '''

def gcd(a,b):
    if b>a:
        a,b = b,a
        
    while b!=0:
        r = a%b
        a = b
        b = r
        
    return a

num1 = int(input("Enter first num"))
num2 = int(input("Enter second num"))

print("gcd of",num1, "and" ,num2, "is ",gcd(num1,num2))
