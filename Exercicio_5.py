"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Faça um algoritmo que receba trê Valores representando os lados de um triângulo fornecidos pelo usuário.
Verifique se os valores formam um triângulo e classifique como:

a) Equilátero (três lados iguais)
b) Isósceles (dis lados iguais)
c) Escaleno (três lados diferentes)

Lembre-se de que, para forma um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser
maior que a soma dos outros dois.

"""
A = int(input('Digite o primeiro lado do triângulo: '))
B = int(input('Digite o segundo lado do triângulo: '))
C = int(input('Digite o terceiro lado do triângulo: '))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):

    # Se você chegou até aqui, é porque o triângulo é válido.
        if (A != B) and (A != C) and (B != C):
            print('Triângulo escaleno!')
        else:
            if A == B and A == C and B == C:
                print("Triângulo equilátero!")
            else:
                print('Triângulo isósceles!')
    else:
        print("Ao menos um dos valores indicado não servem para formar um triângulo")

else:
    print("Ao menos um dos valores indicado não servem para formar um triângulo")
