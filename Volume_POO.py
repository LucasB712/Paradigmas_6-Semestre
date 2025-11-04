class Esfera:
    def __init__(self, pi, r):
        self.pi = pi
        self.r = r
    
    def volume(self):
        volume = 4 * self.pi * self.r * self.r  * self.r  * self.r / 3
        print(volume)

class Piramide:
    def __init__(self, area_base, h):
        self.area_base = area_base
        self.h = h
    
    def volume(self):
        volume = self.area_base * self.h / 3
        print(volume)


class Cilindro:
    def __init__(self, pi, r, h):
        self.pi = pi
        self.r = r
        self.h = h
    
    def volume(self):
        volume = self.pi * self.r * self.r  * self.h
        print(volume)
        
e = Esfera(3.14, 10)
p = Piramide(10, 15)
c = Cilindro(3.14, 15, 10)

e.volume()
p.volume()
c.volume()
