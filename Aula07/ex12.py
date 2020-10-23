alu = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
cust = (alu * 60) + (km * 0.15)
print(f'O total a pagar é de R${cust:.2f}')