app = "Marmitar"

print(f"\nSeja bem vindo(a) ao {app.upper()} by Thamyres Delmindo\n")
print("Segue abaixo nosso Menu...\n")
print("=" * 59)
print("|" + "CARDÁPIO MARMITAR".center(55) + "|".center(5)) #Desenho do cardápio
print("=" * 59)
print("|" + "Tamanho".center(13) + "|" + "Bife Acebolado (BA)".center(21) + "|" + "Filé de Frango (FF)".center(21) + "|")
print("|" + "P".center(13) + "|" + "R$ 16,00".center(21) + "|" + "R$ 15,00".center(21) + "|")
print("|" + "M".center(13) + "|" + "R$ 18,00".center(21) + "|" + "R$ 17,00".center(21) + "|")
print("|" + "G".center(13) + "|" + "R$ 22,00".center(21) + "|" + "R$ 21,00".center(21) + "|")
print("=" * 59)

pedidos = [] #Definindo uma variável de lista vazia pra conseguir imprimir todos os pedidos no final do código
total = 0.0 #Definindo a variável antes para o Python conseguir calcular
encerrar = False #Tive que colocar isso porque não estava conseguindo concluir o loop do 'algo_mais'

print("Gostou das opções? Então vamos começar o seu pedido...\n")
#Inicio do loop
while True:
    while True:
        pratos = input("Digite 'BA' para escolher Bife Acebolado ou 'FF' para escolher Filé de Frango: \n")
        if pratos == "BA":
            prato_escolhido = "Bife Acebolado"
            print(f"Você escolheu: {prato_escolhido}\n")
            break
        elif pratos == "FF":
            prato_escolhido = "Filé de Frango"
            print(f"Você escolheu: {prato_escolhido}\n")
            break
        else:
            print("Sabor inválido. Tente novamente digitando BA ou FF.\n")
            continue

#Modo aninhado, conforme exigência do código
    while True:
        tamanho = input("Digite 'P', 'M' ou 'G' para escolher entre os tamanhos Pequeno, Médio e Grande: \n")
        if tamanho == "P":
            tamanho_escolhido = "Pequeno"
            print(f"\nVocê escolheu: {prato_escolhido} tamanho {tamanho_escolhido}!\n")
            break
        elif tamanho == "M":
            tamanho_escolhido = "Médio"
            print(f"\nVocê escolheu: {prato_escolhido} tamanho {tamanho_escolhido}!\n")
            break
        elif tamanho == "G":
            tamanho_escolhido = "Grande"
            print(f"\nVocê escolheu: {prato_escolhido} tamanho {tamanho_escolhido}!\n")
            break
        else:
            print("Tamanho inválido. Tente novamente digitando P, M ou G.\n")
            continue
    if pratos == "BA":
        if tamanho == "P":
            preco = 16.00
            print(f"Conforme nosso Menu, {prato_escolhido} tamanho {tamanho_escolhido} sairá no valor de R${preco:.2f}\n")
        elif tamanho == "M":
            preco = 18.00
            print(f"Conforme nosso Menu, {prato_escolhido} tamanho {tamanho_escolhido} sairá no valor de R${preco:.2f}\n")
        elif tamanho == "G":
            preco = 22.00
            print(f"Conforme nosso Menu, {prato_escolhido} tamanho {tamanho_escolhido} sairá no valor de R${preco:.2f}\n")
    elif pratos == "FF": 
        if tamanho == "P":
            preco = 15.00
            print(f"Conforme nosso Menu, {prato_escolhido} tamanho {tamanho_escolhido} sairá no valor de R${preco:.2f}\n")
        elif tamanho == "M":
            preco = 17.00
            print(f"Conforme nosso Menu, {prato_escolhido} tamanho {tamanho_escolhido} sairá no valor de R${preco:.2f}\n")
        elif tamanho == "G":
            preco = 21.00
            print(f"Conforme nosso Menu, {prato_escolhido} tamanho {tamanho_escolhido} sairá no valor de R${preco:.2f}\n")
    pedidos.append(f"{prato_escolhido} tamanho {tamanho_escolhido} - R${preco:.2f}")        
    total += preco

    print(f"Até o momento, sua compra está com o valor de: R${total:.2f}\n") 

#Precisei criar mais um while pra rodar esse 'algo_mais
    while True:
        algo_mais = input("Deseja pedir mais alguma coisa? Digite 'Sim' ou 'Não': \n")
        if algo_mais == "Sim":
            break
        elif algo_mais == "Não":
            encerrar = True
            break
        else:
            print("Opção inválida. Tente novamente digitando Sim ou Não.\n")
    #Usando a variável que criei no início do código. Com ele consegue completar o 'algo_mais'    
    if encerrar:
        break

#Uso do For pra imprimir item por item
print("\nRESUMO FINAL DO PEDIDO: \n")
for item in pedidos:
    print(f"- {item}\n")

print(f"Seu pedido ficou no total de R${total:.2f}\n")








