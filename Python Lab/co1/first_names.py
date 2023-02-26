'''
Store a list of first names. Count the occurrences of ‘a’ within the list
'''
fnames = ['tovino','asif','fahad']
count_a = 0
for names in fnames:
    count_a += names.count("a")
print("The occurrences of ‘a’ within the list is ",count_a)
