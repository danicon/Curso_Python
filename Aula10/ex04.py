from random import randint
from time import sleep

pc = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-'*20)
usuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if usuario == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {pc} e não no {usuario}!')