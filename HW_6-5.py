class Stationary:
    title = str

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):

    def draw(self):
        print(f'Запуск отрисовки ручкой')

p = Pen()
print(p.draw())

class Handle(Stationary):

    def draw(self):
        print(f'Запуск отрисовки маркером')

h = Handle()
print(h.draw())