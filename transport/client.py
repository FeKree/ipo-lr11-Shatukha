class Client:
    def __init__(self, name, cargo_weight, is_vip = False):
        self.name = name # Имя клиента
        self.cargo_weight = cargo_weight # Вес груза
        self.is_vip = is_vip # флаг VIP-статуса
    
    def __str__(self): # Магический метод 
        print(f"Клиент {self.name} (VIP: {self.is_vip}) с весом {self.cargo_weight}")
