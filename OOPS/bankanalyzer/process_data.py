

from csv import DictReader

class TransactionAnalyzer:

    def __init__(self):

        fr = open("OOPS\\bankanalyzer\\bank_transactions_500_records.csv")

        self.transaction = list(DictReader(fr))

        print(self.transaction)

        print(len(self.transaction),"records found")


    def debit_transaction(self):

        for t in self.transaction:

            if t.get("type")=="debit":

                print(t)

    def high_value_transactions(self):  #amount>75000

        self.high_value_transactions = [t for t in self.transaction if int(t.get("amount"))>75000]

        print(self.high_value_transactions)

    def highest_debit_transaction(self):

        self.highest_debit = max([t.get("amount") for t in self.transaction if t.get("type")=="debit"])

        self.highest_debit_transaction = [t for t in self.transaction if t.get("amount")==self.highest_debit]

        print(self.highest_debit_transaction)

    def highest_credit_transaction(self):

        self.highest_credit = max([t.get("amount") for t in self.transaction if t.get("type")=="credit"])

        self.highest_credit_transaction = [t for t in self.transaction if t.get("amount")==self.highest_credit]

        print(self.highest_credit_transaction)





analysis = TransactionAnalyzer()

analysis.debit_transaction()
analysis.high_value_transactions()
analysis.highest_debit_transaction()
analysis.highest_credit_transaction()