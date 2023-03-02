'''
Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to
compare the area of 2 rectangles. 
'''

class Rectangle:
	def __init__(self):
		self.__len = int(input("Enter length"))  
		self.__wid = int(input("Enter width"))
		
	def area(self):
		return self.__len * self.__wid
		
	def __lt__(self, other):
		return self.area() < other.area()

rect1 = Rectangle()
rect2 = Rectangle()
print("area of rect1 is ",rect1.area())
print("area of rect2 is ",rect2.area())

if rect1 < rect2:
	print("area of rect2 is greater")
else:
	print("area of rect2 is greater")
