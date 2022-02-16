class Clothes:
    V = float
    H = float


class Coat(Clothes):

    def __init__(self, mat):
        self.mat = mat

    @property
    def material(self):
        self.mat = V / 6.5 + 0.5
        return self.mat


V = 50
c = Coat(mat=1)

print(c.material)


class Suit(Clothes):

    def __init__(self, mat):
        self.mat = mat

    @property
    def material(self):
        self.mat = float(2 * H + 0.3)
        return self.mat


H = 1.89
s = Suit(mat=1)

print(s.material)
