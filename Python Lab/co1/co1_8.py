'''
Get a string from an input string where all occurrences of first character replaced with
‘$’, except first character.
[eg: onion -> oni$n]
'''

string = input("Enter a word")
first_char = string[0]
result = first_char + string[1:].replace(first_char,'$')
print(result)
