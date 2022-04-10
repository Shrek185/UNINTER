"""
Autor : Douglas Nascimento (Shrek18.5)
Obs:    Curso Python #04 - Primeiros comandos em Python3 - Curso em Video Gustavo Guanabara
        Video base para o curso de ADS (EAD) Uninter 2022

https://www.youtube.com/watch?v=31llNGKWDdo&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=4
"""
# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

nome = input("Qual seu nome?")
print("Seja bem vindo", nome, "! Prazer em te conhecer")

# Crie um script Python que leia o dia, mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data fonrmatada.

dia = int(input("Que dia vc nasceu?"))
mes = int(input("Que mês vc nasceu?"))
ano = int(input("Que mês vc nasceu?"))
print('Você nasceu no dia' , dia , "/", mes , "/", ano, ".Correto" , nome, "?")

#Crie um Script Python que leia dois numeros e tente mostrar a soma entre eles.

anos = int(input('Vamos brincar? Vou adivinhar a sua idade agora! Em que ano você está vendo este script?'))
print('Você tem ', anos - ano, 'anos! Acertei?')
res = input('Responta sim ou nao: ')
if res == 'sim':
    print('KKKKKKK')
else:
    print('Tem certeza? Que estranho meu humano me programou para acertar!')
