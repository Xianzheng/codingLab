
'''
from abc import ABC, abstractmethod

class Order():
    def __init__(self,quantity,price,promote) -> None:
        self.quantity = quantity
        self.price = price
        self.promote = promote

    def total(self):
        return self.price * self.quantity
    
    def due(self):

        return self.total() - self.promote.discount(self)
    
    def __repr__(self) -> str:
        return 'original price is %s ' % self.total() + \
            'after discount is %s' % self.due()

    
class Promote(ABC):
    @abstractmethod
    def discount(self,order):
        pass

class Pa(Promote):

    def discount(self,order):
        return order.total() * 0.08
    
print(Order(8,10,Pa()))
'''

from abc import ABC, abstractmethod

class Order():
    def __init__(self,quantity,price,promote) -> None:
        self.quantity = quantity
        self.price = price
        self.promote = promote

    def total(self):
        return self.price * self.quantity
    
    def due(self):

        return self.total() - self.promote(self)
    
    def __repr__(self) -> str:
        return 'original price is %s ' % self.total() + \
            'after discount is %s' % self.due()
    

def A(order):
    return order.total() * 0.08

print(Order(8,10,A))