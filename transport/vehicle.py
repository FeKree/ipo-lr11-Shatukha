from .client import Client
import random 

def validation(prompt):
    while(True):
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else: 
            print("Введите необходимую информацию числом!")

class Vehicle:
    def __init__(self, capacity=0):
        self.vehicle_id = random.randint(100, 10000)
        self.capacity = capacity  # грузоподъемность транспортного средства в тоннах
        self.current_load = 0  # текущая загрузка транспортного средства
        self.clients_list = []  # список клиентов, чьи грузы загружены

    def load_cargo(self, client):
        if not isinstance(client, Client): 
            raise ValueError("client должен быть объектом класса Client")
        if (self.current_load + client.cargo_weight) > self.capacity:
            print("Превышение грузоподъемности транспортного средства")
            exit()
        else:
            self.current_load += client.cargo_weight

    def __str__(self):
        return f"ID транспорта: {self.vehicle_id}, грузоподъёмность в тоннах: {self.capacity}, текущая загрузка: {self.current_load}"
