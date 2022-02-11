class Worker:
    name = "Ярослав"
    surname = "Папаев"
    position = 'Менеджер'
    _income = {"wage": 30000, "bonus": 10000}

    def position(self):
        get_total_income = sum(Worker._income.values())
        get_full_name = print(f"Имя: {self.name}, Фамилия: {self.surname}, Общий доход: {get_total_income}")

a = Worker()

print(a.position())