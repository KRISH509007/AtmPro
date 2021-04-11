class Atm(object):
    def __init__(self,start,pin,check_balance,cash_withdraw,others):
        self.pin = pin
        self.check_balance = check_balance
        self.cash_withdraw = cash_withdraw
        self.others=others
    def start(self):
        print("hi")
    def pin(self):
        print("Enter Your Pin:")
    def check_balance(self):
        print("Click here to check balance!!")
    def cash_withdraw(self): 
        print("Withdraw cash here!..")
    def others(self):
        print(" other options!") 

bank=Atm(1234,"balance 100000","money withdraw 1000","options")
    print(bank.start())
 