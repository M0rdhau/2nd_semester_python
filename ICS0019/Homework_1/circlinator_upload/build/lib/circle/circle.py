from math import pi

def circlinate(radius):
    circumference = 2 * radius * pi
    area = pi * (radius ** 2)
    return (area, circumference)