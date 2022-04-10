""""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Desenvolva um algoritimo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
Calcule e exiba o valor do desconto e o preço final do produto (exercício da apostila - aula2)

""""

preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percenteual de desconto (0-100)%: '))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é R$ {}. Desconto sera de {}%'.format(preco, p))
print('O valor calculado do desconto: R$ {}. Valor final do produto: R$ {}'.format(desconto, final))