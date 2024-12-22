from transport import Client, Vehicle, TransportCompany, Van, Airplane

start = True
count = 0  # Счетчик для всех действий
all_clients = []
all_vehicles = []
id_counter = 0  # Номер клиента

def validation(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print("Введите необходимую информацию числом!")

def menu():
    print()
    print(f" Меню ".center(70, "="))
    print("""
        1 - Создать клиента
        2 - Добавить транспорт
        3 - Вывести список клиентов
        4 - Вывести информацию о всех транспортах
        5 - Оптимизировать распределение груза
        6 - Вывести распределение груза 
        7 - Распределить по одному 
        8 - Выход с программы\n""")
    print("".center(70, "="))    
    print()

def create_company(name): # Создали транспортную кмпанию
    return TransportCompany(name)

def create_client():
    name = input("Введите имя клиента:")
    cargo_weight = validation("Введите вес груза клиента:")

    while True:
        vip = validation("Введите, имеет ли клиент VIP (1 - да, 2 - нет): ")
        if vip == 1:
            is_vip = True
            break
        elif vip == 2:
            is_vip = False
            break
        else:
            print("Введите 1, если клиент имеет VIP. Если нет, введите 2.")

    client = Client(name, cargo_weight, is_vip)
    all_clients.append(client)
    print("Клиент успешно создан!")


def create_transport():
    while True:
        type_veh = validation("\nВыберите транспорт для добавления (1 - самолет, 2 - фургон): ")

        if type_veh == 1:
            capacity = validation("Введите грузоподъёмность самолёта: ")
            max_altitude = validation("Введите максимальную высоту полета: ")
            all_vehicles.append(Airplane(capacity, max_altitude))
            print("Самолёт успешно создан!")
            break

        elif type_veh == 2:
            capacity = validation("Введите грузоподъёмность фургона: ")
            is_refrigerated = get_refrigeration_status()
            all_vehicles.append(Van(capacity, is_refrigerated))
            print("Фургон успешно создан!")
            break

        else:
            print("Выберите 1, если хотите добавить самолет, 2 - если фургон.")

def get_refrigeration_status():
    while True:
        is_refrigerated = validation("Введите, имеет ли фургон холодильник (1 - да, 2 - нет): ")
        if is_refrigerated == 1:
            return True
        elif is_refrigerated == 2:
            return False
        else:
            print("Введите 1, если есть холодильник, 2 если нет.")


   


def print_all_transport():
    print()
    print("Все транспортные средства: ".center(70, "="))
    for idx, vehicle in enumerate(all_vehicles, start=1):
        print(f"{idx}) {vehicle}")
    print()


def print_all_clients():
    print()
    print("Все клиенты: ".center(70, "="))
    for idx, client in enumerate(all_clients, start=1):
        vip_status = "Есть" if client.is_vip else "Нет"
        print(f"{idx}. Имя: {client.name}. Вес груза: {client.cargo_weight}. VIP-статус: {vip_status}")
    print()

def display_cargo_distribution(company):
    print("\nРезультат распределения груза:")
    for vehicle in company.vehicles:
        print(vehicle)
        for client in vehicle.clients_list:
            print(f" - {client.name}: {client.cargo_weight} тонн, VIP: {'да' if client.is_vip else 'нет'}")

def main():
    global start, count
    name = input("Введите название транспортной компании: ")
    company = create_company(name)

    while start:
        menu()
        num = validation("Выберите необходимый пункт: ")

        if num == 1:
            create_client()
            count += 1

        elif num == 2:
            create_transport()
            count += 1

        elif num == 3:
            print_all_clients()
            count += 1

        elif num == 4:
            print_all_transport()
            count += 1

        elif num == 5:
            # Добавляем всех клиентов в компанию
            for client in all_clients:
                company.add_client(client)
    
            # Добавляем все транспортные средства в компанию
            for vehicle in all_vehicles:
                company.add_vehicle(vehicle)
            
            company.optimize_cargo_distribution()
            count += 1

        elif num == 6:
            display_cargo_distribution(company)

        elif num == 7:
            target_vehicle = input("Введите номер транспорта, в который хотите загрузить груз клиента: ")
            target_client = input("Введите номер клиента, груз которого хотите загрузить: ")
            try:
                target_vehicle = int(target_vehicle)
                target_client = int(target_client)
                all_vehicles[target_vehicle - 1].load_cargo(all_clients[target_client - 1])
                print("Груз успешно загружен!")
            except Exception as e:
                print(f"Возникла ошибка! Проверьте корректность введенных данных! Ошибка: {e}")


        elif num == 8:
            start = False
            print(f"Выход из программы. Количество проведедённых операций: {count}.")
            break

        else:
            print("Выберите один из предложенных пунктов!!!")


main()
