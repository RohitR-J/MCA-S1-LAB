'''
Print out all colors from color-list1 not contained in color-list2.  
'''
lis1 = ['red','orange','magenta','cyan','violet','green','blue']
lis2 = ['cyan','magenta','purple','red','pink','blue']
for i in lis1:
    if i in lis2:
        continue;
    else:
        print(i)
