# x - действительное положительное
# y - целое отрицательное

# Первое решение через **

def my_func(x, y):
    return x**y
print(my_func(2.15, -5))

# Второе решение через цикл...

def my_func(x, y):
    while y < -1:
        y = y + 1
        x = 1 / (x * x)
    return x

print(my_func(5, -2))