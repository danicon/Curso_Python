sal = float(input('Digite o seu salário: '))
if sal > 1250:
    aum = sal * 1.10
else:
    aum = sal * 1.15
print(f'O seu novo salário é: {aum}')