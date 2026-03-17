

class Payment:
    def pay(self):
        print("Processing payment")


class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")


class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")


payment_instance = Payment()
credit_instance = CreditCard()
upi_instance = UPI()

# Call pay() method
payment_instance.pay()
credit_instance.pay()
upi_instance.pay()