#Find biggest of 3 numbers entered. 

print("Enter 3 numbers:")
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1>=n2 and n1>=n3:
    biggest = n1
elif n2>=n3 and n2>=n3:
    biggest = n2
else:
    biggest = n3
print("The biggest number is:",biggest)
