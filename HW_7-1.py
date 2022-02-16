class Matrix:

    def __init__(self, a):
        a = [[1, 2, 5], [6, 2, 6]]
        self.a = a
        b = [[5, 7, 1], [5, 7, 8]]
        self.b = b

    def __str__(self):
        a = [[1, 2, 5], [6, 2, 6]]
        print(f'{a}')

    def __add__(self):
        for i in range(len(a)):
            for j in range(len(a[0])):
                [i][j] + b[i][j]


rec = Matrix(a=1)               # Почему указываю "а" равную любму числу и код работает, но изменений нет,
                                # а если указываю просто "а", то "а" не определяется...

a = [[1, 2, 5], [6, 2, 6]]
b = [[5, 7, 1], [5, 7, 8]]

print('Матрица А:\n', *rec.a, sep='\n')
print('Матрица B:\n', *rec.b, sep='\n')

print(rec.a.__add__(rec.b))    # Выводится не совсем та сумма, которую хотелось бы...
print(rec.a + rec.b)



