"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Escreva um Algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
Adição (+);
Subtração (-);
Multiplicação (*);
Divisão (/).
e sair
Exiba na tela o resultado da operação desejada.
Repita até que a opção saída seja escolhida

"""

print('Calculadora ADS 2022')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':

    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

while (op != 's'):

    if (op == '+'):

        res = x + y

        print('Resultado: {} + {} = {}'.format(x, y, res))

    elif (op == '-'):

        res = x - y

        print('Resultado: {} - {} = {}'.format(x, y, res))

    elif (op == '*'):

        res = x * y

        print('Resultado: {} * {} = {}'.format(x, y, res))

    elif (op == '/'):

        res = x / y

        print('Resultado: {} / {} = {}'.format(x, y, res))

    else:
        print("Operação inválida!")

    op = input('Qual operação deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':

        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

print('Encerramendo o programa...')