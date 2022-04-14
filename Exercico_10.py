"""
Autor: Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Um cinema cobra preços diferentes para os ingressos conforme a idade de uma pessoa.
Se a pessoa tiver:

menos de 3 anos, o ingresso será gratuito;
se tiver entre 3 e 12 anos, o ingresso custará R$ 15,00
se tiver mais de 12 anos, custará R$ 30,00

Escreva um laço em que você pergunte a uda de ais usuários e, então, informe-lhes o preço do ingresso do cinema

Encerre o laço usando um break quando o usuário digitar sair

Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total de dinheiro arrecadado
e a média de idades das pessoas

"""

total = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade? ')
    if idade == 'sair':
        break
    idadee = int(idade)
    total += 1

    if idadee < 3:
        ingresso = 0

    else:
        if idadee > 12:
            ingresso = 30

        else:
            ingresso = 15
    dinheiro += ingresso

media = idadee / total

print('Total de pessoas: {}'.format(total))
print('Total de arrecadados R$ {}: '.format(dinheiro))
print('Media de idade das pessoas: {}'.format(media))