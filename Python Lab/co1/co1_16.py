'''
Create a single string separated with space from two strings by swapping the
character at position 1. 
'''
str1 = input("Enter string 1")
str2 = input("Enter string 2")

# Swap the characters at position 1
str1_new = str2[0] + str1[1:]
str2_new = str1[0] + str2[1:]

# Create a single string separated by a space
result = str1_new +' '+str2_new

print(result)
