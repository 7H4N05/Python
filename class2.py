import os
class Account:
    def __init__(self,accnum,bal):
        self.accnum = accnum 
        self.bal = bal
    def credit(self):
        cr=int(input("\nEnter the amount to credit:"))
        self.bal+=cr
    def debit(self):
        db=int(input("\nEnter the amount to debit:"))
        self.bal-=db
    def balance(self):
        print("\nThe amount balance in the account is:",self.bal)

acc=int(input("\nEnter account no:"))     
balance=int(input("\nEnter the amount balance:"))
A1=Account(acc,balance)

while(True):
    choice=input("b:Show balance\nc:Credit money\nd:Debit money\ne:exit\nEnter a choice:")
    os.system('cls')
    if choice=="c":
        A1.credit()
        A1.balance()
        

    elif choice=="b":
        A1.balance()

    elif choice=="d":
        A1.debit()
        A1.balance()
    
    elif choice=="e":
        break

    else:
        print("\nwrong choice entred!!")    

