num = int(input('Digite um número inteiro de 0 á 9999: '))
u = num // 1 % 10
d = num // 10 % 10
r = num // 100 % 10
s = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {r}')
print(f'Milhar: {s}')