import dearpygui.dearpygui as dpg
import json
from transport import Client, Vehicle, TransportCompany, Van, Airplane

company = TransportCompany("TC")


def update_client():
    dpg.delete_item("clients_table", children_only=True)
    for client in company.clients:
        with dpg.table_row(parent="clients_table"): 
            dpg.add_text(client.name)  
            dpg.add_text(str(client.cargo_weight))  
            dpg.add_text("Да" if client.is_vip else "Нет")
            

def update_vehicle():
    dpg.delete_item("vehicles_table", children_only=True) 
    for vehicle in company.vehicles:
        with dpg.table_row(parent="vehicles_table"):
            dpg.add_text(str(vehicle.vehicle_id))
            dpg.add_text(str(vehicle.capacity)) 
            dpg.add_text(str(vehicle.current_load))
            if isinstance(vehicle, Airplane):
                dpg.add_text(f"Высота: {vehicle.max_altitude}") 
            elif isinstance(vehicle, Van):
                dpg.add_text(f"Холодильник: {'Да' if vehicle.is_refrigerated else 'Нет'}")  


def show_clients():
    if dpg.does_item_exist("all_clients_window"): 
        return
    with dpg.window(label="Все клиенты", modal=True, width=700, height=500, tag="all_clients_window"): 
        with dpg.table(header_row=True): 
            dpg.add_table_column(label="Имя клиента") 
            dpg.add_table_column(label="Вес груза")
            dpg.add_table_column(label="VIP статус")
            for client in company.clients:
                with dpg.table_row(): 
                    dpg.add_text(client.name) 
                    dpg.add_text(str(client.cargo_weight))
                    dpg.add_text("Да" if client.is_vip else "Нет") 
                    dpg.set_value("status", "Таблица выведена")
        dpg.add_button(label="Закрыть", callback=lambda: dpg.delete_item("all_clients_window"))



def show_vehicles():
    if dpg.does_item_exist("all_vehicles_window"): 
        for vehicle in company.vehicles:
            with dpg.table_row(): 
                dpg.add_text(str(vehicle.vehicle_id)) 
                dpg.add_text(str(vehicle.capacity)) 
                dpg.add_text(str(vehicle.current_load)) 
                if isinstance(vehicle, Airplane):
                    dpg.add_text(f"Высота: {vehicle.max_altitude}")
                elif isinstance(vehicle, Van):
                    dpg.add_text(f"Холодильник: {'Да' if vehicle.is_refrigerated else 'Нет'}")
            dpg.set_value("status", "Таблица выведена")
        return
    with dpg.window(label="Все транспортные средства", modal=True, width=900, height=700, tag="all_vehicles_window"):  # Создаем новое окно "Все транспортные средства"
        with dpg.table(header_row=True): 
            dpg.add_table_column(label="ID") 
            dpg.add_table_column(label="Грузоподъемность")
            dpg.add_table_column(label="Текущая загрузка")  
            dpg.add_table_column(label="Особенности")
            for vehicle in company.vehicles:
                with dpg.table_row():  
                    dpg.add_text(str(vehicle.vehicle_id)) 
                    dpg.add_text(str(vehicle.capacity))  
                    dpg.add_text(str(vehicle.current_load)) 
                    if isinstance(vehicle, Airplane):
                        dpg.add_text(f"Высота: {vehicle.max_altitude}")
                    elif isinstance(vehicle, Van):
                        dpg.add_text(f"Холодильник: {'Да' if vehicle.is_refrigerated else 'Нет'}")
            dpg.set_value("status", "Таблица выведена")
        dpg.add_button(label="Закрыть", callback=lambda: dpg.delete_item("all_vehicles_window")) 


def show_loaded():
    if dpg.does_item_exist("loaded_vehicles_window"): 
        for vehicle in loaded_vehicles:
                with dpg.table_row():
                    dpg.add_text(str(vehicle.vehicle_id)) 
                    dpg.add_text(str(vehicle.capacity)) 
                    dpg.add_text(str(vehicle.current_load))

                    if isinstance(vehicle, Airplane):
                        dpg.add_text(f"Высота: {vehicle.max_altitude}") 
                    elif isinstance(vehicle, Van):
                        dpg.add_text(f"Холодильник: {'Да' if vehicle.is_refrigerated else 'Нет'}") 
                dpg.set_value("status", "Таблица выведена")
        return

    loaded_vehicles = list(filter(lambda v: v.current_load > 0, company.vehicles)) 
    if not loaded_vehicles:  
        print("Нет загруженных транспортных средств.") 
        return

    with dpg.window(label="Загруженные транспортные средства", modal=True, width=600, height=400, tag="loaded_vehicles_window"): 
        with dpg.table(header_row=True):  
            dpg.add_table_column(label="ID")  
            dpg.add_table_column(label="Грузоподъемность")  
            dpg.add_table_column(label="Текущая загрузка") 
            dpg.add_table_column(label="Особенности")  

            for vehicle in loaded_vehicles:
                with dpg.table_row():  
                    dpg.add_text(str(vehicle.vehicle_id)) 
                    dpg.add_text(str(vehicle.capacity)) 
                    dpg.add_text(str(vehicle.current_load))

                    if isinstance(vehicle, Airplane):
                        dpg.add_text(f"Высота: {vehicle.max_altitude}")
                    elif isinstance(vehicle, Van):
                        dpg.add_text(f"Холодильник: {'Да' if vehicle.is_refrigerated else 'Нет'}") 
                dpg.set_value("status", "Таблица выведена")

        dpg.add_button(label="Закрыть", callback=lambda: dpg.delete_item("loaded_vehicles_window"))

    print("Окно с загруженными транспортными средствами создано.")


def client_form():
    if dpg.does_item_exist("client_form"): 
        return
    with dpg.window(label="Добавить клиента", width=400, height=300, modal=True, tag="client_form"):  
        dpg.add_text("Имя клиента:") 
        dpg.add_input_text(tag="client_name", width=250) 
        dpg.add_text("Вес груза:")  
        dpg.add_input_text(tag="client_cargo_weight", width=250)
        dpg.add_text("VIP статус:")  
        dpg.add_checkbox(tag="client_is_vip")
        dpg.add_button(label="Сохранить", callback=save_client) 
        dpg.add_button(label="Отмена", callback=lambda: dpg.delete_item("client_form")) 

def save_client():
    name = dpg.get_value("client_name") 
    cargo_weight = dpg.get_value("client_cargo_weight") 
    is_vip = dpg.get_value("client_is_vip") 

    if name and cargo_weight.isdigit() and int(cargo_weight) > 0:  
        client = Client(name, int(cargo_weight), is_vip)
        company.add_client(client) 
        update_client() 
        dpg.delete_item("client_form")
        dpg.set_value("status", "Клиент добавлен")
    else:
        dpg.set_value("status", "Ошибка: Проверьте введённые данные!") 


def vehicle_form():
    if dpg.does_item_exist("vehicle_form"): 
        return
    with dpg.window(label="Добавить транспорт", width=400, height=300, modal=True, tag="vehicle_form"): 
        dpg.add_text("Тип транспорта:")  
        dpg.add_combo(["Самолет", "Фургон"], tag="vehicle_type", width=250, callback=specific_reg) 
        dpg.add_text("Грузоподъемность (тонны):") 
        dpg.add_input_text(tag="vehicle_capacity", width=250) 

        dpg.add_text("Введите высоту полёта:", tag="max_altitude_label", show=False) 
        dpg.add_input_text(tag="max_altitude", width=250, show=False) 

        dpg.add_text("Есть ли холодильник:", tag="refrigerator_label", show=False) 
        dpg.add_checkbox(tag="refrigerator", show=False) 

        dpg.add_button(label="Сохранить", callback=save_vehicle)
        dpg.add_button(label="Отмена", callback=lambda: dpg.delete_item("vehicle_form")) 

def specific_reg(sender, app_data):
    if app_data == "Самолет":
        dpg.configure_item("max_altitude_label", show=True)  # Показать поле для высоты полёта
        dpg.configure_item("max_altitude", show=True)  # Показать поле для ввода высоты полёта
        dpg.configure_item("refrigerator_label", show=False)  # Скрыть поле для холодильника
        dpg.configure_item("refrigerator", show=False)  # Скрыть чекбокс для холодильника
    elif app_data == "Фургон":
        dpg.configure_item("max_altitude_label", show=False)  # Скрыть поле для высоты полёта
        dpg.configure_item("max_altitude", show=False)  # Скрыть поле для ввода высоты полёта
        dpg.configure_item("refrigerator_label", show=True)  # Показать поле для холодильника
        dpg.configure_item("refrigerator", show=True)  # Показать чекбокс для холодильника


def save_vehicle():
    vehicle_type = dpg.get_value("vehicle_type")  # Получение типа транспортного средства
    capacity = dpg.get_value("vehicle_capacity")  # Получение грузоподъемности

    if capacity.isdigit() and int(capacity) > 0:  # Проверка корректности введенной грузоподъемности
        capacity = int(capacity)
        if vehicle_type == "Самолет":
            max_altitude = dpg.get_value("max_altitude")  # Получение высоты полёта
            if max_altitude.isdigit() and int(max_altitude) > 0:  # Проверка корректности введенной высоты полёта
                vehicle = Airplane(capacity, int(max_altitude))  # Передаем высоту полёта
            else:
                dpg.set_value("status", "Ошибка: Проверьте высоту полёта!")  # Установка сообщения об ошибке
                return
        elif vehicle_type == "Фургон":
            has_refrigerator = dpg.get_value("refrigerator")  # Получение значения холодильника
            vehicle = Van(capacity, has_refrigerator)  # Создание объекта фургона
        else:
            vehicle = Vehicle(capacity)  # Грузовик по умолчанию
        dpg.set_value("status", "Транспорт добавлен")

        company.add_vehicle(vehicle)  # Добавление транспортного средства
        update_vehicle()  # Обновление таблицы транспортных средств
        dpg.delete_item("vehicle_form")  # Закрытие формы
    else:
        print("\n\n\n\n\n\n")
        dpg.set_value("status", "Ошибка: Проверьте введённые данные!")  # Установка сообщения об ошибке




# Создаем окно с VIP клиентами
    with dpg.window(label="VIP клиенты", modal=True, width=600, height=400, tag="clients_window"):  # Создаем новое окно "VIP клиенты"
        # Добавляем таблицу с данными
        with dpg.table(header_row=True):  # Создаем таблицу с заголовком
            dpg.add_table_column(label="Имя клиента")  # Добавляем колонку "Имя клиента"
            dpg.add_table_column(label="Вес груза")  # Добавляем колонку "Вес груза"
            dpg.add_table_column(label="VIP статус")  # Добавляем колонку "VIP статус"

            for client in filter(lambda c: c.is_vip, company.clients):  # Проходим по всем VIP клиентам
                with dpg.table_row():  # Добавляем строку в таблицу для каждого VIP клиента
                    dpg.add_text(client.name)  # Имя клиента
                    dpg.add_text(str(client.cargo_weight))  # Вес груза клиента
                    dpg.add_text("Да")  # VIP статус клиента
        
        dpg.add_button(label="Закрыть", callback=lambda: dpg.delete_item("clients_window")) # Кнопка для закрытия окна


def json_load():
    data = {
        "clients": [{"name": c.name, "cargo_weight": c.cargo_weight, "is_vip": c.is_vip} for c in company.clients],  # Список клиентов с их данными
        "vehicles": [
            {
                "vehicle_id": v.vehicle_id,  # ID транспортного средства
                "capacity": v.capacity,  # Грузоподъемность транспортного средства
                "current_load": v.current_load,  # Текущая загрузка транспортного средства
                "type": "Airplane" if isinstance(v, Airplane) else "Van" if isinstance(v, Van) else "Truck",  # Тип транспортного средства
                "details": {
                    "max_altitude": getattr(v, 'max_altitude', None),  # Высота полёта для самолета;getattr получить значение атрибута объекта по его имени в виде строки.
                    "has_refrigerator": getattr(v, 'has_refrigerator', None)  # Наличие холодильника для фургона
                }
            } for v in company.vehicles  # Проходим по всем транспортным средствам
        ]
    }

    with open("database.json", "w", encoding="utf-8") as file:  # Открываем файл "export.json" для записи с кодировкой "utf-8"
        json.dump(data, file, ensure_ascii=False, indent=4)  # Записываем данные в файл в формате JSON с отступами
    dpg.set_value("status", "Результаты экспортированы в файл database.json.")  # Устанавливаем сообщение о статусе экспорта


def optimize_cargo():
    company.distribute_cargo()  # Распределяем грузы по транспортным средствам
    update_vehicle()  # Обновляем таблицу транспортных средств
    dpg.set_value("status", "Грузы успешно распределены!")  # Устанавливаем сообщение о статусе распределения

def distribute_cargo_results():
    # Проверяем, существует ли уже окно с результатами распределения
    if dpg.does_item_exist("cargo_distribution_window"):  # Проверка, существует ли уже окно с результатами распределения
        with dpg.table(header_row=True):
            dpg.add_table_column(label="Транспортное средство")
            dpg.add_table_column(label="Грузоподъемность")
            dpg.add_table_column(label="Текущий груз")
            dpg.add_table_column(label="Распределенный груз")

            # Пример распределения груза: для каждого транспортного средства
            for vehicle in company.vehicles:
                # Пример распределения груза
                distributed_cargo = vehicle.current_load  # Здесь вы можете взять данные из своей логики распределения
                with dpg.table_row():
                    dpg.add_text(vehicle.vehicle_id)  # Идентификатор транспортного средства
                    dpg.add_text(str(vehicle.capacity))  # Грузоподъемность
                    dpg.add_text(str(vehicle.current_load))  # Текущий груз
                    dpg.add_text(str(distributed_cargo))  # Распределенный груз
        return


    # Создаем окно для отображения результатов
    with dpg.window(label="Распределение груза", modal=True, width=600, height=400, tag="cargo_distribution_window"):
        # Создаем таблицу для отображения результатов
        with dpg.table(header_row=True):
            dpg.add_table_column(label="Транспортное средство")
            dpg.add_table_column(label="Грузоподъемность")
            dpg.add_table_column(label="Текущий груз")
            dpg.add_table_column(label="Распределенный груз")

            # Пример распределения груза: для каждого транспортного средства
            for vehicle in company.vehicles:
                # Пример распределения груза
                distributed_cargo = vehicle.current_load  # Здесь вы можете взять данные из своей логики распределения
                with dpg.table_row():
                    dpg.add_text(vehicle.vehicle_id)  # Идентификатор транспортного средства
                    dpg.add_text(str(vehicle.capacity))  # Грузоподъемность
                    dpg.add_text(str(vehicle.current_load))  # Текущий груз
                    dpg.add_text(str(distributed_cargo))  # Распределенный груз

        # Кнопка для закрытия окна
        dpg.add_button(label="Закрыть", callback=lambda: dpg.delete_item("cargo_distribution_window"))


def show_me():
    if dpg.does_item_exist("about_window"):  # Проверка, существует ли уже окно "about_window"
        return

    with dpg.window(label="Программа", width=800, height=600, modal=True, tag="about_window"):  # Создание нового окна "О программе"
        dpg.add_text("Лабораторная работа 12", color=[133, 135, 55])  # Добавление текста "Лабораторная работа номер 12"
        dpg.add_text("Вариант: 4", color=[133, 135, 55])  # Добавление текста "Вариант: 4"
        dpg.add_text("Шатуха Алексей Кириллович",   color=[133, 135, 55]) 
        dpg.add_button(label="Закрыть", callback=lambda: dpg.delete_item("about_window"))  
        dpg.set_value("status", "Вот и вы")


def fonts():
    with dpg.font_registry():  # Создание реестра шрифтов
        with dpg.font("minecraft.ttf", 14) as default_font:  # Добавление шрифта Arial размером 20
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)  # Добавление диапазона шрифтов по умолчанию
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)  # Добавление диапазона шрифтов для кириллицы
            dpg.bind_font(default_font)  # Привязка шрифта по умолчанию


def optimize_cargo():
    company.optimize_cargo_distribution()  # Вызываем метод для распределения грузов
    update_vehicle()  # Обновляем таблицу с транспортными средствами
    dpg.set_value("status", "Грузы успешно распределены!")


def keyboard():
    """
    Настройка глобальных обработчиков клавиш для всех окон.
    """
    def handle_escape():
        # Закрытие всех открытых окон
        open_windows = [
            "client_form",  # Форма клиента
            "vehicle_form",  # Форма транспортного средства
            "clients_window",  # Окно клиентов
            "all_vehicles_window",  # Окно всех транспортных средств
            "about_window",  # Окно "О программе"
            "all_clients_window",  # Окно всех клиентов
            "cargo_distribution_window",  # Окно распределения грузов
            "cargo_distribution_window",  # Окно распределения грузов (повтор)
        ]
        for window in open_windows:
            if dpg.does_item_exist(window):  # Проверка, существует ли окно
                dpg.delete_item(window)  # Удаление окна

    def handle_enter():
        # Сохранение данных в активной форме
        if dpg.does_item_exist("client_form"):  # Проверка, существует ли форма клиента
            save_client()  # Сохранение данных клиента
        elif dpg.does_item_exist("vehicle_form"):  # Проверка, существует ли форма транспортного средства
            save_vehicle()  # Сохранение данных транспортного средства


    # Глобальная регистрация обработчиков
    with dpg.handler_registry():
        # Escape: закрыть окна
        dpg.add_key_down_handler(key=dpg.mvKey_Escape, callback=lambda: handle_escape())
        # Enter: сохранить данные
        dpg.add_key_down_handler(key=dpg.mvKey_Return, callback=lambda: handle_enter())

def main_topic():
    with dpg.window(label="Основное окно", width=1500, height=1000):  # Создаем основное окно
        dpg.add_button(label="О программе", callback=show_me )  # Добавляем кнопку "О программе" с вызовом функции show_about

        with dpg.group(horizontal=False):  # Создаем горизонтальную группу
            # Клиенты
            with dpg.group():  # Создаем группу для клиентов
                dpg.add_text("Клиенты", tag="clients_text" , color=[255, 0, 0])  # Добавляем текст "Клиенты"
                with dpg.table(tag="clients_table", header_row=True ):  # Создаем таблицу для клиентов
                    dpg  # Пустая строка для таблицы
                dpg.add_button(label="Добавить клиента", callback=client_form)  # Добавляем кнопку "Добавить клиента" с вызовом функции show_client_form
                dpg.add_button(label="Показать всех клиентов", callback=show_clients)  # Добавляем кнопку "Показать всех клиентов" с вызовом функции show_all_clients

            # Транспортные средства
            with dpg.group():  # Создаем группу для транспортных средств
                dpg.add_text("Транспортные средства", tag="vehicles_text" , color=[255, 0, 0] )  # Добавляем текст "Транспортные средства"
                with dpg.table(tag="vehicles_table", header_row=True):  # Создаем таблицу для транспортных средств
                    dpg  # Пустая строка для таблицы
                dpg.add_button(label="Добавить транспорт", callback=vehicle_form)  # Добавляем кнопку "Добавить транспорт" с вызовом функции show_vehicle_form
                dpg.add_button(label="Распределить грузы", callback=optimize_cargo)  # Добавляем кнопку "Распределить грузы" с вызовом функции optimize_cargo_distribution
                dpg.add_button(label="Показать все транспортные средства", callback=show_vehicles)  # Добавляем кнопку "Показать все транспортные средства" с вызовом функции show_all_vehicles
                dpg.add_button(label="Показать результат распределения", callback=distribute_cargo_results)  # Добавляем кнопку "Показать результат распределения" с вызовом функции distribute_cargo_results
                dpg.add_button(label="Экспортировать результат", callback=json_load)  # Добавляем кнопку "Экспортировать результат" с вызовом функции export_results

        dpg.add_text("", tag="status" , color=[0, 255, 0]) # Добавляем текстовый элемент с тегом "status"

# Запуск приложения
dpg.create_context()
fonts()
main_topic()

# Настройка обработчиков клавиш
keyboard()

dpg.create_viewport(title="TC", width=1500, height=1000)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
