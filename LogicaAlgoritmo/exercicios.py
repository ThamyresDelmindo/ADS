
#Lógica
# a) O somatório dos 5 primeiros números inteiros e positivos
#b) A média entre 23, 19 e 31
#c) O número de vezes que 73 cabe em 403
#d) A sobra quando 403 é divido por 73
#e) 2 elevado à 10 potência
#f) O valor absoluto da diferença entre 54 e 57
#g) O menor valor entre 34, 29 e 31 

print(1 + 2 + 3 + 4 + 5)
print((23 + 19 + 31) //3) 
print(403 // 73)  #// as duas barras da uma parte inteira ao invés de fracionar
print(403 % 73)
print(2 ** 10)
print(abs(54 - 57))
print(min(34, 29, 31))

#Atribuição

# a) Atribuir o valor inteiro 3 à variável a 
# b) Atribuir o valor 4 à variável b
# c) atribuir à variável c o valor da expressão a*a + b *b

a = 3
b = 4
c = a*a + b *b
print(a, b, c)

#Strings
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

exea = s1 + ' ' + s2 + ' ' + s3 + ' '
exeb = 10 * (s1 + ' ')
exec = (s1 + ' ') + 2 * (s2 + ' ') + 3 * (s3 + ' ')
exed = (s1 + ' ' + s2 + ' ' + s1 + ' ' + s2 + ' ') *3
exee = (s2+s2+s3 + ' ') *5
print(exea)
print(exeb)
print(exec)
print(exed)
print(exee)


