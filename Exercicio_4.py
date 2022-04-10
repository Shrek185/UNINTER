""""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Desenvolva um programa que lê dois valores numéricos inteiros e compara se o primeiro é maior que o segundo,
que o primeiro valor digitado é maior que o segundo.
Utilizando uma condicional simples. Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando
""""

# Lê dois valores interiors e compara ambos.

x = int(input('Digite um valor inteiro: '))

y = int(input('Digite um segundo valor inteiro: '))

if(x > y):
    print('O primeiro valor é maior que o segundo!')
else:
    print('O Segundo valor é maior que o primeiro')
