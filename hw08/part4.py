from abc import ABC, abstractmethod


class OfficeEquipment:
    def __init__(self, name, model, volume):
        self.name, self.model, self.volume = name, model, 0
        if type(volume) is int and volume > 0:
            self.volume = volume
        else:
            raise ValueError(f"Некорректное значение занимаемого объема: {volume}")

    def __str__(self):
        return f"{type(self)}: name = {self.name}; model = {self.model}; volume = {self.volume}"


class Printer(OfficeEquipment):
    def __init__(self, name, model, volume, cartridge):
        super().__init__(name, model, volume)
        self.cartridge = cartridge

    def __str__(self):
        return f"{super().__str__()}; cartridge = {self.cartridge}"


class Scanner(OfficeEquipment):
    def __init__(self, name, model, volume, resolution):
        super().__init__(name, model, volume)
        self.resolution = resolution

    def __str__(self):
        return f"{super().__str__()}; resolution = {self.resolution}"


class Xerox(OfficeEquipment):
    def __init__(self, name, model, volume, cartridge, resolution):
        super().__init__(name, model, volume)
        self.cartridge = cartridge
        self.resolution = resolution

    def __str__(self):
        return f"{super().__str__()}; cartridge = {self.cartridge}; resolution = {self.resolution}"


class InventoryOperationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Inventory:
    def __init__(self, name, volume, location):
        self.name = name
        if type(volume) is int and volume > 0:
            self.total_volume = volume
        else:
            raise ValueError(f"Некорректное значение доступного пространства: {volume}")
        self.location = location
        self.current_volume = 0
        self.items = {}

    @property
    def available_volume(self):
        return self.total_volume - self.current_volume

    def __str__(self):
        storage = ""
        for key in self.items.keys():
            storage += f"\t{key}:\n" + "\n".join([f"\t\t{x}" for x in self.items[key]]) + "\n"
        return f"""Склад {self.name}, расположенный в {self.location}. 
        Максимальный объем {self.total_volume}. 
        Доступный объем {self.available_volume}.
        Занятый объем {self.current_volume}.
        Текущие содержание:\n{storage}"""

    def add_item(self, new_item):
        if isinstance(new_item, OfficeEquipment) and self.available_volume - new_item.volume > 0:
            current_items = self.items.get(type(new_item), [])
            current_items.append(new_item)
            self.items[type(new_item)] = current_items
            self.current_volume += new_item.volume
        else:
            raise InventoryOperationError("Невозможно добавить новое оборудование.")

    def remove_item(self, type_item):
        current_items = self.items.get(type_item, [])
        if len(current_items) > 0:
            removed = current_items.pop()
            if len(current_items) == 0:
                self.items.pop(type_item)
            else:
                self.items[type_item] = current_items
            return removed
        raise InventoryOperationError(f"Оборудование вида {type_item} на складе не найдено.")


class EquipmentReceiver(ABC):
    @abstractmethod
    def add_equipments(self, equipments):
        pass

    def _validate_equipments(self, equipments):
        if len(equipments) < 1:
            raise InventoryOperationError("Некорректный формат запроса на добавление оборудования")
        if type(equipments) == list or type(equipments) == tuple:
            self.__validate_list_equipments(equipments)
        elif type(equipments) == dict:
            for key in equipments.keys():
                if not issubclass(key, OfficeEquipment):
                    raise InventoryOperationError("Некорректный формат запроса на добавление оборудования")
                if type(equipments[key]) == list or type(equipments[key]) == tuple:
                    self.__validate_list_equipments(equipments[key], key)
                elif not isinstance(equipments[key], OfficeEquipment):
                    raise InventoryOperationError("Некорректный формат запроса на добавление оборудования")
        elif not isinstance(equipments, OfficeEquipment):
            raise InventoryOperationError("Некорректный формат запроса на добавление оборудования")

    @staticmethod
    def __validate_list_equipments(equipments, equipment_type=None):
        for equipment in equipments:
            if equipment_type is None:
                equipment_type = type(equipment)
            elif equipment_type != type(equipment):
                raise InventoryOperationError("Некорректный формат запроса на добавление оборудования")


class Department(EquipmentReceiver, ABC):
    def add_equipments(self, equipments):
        self._validate_equipments(equipments)
        equipments_print = "Полученное оборудование: "
        if type(equipments) == dict:
            for key in equipments.keys():
                equipments_print += "\t" + str(key) + ": [" + "|".join([str(x) for x in equipments[key]]) + "]\n"
        elif type(equipments) == tuple or type(equipments) == list:
            equipments += "\t[" + "|".join([str(x) for x in equipments]) + "]\n"
        else:
            equipments_print += str(equipments)
        print(equipments_print)


class InventoryManager(EquipmentReceiver, ABC):
    def __init__(self, inventory):
        if type(inventory) != Inventory:
            raise ValueError(f"Ожидался объект типа Inventory, но получен объект типа {type(inventory)}")
        self.inventory = inventory

    def add_equipments(self, equipments):
        self._validate_equipments(equipments)
        if type(equipments) == dict:
            for key in equipments.keys():
                if type(equipments[key]) == list or type(equipments[key]) == tuple:
                    for equipment in equipments[key]:
                        self.inventory.add_item(equipment)
                else:
                    self.inventory.add_item(equipments[key])
        elif type(equipments) == list or type(equipments) == tuple:
            for equipment in equipments:
                self.inventory.add_item(equipment)
        else:
            self.inventory.add_item(equipments)

    def transfer_equipments(self, required_equipments, department):
        if not isinstance(department, Department):
            raise ValueError(f"Некорректный тип департамента")
        self.__validate_transfer_equipments(required_equipments)
        equipments_for_transfer = {}
        for key in required_equipments.keys():
            equipments_for_transfer[key] = []
            for i in range(required_equipments[key]):
                equipments_for_transfer[key].append(self.inventory.remove_item(key))
        department.add_equipments(equipments_for_transfer)

    @staticmethod
    def __validate_transfer_equipments(required_equipments):
        if type(required_equipments) != dict or len(required_equipments) == 0:
            raise ValueError(f"Некорректный формат запроса оборудования")
        for key in required_equipments.keys():
            if not issubclass(key, OfficeEquipment):
                raise ValueError(f"Некорректный формат запроса оборудования")
            if type(required_equipments[key]) != int or required_equipments[key] < 0:
                raise ValueError(f"Некорректный формат запроса оборудования")


current_inventory = Inventory("Хранилище №42", 2000, "Москва")
print(current_inventory)
current_inventory.add_item(Printer("Xerox", "RKD-2313", 1, "LDE-231"))
current_inventory.add_item(Scanner("LG", "LSIRLS-2568", 4, "2000x300"))
print(current_inventory)
removed_eq = current_inventory.remove_item(Scanner)
print(current_inventory)
print(removed_eq)
current_inventory = Inventory("Хранилище №42", 2000, "Москва")
manager = InventoryManager(current_inventory)
manager.add_equipments((Printer("Xerox", "RKD-2313", 1, "LDE-231"), Printer("Xerox", "RKD-2314", 1, "LDE-232")))
print(current_inventory)
manager.add_equipments(
    {Printer: [Printer("Xerox", "RKD-2314", 1, "LDE-232")], Scanner: Scanner("LG", "LSIRLS-2568", 4, "2000x300")})
print(current_inventory)
manager.transfer_equipments({Scanner: 1, Printer: 2}, Department())
print(current_inventory)
