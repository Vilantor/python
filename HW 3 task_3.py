def my_func(arg_1, arg_2, arg_3):
    arg_1 == arg_2 == arg_3
    if arg_1 < arg_2 and arg_1 < arg_3:
        return arg_2 + arg_3
    elif arg_2 < arg_1 and arg_2 < arg_3:
        return arg_1 + arg_3
    elif arg_3 < arg_1 and arg_3 < arg_2:
        return arg_1 + arg_2
    return arg_1, arg_2, arg_3

print(my_func(20,10,30))
print(my_func(10,20,30))
print(my_func(30,20,10))

