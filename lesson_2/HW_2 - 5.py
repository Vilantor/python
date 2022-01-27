my_list = [7, 5, 3, 3, 2, 0]
a = int(input('Введите любое натуральное число: '))
if a >= my_list[0]:
    my_list.insert(0, a)
elif a >= my_list[1]:
    my_list.insert(1, a)
elif a >= my_list[2]:
    my_list.insert(2, a)
elif a >= my_list[3]:
    my_list.insert(3, a)
elif a >= my_list[4]:
    my_list.insert(4, a)
elif a >= my_list[5]:
    my_list.insert(5, a)

print(my_list)
