velo = float(input('Qual é a velocidade atual do seu carro: '))
if velo > 80:
    multa = (velo - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('NÃO FOI MULTADO!')
print('Tenha um bom dia! Dirija com segurança!')