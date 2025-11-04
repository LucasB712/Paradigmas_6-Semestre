
def volume_esfera(pi, r):
        volume = 4 * pi * r * r  * r  * r / 3
        print(volume)

def volume_piramide(area_base, h):
        volume = area_base * h / 3
        print(volume)

def volume_cilindro(pi, r, h):
        volume = pi * r * r  * h
        print(volume)
        
e = volume_esfera(3.14, 10)
p = volume_piramide(10, 15)
c = volume_cilindro(3.14, 15, 10)

print(e)
print(p)
print(c)
