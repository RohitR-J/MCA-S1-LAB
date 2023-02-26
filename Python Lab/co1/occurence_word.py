#Count the occurrences of each word in a line of text.
text = input("Enter text")
word = text.split(" ")
dic = {}
for count in word:
    if count in dic:
        dic[count]+=1
    else:
        dic[count]=1
print(dic)
