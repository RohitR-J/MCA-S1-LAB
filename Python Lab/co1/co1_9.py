'''
Create a string from given string where first and last characters exchanged.
[eg: python -> nythop] 
'''
word = input("Enter a word")
firstchar = word[0]
lastchar = word[-1]
middlechar = word[1:-1]
exchanged = lastchar + middlechar + firstchar
print(exchanged)
