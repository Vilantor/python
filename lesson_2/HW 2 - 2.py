spisok = input("Введите элементы списка, которые хотите добавить: ").split()

for i in range(0, len(spisok)-1, 2):
    spisok[i], spisok[i+1] = spisok[i+1], spisok[i]

print(spisok)
