class Complexnum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complexnum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complexnum(self.re * other.re, self.im * other.im)


c = Complexnum(1, 2)

print()
