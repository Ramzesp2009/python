from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def initialize_payment(self, amount: float):
        pass

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def cancel_payment(self):
        pass


class CreditCardPayment(PaymentGateway):
    def __init__(self):
        self.is_called = False

    def initialize_payment(self, amount: float):
        print(f"It'll be payed {amount}")
        self.is_called = True

    def process_payment(self):
        print("The payment is in prosses")

    def cancel_payment(self):
        print("The payment will be canceled")

    def check_the_payment(self):
        return True if self.is_called else False


class BitcoinPayment(PaymentGateway):
    def __init__(self):
        self.__is_called = False

    def initialize_payment(self, amount: float):
        print(f"It'll be payed {amount}")
        self.__is_called = True

    def process_payment(self):
        print("The payment is in prosses")

    def cancel_payment(self):
        print("The payment will be canceled")

    def check_the_payment(self):
        return True if self.__is_called else False


def pay(obj, amount):
    obj.initialize_payment(amount)
    if obj.check_the_payment():
        print("The payment is successful")


bit_pay = BitcoinPayment()
# bit_pay.initialize_payment(5000.0)
pay(bit_pay, 5000)


