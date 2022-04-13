"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Traduza as afirmações a seguir para condicionais em Python:

a) Se ano é divisível por 4, escreva: "Pode ser um ano bissexto".
    Caso contrário, escreva: "Definitivamente não é ium ano bissexto"

**********************************************************************************************************
* Bissexto - Um ano é bissexto se ele for divisível por 400 ou se ele for divisível por 4 e não por 100. *
**********************************************************************************************************

b) Se ambas as variáveios booleanas cima e baixo forem True, escreva: "Decida-se",
    caso contrário, escreva: "Você escolheu um caminho!"

"""

ano = int(input('Digite o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é bissexto')



cima = input('Para CIMA ou para BAIXO: ')
baixo = input('Para CIMA ou para BAIXO: ')

if cima == 'CIMA' and baixo == 'BAIXO':
    print('DECIDA-SE!')
else:
    print('Você escolheu um caminho')
