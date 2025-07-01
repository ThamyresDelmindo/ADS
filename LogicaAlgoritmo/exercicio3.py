"""
Crie uma variável de string que receba uma frase qualquer. 
Crie uma segunda variável, agora contendo a metade da string digitada.
Imprimpa na tela somente os dois últimos caracteres da segunda variável do tipo string. 
"""

frase = input("Digite uma frase qualquer: ")
tam = len(frase)
meia_frase = frase[:int(tam/2)]

print(meia_frase[-2:])