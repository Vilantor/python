def fact():
    factorial = 0
    n = int(input('Введите число, факториал которого хотите найти: '))
    while n <= 0:
        factorial += n * (n - 1)
        n -= 1
    yield fact()

print(fact(n))