def division (arg_1, arg_2):
    if arg_2 != 0:
        return arg_1 / arg_2
    else:
        print('На ноль делить нельзя!')

print(division(arg_1=int(input('Введите первое число: ')), arg_2=int(input('Введите второе число: '))))