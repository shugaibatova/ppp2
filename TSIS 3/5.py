# Create a bank account class that has attributes owner, balance and 
# two methods deposit and withdraw. Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals,
#  and test to make sure the account can't be overdrawn.
class bank_account():
    def __init__(self):
        self.owner="Azamat"
        self.balance=0
    def deposit(self,summa):
        self.balance+=summa
        print(f"Balance:{self.balance} tg")
    def withdraw(self,tg):
        if tg<self.balance:
            self.balance-=tg
            print(f"Removed:{tg} tg -> Remainder balance: {self.balance} tg")
        else: 
            print( "Overdrawn!!!!!")
            print("Missing:",tg-self.balance,"tg")

bank1=bank_account()
bank2=bank_account()
bank3=bank_account()
bank1.deposit(100000)
bank1.withdraw(120000) #might output Overdrawn
#2
bank2.deposit(35000)
bank2.withdraw(12000) #might output remainder balance
#3
bank3.deposit(4000)
bank3.withdraw(12304) #output remainder balance

        
       


