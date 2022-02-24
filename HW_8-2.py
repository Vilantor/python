class MyException(Exception):
    a = int(input('Введите делимое:'))
    b = int(input('Введите делитель НЕ равный нулю!: '))

    try:
        if b != 0:
            print(a / b)
        else:
            print('Вы ввели делитель равный нулю! На ноль делить нельзя!')
    except ZeroDivisionError:
        print('Вы ввели делитель равный нулю! На ноль делить нельзя!')
