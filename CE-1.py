# 1
import math

x1 = math.factorial(30)
x2 = math.factorial(40)
x3 = math.factorial(50)

# 2
grausCelsius = float(input())  

grausFahrenheit = ((grausCelsius * 1.8) + 32)

# 3
a = float(input())   # terei de fazer alguma conversão de valores?
b = float(input())
c = float(input())

print('{:0.3f}'.format((a**2 - b**2 - c**2)/ (-2*b * c)))

# 4
import math

h = float(input())
r = float(input())

volumeCilindro = ((math.pi * r**2) * h)
volumeCone = ((math.pi * r**2) * h / 3)
ratio = (volumeCilindro + volumeCone)

print('{:0.4f}'.format(volumeCilindro))
print('{:0.4f}'.format(volumeCone))
print('{:0.4f}'.format(volumeCilindro/volumeCone))