#list comprehensions

text = input("Enter text: ")
ord_list = [ord(val) for val in text]
print(ord_list)

for i,j in zip(text,ord_list):
    print(i,j)
