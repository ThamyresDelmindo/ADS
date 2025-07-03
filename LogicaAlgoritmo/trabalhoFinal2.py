"""
QUESTÃO 2 de 4 - Conteúdo até aula 04
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas
para uma loja que vende Marmitas de Bife Acebolado ou Filé de Frango. 
Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:
•	Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;
•	Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;
•	Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais;

Elabore um programa em Python que: 
A.	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome (somente print, não usar input aqui). ok
Além do seu nome e sobrenome, deve-se implementar um print com um Menu para o cliente. [EXIGÊNCIA DE CÓDIGO 1 de 8];
B.	Deve-se implementar o input do sabor (BA/FF) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de BA e FF [EXIGÊNCIA DE CÓDIGO 2 de 8];
C.	Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
D.	Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];
E.	Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
F.	Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
G.	Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
H.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];

Teste seu código atendendo as seguintes exigências:
I.	Deve-se apresentar na saída de console uma mensagem com o seu nome completo e o menu para o cliente conhecer as opções [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
J.	Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
K.	Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
L.	Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];  
"""

app = "Marmitar"

print(f"Seja bem vindo(a) ao {app.upper()} by Thamyres Delmindo")

print("Segue abaixo nosso Menu...")



while True:
    sabores = input("Digite 'BA' para escolher Bife Acebolado ou 'FF' para escolher Filé de Frango").upper()
    if sabores == "BA":
        sabor_escolhido = "Bife Acebolado"
        print(f"Você escolheu {sabor_escolhido}")
        break
    elif sabores == "FF":
        sabor_escolhido = "Filé de Frango"
        print(f"Você escolheu {sabor_escolhido}")
        break
    else:
        print("Opção inválida. Tente novamente digitando BA ou FF")


continue
tamanho = input("Digite 'P', 'M' ou 'G' para escolher entre os tamanhos Pequeno, Médio e Grande").upper()
if tamanho == "P":
    tamanho_escolhido = "Pequeno"
elif tamanho == "M":
    tamanho_escolhido = "Médio"
elif tamanho == "G":
    tamanho_escolhido = "Grande"
    print(f"Você escolheu {sabor_escolhido} tamanho {tamanho_escolhido}!")
else:
    print("Opção inválida. Tente novamente digitando P, M ou G.")
if sabor_escolhido == "BA" and tamanho_escolhido == "P":
    preco = 16.00
if sabor_escolhido == "BA" and tamanho_escolhido == "M":
    preco = 18.00
if sabor_escolhido == "BA" and tamanho_escolhido == "G":
    preco = 22.00
if sabor_escolhido == "FF" and tamanho_escolhido == "P":
    preco = 15.00
if sabor_escolhido == "FF" and tamanho_escolhido == "M":
    preco = 17.00
if sabor_escolhido == "FF" and tamanho_escolhido == "G":
    preco = 21.00

print(f"Seu pedido de {sabor_escolhido} tamanho {tamanho_escolhido} ficou no valor total de {preco}")




# while True:
#     print()
#     print("\nCARDÁPIO MARMITAR")
#     print()
#     print("1 - Ver todas os pratos")
#     print("2 - Adicionar uma fruta")
#     print("3 - Remover uma fruta")
#     print("4 - Verificar se uma fruta está na feira")
#     print("5 - Mostrar quantas frutas tem na feira")
#     print("6 - Mostrar a lista completa da feira")
#     print("7 - Sair do programa")
#     print("🍑" * 20)
#     break




