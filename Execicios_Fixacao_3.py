# Execute as seguintes atribuiçoes

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# Agora, utilizando operadores + e *, crie as saidas a seguir

# a) 'ant bat cod'
print(s1 + ' ' + s2 + ' ' + s3)

#  b) 'ant ant ant ant ant ant ant ant ant ant'
print(10 * (s1 + ' '))

#  c) 'ant bat bat cod cod cod'
print(s1 + ' ' + 2 * (s2 + ' ') + 3 * (s3 + ' '))

#  d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print(7 * (s1 + ' ' + s2 + ' '))

#  e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
print(5 * (2 * s2 + s3 + ' '))