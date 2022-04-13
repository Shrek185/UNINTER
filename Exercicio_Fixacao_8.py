"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

WHILE x FOR

Realize a sequência de print com for e while:

a) Inteiro de 3 até 12, com 12 incluso

b) Inteiro de 0 até 9, excluindo 9, com passo de 2

"""
x = 3
while (x <=12):
    print('Usando while: ', x)

    x=x+1

for i in range(3,13,1):

    print('Usando for: ', i)

x = 0
while (x <9):
    print('Usando while: ', x)

    x=x+2

for i in range(0,9,2):

    print('Usando for: ', i)