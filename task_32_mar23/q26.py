class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully")
            print(f"{self.balance} is the new balance")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
            print(f"{self.balance} is the new balance")

    def check_balance(self):
        print(f"Current balance={self.balance}")


account = BankAccount("Manoj", 1000)

account.check_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.check_balance()


