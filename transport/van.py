from .vehicle import Vehicle
from .client import Client

class Van(Vehicle):
    def __init__(self, capacity, is_refrigerated):
        super().__init__(capacity)
        self.is_refrigerated = is_refrigerated

    def __str__(self):
        return super().__str__() + f". Холодильник: {'есть' if self.is_refrigerated else 'нет'}"
    
