class User:
    def __init__(self, name_input, email_input):
        self.name=name_input
        self.email=email_input
        self.account_balance=0.0
        
class Bank_account:
    def __init__(self, int_rate,account_balance,name_input,email_input):
     self.name=name_input
     self.email=email_input
     self. account_balance=0.00
     self.int_rate=0.1
     
    def add_interest(self):
         self.account_balance=(self.accout_balance*self.account_in_rate)
         print(self.account_balance)
         return self

    def make_deposit(self, amount):
            self.account_balance +=amount
            return self
        
    def venmo (self, amount, payee):
            self.account_balance -=amount
            payee.account_balance +=amount
            return self

    def make_widthdrawl(self, amount):
        self.account_balance -= amount
        return self
        

