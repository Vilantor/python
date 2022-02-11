import time

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        n = 0                                           # просто решил сделать условия завершения цикла
        while n < 20:
            self.TrafficLight__color = [0]
            print('Красный!')
            time.sleep(7)
            n += 1
            self.TrafficLight__color = [1]
            print('Жёлтый!')
            time.sleep(2)
            n += 1
            self.TrafficLight__color = [2]
            print('Зеленый!')
            time.sleep(6)
            n += 1
        else:
            print('Работа светофора окончена... =(')

a = TrafficLight()

print(a.running())

