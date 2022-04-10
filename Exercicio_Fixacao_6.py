""""
Condicional Simples

Traduza as afimaçòes a seguir para condicionais em Python

a) Se idade é maior que 60, escreva: "Voce trem direitos aos benefícios"

b) Se dano é maior que 10 escudo é igual a 0, escreva: "Vocês está morto"

C) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em true, escreva: "Você escapou"
"""


idade = int(input("Qual a sua idade (0-100)? "))
if idade >= 60:
    print('*** Voce tem direitos aos benefícios! ***')
else:
    print('*** Você é jovem ainda! ***')

dano = int(input('Qual o valor do dano (até 10)'))
escudo = int(input('Qual o valor do seu escudo(entre 0 e 10)'))
if escudo == 0 and dano <= 10:
    print('Vocês está morto!')
else:
    print('Fuja para montanhas!')


lado: str = input('Para qual lado você vai? ')

if (lado == 'norte' or 'sul' or 'leste' or 'oeste'):
    print('Você Escapou!!')
