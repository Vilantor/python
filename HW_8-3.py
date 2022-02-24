# class Exept(Exception):
#     pass
#
#     def expt(self):
#         sp = []
#         a = input('Введите число для добавления в список: ')
#         while a != 'stop' and a == int():
#             sp.append(a)
#         else:
#             print('Введено не число!')
#             return sp
#
#
# e = Exept()
#
# print(e.expt())


class Exept(Exception):

    try:
        a = int(input('Введите число для добавления в список: '))
        sp = []
        sp.append(a)
        for a in sp:
            if a == int:
                sp.append(a)
            elif a == 'stop':
                break
    except ValueError:
        print('Введено не число!')





