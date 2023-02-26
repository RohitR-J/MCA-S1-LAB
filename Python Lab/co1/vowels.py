#list comprehensions
word = input("Enter a word")
vowels = "AaEeIiOoUu"

final = [i for i in word if i in vowels]
print(final)
count = {}
for i in final:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count)

