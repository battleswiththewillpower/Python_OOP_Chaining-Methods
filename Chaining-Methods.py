"""make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified

display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150

BONUS: transfer_money(self, other_user, amount) 
- have this method decrease the user's balance by the amount and add that amount to other other_user's balance"""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        #print the users name and account balance
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        #decrease the users balance, add the amount taken out to another users acct
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self
        
mars = User("mars", "sentfrom-mars@planet.com")
mars.make_deposit(10000).make_deposit(22300).make_deposit(722).make_withdrawal(722).display_user_balance()

creed = User("creed", "creed-aim-high@prosper.com")
creed.make_deposit(5000).make_deposit(15000).make_withdrawal(2300).make_withdrawal(573).display_user_balance()
brooklyn = User("brooklyn", "hyped_doggie24-7@alwaysonten.com")
brooklyn.make_deposit(6479).make_withdrawal(360).make_withdrawal(100).make_withdrawal(50).display_user_balance()
#transfer money
mars.transfer_money(brooklyn, 2300)
"""mars.display_user_balance()
brooklyn.display_user_balance()"""