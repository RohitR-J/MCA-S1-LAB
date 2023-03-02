'''import csv

filename = "new.csv"
data = [1,2,3,4,5,6]
with open(filename,"w") as cs:
	write = csv.writer(cs)
	write.writerow(data)	'''
'''
import csv

filename = 'new.csv'
values = [1, 'John', 25, 'New York']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(values)
    
with open(filename,"r") as cs:
	reader = csv.reader(cs)
	for rows in reader:
		print(rows)'''
'''		
import calendar
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
print(calendar.month(yy,mm))'''

"""
binary = input("Enter binary")
decimal = int(binary, 2)
print(decimal)"""

'''decimal  = int(input("Enter no:"))
decimal_to_binary = bin(decimal)[2:]
print(decimal_to_binary)'''

'''
def sum(num):
	var = str(num)
	sum_ = 0
	for i in var:
		new = int(i)
		sum_ += new	
	print(sum_)
sum(34)'''
'''
lis = [1,2,3,12,5,6,7]	

largest = lis[0]

for num in lis:
	if num < largest:
		largest = num
print("The largest number is : ",largest)'''

'''
num = int(input("Enter no to check palindrome or not"))
temp = num
reverse = 0

while temp > 0:
	digit = temp % 10
	reverse = reverse * 10 + digit
	temp //= 10

if num == reverse:
	print("The number is palindrome")
else:
	print("The number is not palindrome")'''
	
'''Generate all factors of a number.'''
'''
num = 10
lis = []
for i in range(1,num + 1):
	if num % i == 0:
		lis.append(i)
print("Factors of ",num," are ",lis)'''

'''Program to find the factorial of a number  '''
'''
num = int(input("Enter a number:"))
fact = 1
for i in range(1,num+1):
	fact *= i
print("factorial of a number is ",fact)'''

'''Generate Fibonacci series of N terms '''
'''
N = int(input("Enter number"))
a = 0
b = 1
count = 0
while count < N:
	print(a)
	c = a + b
	a = b
	b = c
	count+=1'''
	
'''
Display the given pyramid with step number accepted from user.
Eg: N=4
1
2 4
3 6 9
4 8 12 16 
'''
'''
# # # # # 
# # # # # 
# # # # # 
# # # # # 
# # # # # 

''''''
n = int(input("ENter no of steps"))
for i in range(n):
	for j in range(n):
		print("# ",end="")
	print()'''

'''
# 
# # 
# # # 
# # # # 
# # # # # 
'''
'''
for i in range(5):
	for j in range(i+1):
		print("#", end = " ")
	print()

for i in range(4):
	for j in range(4-i):
		print("#",end = ' ')
	print()
'''	'''
string = 'rohitraj'
d = {}
for i in string:
	if i in d:
		d[i] += 1
	else:
		d[i]=1
print(d)'''

'''
string = input("Enter a string")
leng = len(string)
n = leng - 3
slice_ = string[n:]
if slice_ == 'ing':
	string += 'ly'
else:
	string += 'ing'
print(string)'''

'''
if 'ing' not in string[:-1]:
	
	print(string)
else:
	print(string)'''
'''
lis = [12,2,3]
#lis = ["apple", "pappaya","grapes"]
word_len = 0
for i in lis:
	if i > word_len:
		word_len = i
	
print(word_len)'''
'''
n = 16
for i in range(1,n):
	if n % i == 0:
		print(i)'''

'''word = "12"'''
'''
rev = word[::-1]
if word == rev:
	print(f"{word} == {rev}")
else:
	print(f"{word} != {rev}")'''
	
	
'''	
num = 1634
order = len(str(num))

sum_ = 0

temp = num
while temp > 0:
	digit = temp%10
	sum_ += digit **order
	temp //= 10
print(sum_)
if num == sum_:
	print("Armstrong number")
else:
	print("Not")
'''
'''
a,b = 12378,3054
if b>a:
	a,b = b,a
while b != 0:
	r = a%b
	a = b
	b = r
print(a	)'''
'''
lis = ["Rohit","Raj"]
mystr = ''.join(str(ele) for ele in lis)
print(mystr)'''

'''Print number 1-20 
multiples of ‘3’ print “Fizz”  and for the multiples of ‘5’ print “Buzz”'''
'''
for i in range(1,21):
	if i%3 == 0:
		print("Fizz")
	elif i%5 == 0:
		print("Buzz")
	else:
		print(i)'''
'''	
num = 123
sum_ = 0
temp = num	
def happy(num) :
	
	while temp >0:
		digit = temp%10
		sum_ += digit**2
		temp //= 0
	return sum_
 	
res = temp
while(res!=1 and res!=4):
	res = happy(num) 
	if result == 1:
 		print("happy number") 
	elif(result==4) :
   		print("unhappy number")'''
'''   	
def happ(num):
	sum = 0
	while num > 0:
		digit = num %10
		sum += digit**2
		num //= 10
	return sum
num = int(input("Enter the num"))
res = num
while(res != 1 and	 res !=4):
	res = happ(res)
if res ==1:
	print("num is happy")
elif res == 4:
	print("num is not happy")'''
'''
num = 13
if num>1:
	for n in range(2,num):
		if num %n == 0:
			print(num," is not a prime number")
			break
	else:
		print(num," is a prime number")
			
else:
	print(num," is not a prime number")'''
'''	
matrix1 = [[1,2,3],
		   [4,5,6],
		   [7,8,9]]
matrix2 = [[1,2,3],
		   [4,5,6],
		   [7,8,9]]
res = 	   [[0,0,0],
		   [0,0,0],
		   [0,0,0]]
for i in range(len(matrix1)):
	for j in range(len(matrix1[0])):
		res[i][j] = matrix1[i][j] + matrix2[i][j]
for i in res:
	print(i)
'''

'''transpose'''
'''
matrix1 = [[1,2,3],
		   [4,5,6],
		   [7,8,9]]

trans = 	[[0,0,0],
		   [0,0,0],
		   [0,0,0]]
for i in range(len(matrix1)):
	for j in range(len(matrix1[0])):
		trans[j][i] = matrix1[i][j]

for i in trans:
	print(i)'''
	
n = 4
adj_matrix = [[0] * n for _ in range(n)]

adj_matrix[0][1] = 1
adj_matrix[0][2] = 1
adj_matrix[1][1] = 1
adj_matrix[2][1] = 1
for row in adj_matrix:
	print(row)






	
	
