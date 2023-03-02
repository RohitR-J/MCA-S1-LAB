'''Generate Fibonacci series of N terms '''

def fiba(n):
    a,b = 0,1
    print(a)
    print(b)

    for i in range(n-2):
        c = a+b
        a,b = b,c
        print(c)
num = int(input("Enter a num:"))
print("Fibanocci series of ",num," is",fiba(num))

