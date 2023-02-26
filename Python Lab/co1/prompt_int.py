'''Prompt the user for a list of integers.
For all values greater than 100, store ‘over’ instead.'''

size = int(input("Enter the size of list"))
lis = []
for i in range(size):
    val = int(input("Enter data:"))
    if (val>99):
        lis.append("over")
    else:
        lis.append(val)
print(lis)
        
