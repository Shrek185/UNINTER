"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Escreva um program que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como o quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$ 60,00 por dia e R$ 0,15 por km rodado.
"""

km = int(input('Quantos Km forma percorridos? '))
dias = int(input('Por quantos dias ele foi alugado? '))

preco = 60 * dias + 0.15 * km

print('Km = {}. Dias {}'.format(km, dias))
print('Valor a ser pago é de R$ {}'.format(preco))