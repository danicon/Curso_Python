viag = float(input('Distância da sua viagem: '))
if viag <= 200:
    tot = viag * 0.50
else:
    tot = viag * 0.45
print(f'O valor final da sua passagem é: R${tot:.2f}')