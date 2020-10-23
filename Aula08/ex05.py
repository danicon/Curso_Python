from math import hypot
co = float(input('Digiteo o valor do cateto oposto: '))
ca = float(input('Digiteo o valor do cateto adjacente: '))
pit = hypot(co,ca)
print(f'A hipotenusa vai medir {pit:.2f}')