

from abc import ABC, abstractmethod
class toyota(ABC):
    def price(self, cost):
        print("Your payment amount: ",cost)


    @abstractmethod
    def amount(self, cost):
        pass

class CreditCardPayment(toyota):
    def amount(self, cost):
        print("Your payment of {} exceeded your $150 limit ".format(cost))

calc = CreditCardPayment()
calc.price("$800")
calc.amount("$800")

    
    
