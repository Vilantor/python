class Date:

    @classmethod
    def date(cls):
        day = num[:2]
        month = num[3:5]
        year = num[6:10]
        data = [day, month, year]

        return data

    @staticmethod
    def date():
        day = d.num[:2]
        month = d.num[3:5]
        year = d.num[6:10]
        data = [day, month, year]
        return data


d = Date()
num = str(input('Введите дату в формате "дд-мм-гггг": '))

print(d.date())
print(Date.date(12-05-2022))
