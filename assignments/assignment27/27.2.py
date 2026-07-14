# Bank Acount class

class BankAcount:
    ROI  = 10.5

    def __init__(self,name, amount):
        self.name = name
        self.amount = amount

    def Display(self):
        print("Name = ", self.name)
        print("Balance = ",self.amount)

    def Deposite(self,amt):
        self.amount += amt
        print("Deposited amount =" ,amt)

    def Withdraw(self, amt):
        if amt <= self.amount:
            self.amount -= amt
            print("Withrawn: ", amt)
        else:
            print("Insufficient balance")  

    def Interest(self):
        interest = (self.amount * BankAcount.ROI) / 100
        return interest

obj = BankAcount("Amit", 100)    
obj.Display()
obj.Deposite(500)
obj.Withdraw(100)
obj.Display()
print("Interest: ", obj.Interest())




