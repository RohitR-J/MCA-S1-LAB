class Account:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Your new balance is {self.balance}.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is {self.balance}.")
            
    def check_balance(self):
        print(f"Your current balance is {self.balance}.")
        
    def account_details(self):
        print(f"Account Name: {self.name}")
        print(f"Account Balance: {self.balance}")
        
class ATM:
    def __init__(self):
        self.accounts = {}
        
    def create_account(self):
        name = input("Enter your name: ")
        pin = input("Enter a 4-digit PIN: ")
        account = Account(name, pin)
        self.accounts[name] = account
        print("Account created successfully.")
        
    def login(self):
        name = input("Enter your name: ")
        pin = input("Enter your 4-digit PIN: ")
        if name not in self.accounts or self.accounts[name].pin != pin:
            print("Invalid name or PIN.")
            return None
        else:
            return self.accounts[name]
        
    def menu(self):
        print("Welcome to the ATM.")
        account = self.login()
        if not account:
            return
        while True:
            print("Select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Account Details")
            print("5. Logout")
            choice = input()
            if choice == "1":
                amount = int(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = int(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                account.account_details()
            elif choice == "5":
                print("Logout successful.")
                break
            else:
                print("Invalid choice.")
                
atm = ATM()
while True:
    print("Select an option:")
    print("1. Create Account")
    print("2. Login")
    print("3. Quit")
    choice = input()
    if choice == "1":
        atm.create_account()
    elif choice == "2":
        atm.menu()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

