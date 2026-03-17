

class BankAccount:

    def __init__(self,acc_name,balance):

        self.acc_name=acc_name
        self.balance=balance

    def display(self):

        print(self.acc_name,self.balance)

bankaccount_instance = BankAccount("vipin",5000)

bankaccount_instance.display()