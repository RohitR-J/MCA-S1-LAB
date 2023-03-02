'''Generate a list of four digit numbers in a given range with all their digits even and the
 number is a perfect square. '''


n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
n3=int(input("Enter a number"))
if n1>n2 and n1>n3:
    biggest=n1
elif n2>n3 and n2>n1:
    biggest=n2
else:
    biggest=n3
print("The biggest number is",biggest)
