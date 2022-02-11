class Road:
    _lenght = int(input('Введите длину: '))
    _width = int(input('Введите ширину: '))

    def area_calc(self):
        onemeter = int(25)
        thickness = int(5)
        area = int((self._width * self._lenght * onemeter * thickness)/1000)
        return area

a = Road()

print(f'Для покрытия всей дороги необходимо {a.area_calc()} тонн асфальта')