import random

class Car:
    speed = int
    color = str
    name = str
    is_police = bool

    def go(self):
          print('Машина завелась и начала движение')

    def stop(self):
        print('Машина остановилась')

    def turn(self, left, right):
        if turn == left(self):
            print('Машина повернула влево')
        elif turn == right(self):
            print('Машина повернула направо')

    def show_speed(self):
        speed = random.randrange(1, 120, 1)
        print(f'В данный момент скорость автомобиля: {speed} км/ч')

a = Car()
print(a.show_speed())

class TownCar(Car):
    def show_speed(self):
        speed = random.randrange(1, 120, 1)
        if speed > 60:
            print(f'Внимание! Скорость TownCar составляет {speed} км/ч. Превышение скорости!')
        else:
            print(f'В данный момент скорость TownCar: {speed} км/ч')

tc = TownCar()
print(tc.show_speed())

class WorkCar(Car):
    def show_speed(self):
        speed = random.randrange(1, 100, 1)
        if speed > 40:
            print(f'Внимание! Скорость WorkCar составляет {speed} км/ч. Превышение скорости!')
        else:
            print(f'В данный момент скорость WorkCar: {speed} км/ч')

wc = WorkCar()
print(wc.show_speed())