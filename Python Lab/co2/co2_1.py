'''Program to find the factorial of a number'''

def facto(n):
    fact = 1
    for i in range(1,n+1):
        fact  = fact*i
    return fact

num = int(input("Enter a number to find its factorial"))
print("Factorial of ",num," is ",facto(num))

