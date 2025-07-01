"""
Escreva um algoritmo em Python em que o usuário escolhe se quer comprar
maças, laranjas ou bananas. Deverá ser apresentado na tela um menu com as
opções: 1 para maçã, 2 para laranja e 3 para banana.

Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.

Considere que uma maçã custa R$2,30, uma laranja R$ 3,60 e uma banana R$1,85
"""

preco = ("opcao 1": 2,30)

total = quantidade * preco


print("1 - Maçã", "2 - Laranja", "3 - Banana")

frutas = ["maçã", "laranja", "banana"]

opcao = input(f"Escolha sua fruta entre {frutas}")

quantidade = input("Qual a quantidade ? ")

if opcao == "1":
    print(f"Você escolheu {quantidade} Maça!")
elif opcao == "2":
    print(f"Você escolheu {quantidade} Laranja!")
else:
    print(f"Você escolheu {quantidade} Banana!")

print(f"O total da sua compra é {total}")
