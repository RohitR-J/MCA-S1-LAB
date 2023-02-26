'''
Accept an integer n and compute n+nn+nnn.  
'''
n = int(input("Enter a integer value"))
nn = n*10 + n
nnn = n*100 + nn
result = n+nn+nnn
print(result)

