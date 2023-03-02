'''
Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank. 
'''

class BankAccount:
	def __init__(self):
		self.name = "Rohit"
		self.acc_no = 12121212
		self.acc_type = "Zero Balance"
		self.balance = 0
	
	def deposit(self):
		deposit = float(input("Enter amount to deposit: "))
		self.balance += deposit
		print("Account balance : ", self.balance,"\n")
	
	def withdraw(self):
		withdraw = float(input("Enter the amount to withdraw: "))
		if self.balance >= withdraw:
			self.balance -= withdraw
		else:
			print("Insufficient balance")
		print("Net Available balance is ",self.balance,"\n")
	
b = BankAccount()
while(1):
	print(" Choose an option")
	ch = int(input(" 1.Deposit \n 2.Withdraw \n"))
	if ch == 1:
		b.deposit()
	elif ch == 2:
		b.withdraw()
	else:
		print("Invalid")
		exit()
		
'''
Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank. 
'''
'''
class bank:
	def __init__(self):
		self.name = 'jisha'
		self.accno = 1212121
		self.acc_type = "Zero balance"
		self.bal = 0
	
	def deposit(self):
		amount = int(input("Enter amount to deposit"))
		self.bal += amount
		print("credited",amount,"current bal: ",self.bal)
	
	def withdraw(self):
		withd = int(input("Enter amount to withdraw"))
		if self.bal >= withd:
			self.bal -= withd
			print("debited : ",withd," current bal: ",self.bal)
		else:
			print("Insufficient balance")
	
	
b = bank()

while(1):
	print("1.deposit")
	print("2.withdraw")
	print("3.exit")
	ch = int(input("Enter ur choice"))
	if ch == 1:
		b.deposit()
	if ch == 2:
		b.withdraw()
	if ch == 3:
		exit()
	if ch > 3:
		print("Invalid")
	
'''


		
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
