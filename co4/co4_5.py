'''Create a class Publisher (name). Derive class Book from Publisher with attributes title and
author. Derive class Python from Book with attributes price and no_of_pages. Write a
program that displays information about a Python book. Use base class constructor invocation and
method overriding. '''

class publisher:
	def __init__(self):
		self.name = "Jacob Thomas"
		
	def display(self):
		print("publisher: ",self.name)

class book(publisher):
	def __init__(self):
		super().__init__()
		self.title = "Cobra"
		self.author = "Terry Silver"

class python(book):
	def __init__(self):
		super().__init__()
		self.price = 100
		self.pages = 50
	
	def display(self):
		super().display()
		print("tile: ",self.title)
		print("author: ",self.author)
		print("price: ",self.price)
		print("pages: ",self.pages)
b = python()
b.display()	
		
		
		
		
