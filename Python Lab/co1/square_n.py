#list comprehension

n = int(input("Enter a limit:"))
sqr_n = [sqr**2 for sqr in range(n+1)]
print(sqr_n)
