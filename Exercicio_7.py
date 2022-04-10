"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022

Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação:

R para residências;
I para indústria
C para comércio

  *********************************************
  * Preço por tipo e faixa de consumo         *
  * *******************************************
  * Tipo        * Faixa (kWh)    * Preço (R$) *
  *********************************************
  *             * Até 500        * 0,40       *
  * Residencial *******************************
  *             * Acima de 500   * 0,65       *
  *********************************************
  *             * Até 1000       * 0,55       *
  * Comercial   *******************************
  *             * Acima 1000     * 0,60       *
  *********************************************
  *             *  Até 5000      * 0,55       *
  * Industrial  *******************************
  *             * Acima de 5000  *  0,60      *
  *********************************************

"""
kWh = float(input('Quanto kWh?'))
tipo = input('Qual o tipo de instalação (R, C ou I)')

if (tipo == "R"):
    if kWh <= 500:
        preco = 0.4
    else:
        preco = 0.65

elif (tipo == 'C'):
    if kWh <= 1000:
        preco = 0.55
    else:
        preco = 0.60

elif (tipo == 'I'):
    if kWh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Instalação inválida!')

print('Total a pagar: R$ {}'.format(preco * kWh))