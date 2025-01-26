import sys
import random
class bank:
    def __init__(self,name,Balance,Account_number):
        self.name=name
        self.Balance=Balance
        self.Account_number=Account_number


    def Deposit(self,Amount):
        self.Balance =self.Balance+Amount
        print("Balance Amount:",self.Balance)
        
    def Withdraw(self,Amount):
        if self.Balance < Amount:
            print("Unsufficent Balance")
        else:
            self.Balance = self.Balance - Amount
            print("Balance Amount:",self.Balance)
def generate_account_number():
    return random.randint(1000000000, 9999999999) 
print("Create your bank Account")            
name = input("Enter your name:")
Account_number = generate_account_number()
print("Account Number:",Account_number)
Balance = int(input("Enter your Balance:"))
s=bank(name,Balance,Account_number)
print("***welcome to kt bank***")
print("1.Deposit\n2.Withdraw\n3.exit")

option = input("Enter your option:")

while True:
    if option == "1" :
        Amount = int(input("Enter your Amount:"))
        s.Deposit(Amount)
        sys.exit()
    elif option == "2":
        Amount = int(input("Enter your Amount:"))
        s.Withdraw(Amount)
    else:
        print("Thanks for visiting")
        sys.exit()