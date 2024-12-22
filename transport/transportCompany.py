from .vehicle import Vehicle # Импорт класс Vehicle
from .airplane import Airplane
from .van import Van
from .client import Client

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = [] # список транспортных средств
        self.clients = [] # список клиентов

    def add_vehicle(self, vehicle): # добавляет транспортное средство
        if not isinstance(vehicle, Vehicle): # — это условие, которое проверяет, является ли объект vehicle экземпляром класса Vehicle
            raise ValueError("vehicle должен быть объектом класса Vehicle")
        self.vehicles.append(vehicle)

    def list_vehicles(self): # возвращает список всех транспортных средств
        vehicles_list = []
        for vehicle in self.vehicles:
            vehicles_list.append(str(vehicle))
        return vehicles_list 


    def add_client(self, client): # добавляет клиента
        if not isinstance(client, Client):
            raise ValueError("client должен быть объектом класса Client")
        self.clients.append(client)

    def optimize_cargo_distribution(self):
        # Сортируем транспортные средства по грузоподъемности (по убыванию)
        sorted_vehicles = sorted(self.vehicles, key=lambda v: v.capacity, reverse=True)

        for client in self.clients:
            for vehicle in sorted_vehicles:
                if vehicle.current_load + client.cargo_weight <= vehicle.capacity:
                    vehicle.current_load += client.cargo_weight  # Добавляем груз
                    print(f"Груз клиента {client.name} (вес: {client.cargo_weight}) распределен на транспортное средство {vehicle.vehicle_id}")
                    break
