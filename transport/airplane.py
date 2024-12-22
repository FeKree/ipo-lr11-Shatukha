from .vehicle import Vehicle # Импорт класс Vehicle

class Airplane(Vehicle):
    def __init__(self, capacity, max_altitude):
        if isinstance(max_altitude, (int, float)) and max_altitude > 0:
            super().__init__(capacity)
            self.max_altitude = max_altitude
        else:
            raise ValueError("Высота полета должна быть положительным числом!")
        
    def __str__(self):
        return super().__str__() + f". Максимальная высота полета {self.max_altitude} метров"
      
  
