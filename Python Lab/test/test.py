'''
1. Create Rectangle class with attributes length and breadth and methods to find area and
perimeter. Compare two Rectangle objects by their area.

'''
'''
class rectangle:
	def __init__(self):
		self.leng = int(input("Enter len"))
		self.bread = int(input("Enter breadth"))
		
	def area(self):
		return self.leng * self.bread
		
	def peri(self): 
		return 2*(self.leng + self.bread)
rect1 = rectangle()
rect2 = rectangle()
print("rect1 area:",rect1.area())
print("rect1 peri:",rect1.peri())
print("rect2 area:",rect2.area())
print("rect2 area:",rect2.peri())'''


''' 2. Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank.'''

'''
class bankaccount:
	def __init__(self):
		self.acc_no = 123456
		self.name = "suresh"
		self.acc_type = "savings"
		self.bal = 0
	def depo(self):
		deposit = float(input("Enter amount:"))
		self.bal += deposit
		print(f"credited +{deposit} INR")
	
	def withd(self):
		deb = float(input("Enter amount to withdraw"))
		if self.bal >= deb:
			self.bal -= deb
			print(f"debited -{deb} INR")
		else:
			print("Insufficient balance")
	def balance(self):
		print("Account balance:",self.bal)
bank = bankaccount()
bank.depo()
bank.withd()
bank.balance()'''

		
		


'''3. Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to
compare the area of 2 rectangles.'''
'''
class rectangle:
	def __init__(self):
		self.__len  = float(input("Enter length"))
		self.__wid =  float(input("Enter breadth"))
	def area(self):
		return self.__len * self.__wid
	def __lt__(self,other)
		return self.area() < other.area()
rect1  = rectangle()
rect2 = rectangle()
if rect1 <rect2:
	print("Area of rect1 is greater")
else:
	print("Area of rect2 is greater")'''


'''4. Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
find sum of 2 time.'''
'''
class time:
	def __init__(self,hr,minu,sec):
		self.__hr = hr
		self.__minu = minu
		self.__sec = sec
	
	def get(self):
		return self.__hr,self.__minu,self.__sec
	
	def __add__(self,other):
		hr = self.__hr + other.__hr
		minu = self.__minu + other.__hr
		sec = self.__sec + other.__sec
		
		if sec >= 60:
			minu+=1
			sec-=60
		if minu>=60:
			hr +=1
			minu-=60
		if hr>=24:
			hr-=24
		return time(hr,minu,sec)
		
t1 = time(2,3,4)
t2 = time(5,6,7)
total = t1+t2
print(total.get())'''


'''5. Create a class Publisher (name). Derive class Book from Publisher with attributes title and
author. Derive class Python from Book with attributes price and no_of_pages. Write a
program that displays information about a Python book. Use base class constructor invocation and
method overriding. '''
'''
class publisher:
	def __init__(self):
		self.name = "raju"
	def disp(self):
		print("name : ", self.name)
		
class book(publisher):
	def __init__(self):
		super().__init__()
		self.title = "qaasas"
		self.author = "asasddf"

class Python(book):
	def __init__(self):
		super().__init__()
		self.price = 1212
		self.pages = 100
	def disp(self):
		super().disp()
		print("title : ", self.title)
		print("author : ", self.author)
		print("price : ",self.price)
		print("pages : ",self.pages)
book =Python()
book.disp()'''

"""Make an ATM system using python oops with the following activities account creation cash deposit cash withdrawal account balance account details view (multi user support)"""

class atm:
	def __init__(self,name,accno):
		


		



















		
