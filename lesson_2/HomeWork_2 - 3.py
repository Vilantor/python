# Через словарь:
# vremena = {12: 'Zima', 1: 'Zima', 2: 'Zima', 3: 'Vesna', 4: 'Vesna', 5: 'Vesna', 6: 'Leto', 7: 'Leto', 8: 'Leto', 9: 'Osen', 10: 'Osen', 11: 'Osen'}
# time = int(input('Введите номер месяца: '))
#
# print(vremena.get(time))

# Через список:
vremena = ['Zima', 'Zima', 'Vesna', 'Vesna', 'Vesna', 'Leto', 'Leto', 'Leto', 'Osen', 'Osen', 'Osen', 'Zima']
month = int(input('Введите номер месяца: '))

print(vremena[month-1])
