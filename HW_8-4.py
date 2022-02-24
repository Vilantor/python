class Store:
    storage = {'printer': 11, 'scaner': 20, 'xerox': 13}  # Количество техники на складе


class OfficeEquipments:
    ethernet = bool  # Наличие LAN-порта
    wireless = bool  # Наличие возможности беспроводного подключения


class Printer(OfficeEquipments):
    color = bool  # Цветной / монохромный
    connection = str  # Вид подключения
    numbprint = 3  # Количество выданных принтеров

    def PickupStoragePrint(self, numbprint):
        key = int(input('Введите количество принтеров, которое хотите передать на склад: '))
        numbprint -= key
        Store.storage.get(print(-key))

    def PutStoragePrint(self, numbprint):
        key = int(input('Введите количество принтеров, которое хотите забрать со склада: '))
        numbprint += key
        Store.storage.get(print(+ key))


class Scaner(OfficeEquipments):
    automaticfeeder = bool  # Наличие автоподатчика
    numbscan = 3

    def PickupStorageScan(self, numbprint):
        key = int(input('Введите количество сканеров, которое хотите передать на склад: '))
        numbprint -= key
        Store.storage.get(print(-key))

    def PutStoragePrint(self, numbprint):
        key = int(input('Введите количество сканеров, которое хотите забрать со склада: '))
        numbprint += key
        Store.storage.get(print(+ key))


class xerox(OfficeEquipments):
    functional = str  # Размер печати: Стандарт (А3 - А4), Специальный (издательство), Широкоформатный (чертежи)
    numbxerox = 3

    def PickupStorageXerox(self, numbprint):
        key = int(input('Введите количество ксероксов, которое хотите передать на склад: '))
        numbprint -= key
        Store.storage.get(print(-key))

    def PutStorageXerox(self, numbprint):
        key = int(input('Введите количество ксероксов, которое хотите забрать со склада: '))
        numbprint += key
        Store.storage.get(print(+ key))