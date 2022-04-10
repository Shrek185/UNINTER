""""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Escreva as seguintes expressões booleanas em linguagem Python:

a) 1387 é divisível por 19

b) 31 é par

c) o menor valor entre: 34, 29 e 31 é menor do que 30

"""

if ( 1387 % 2) == 0:
    print( '1387 é divisível por 19')
else:
    print('1387 não é divisível por 19')

if ( 31 % 2) == 0:
    print( '31 é par')
else:
    print('31 é impar' )

valor = min(34, 29, 31)
if (valor < 30):
    print('{} é menor 30'.format(valor))
else:
    print('{} é maior 30'.format(valor))
