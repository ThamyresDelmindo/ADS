print("\nBoas vindas ao Camisaria by Thamyres Delmindo\n")
print("Segue abaixo nosso Catálogo\n")
print("=" * 80)
print("|" + "CAMISARIA".center(75) + "|".center(1)) #Desenho do catálogo
print("=" * 80)
print("|" + "Modelos".center(29) + "|" + "Valor Unitário".center(21) + "|" + "Fretes Disponíveis".center(23) + "|")
print("|" + "MCS - Manga Curta Simples".center(29) + "|" + "R$ 1,80".center(21) + "|" + "Transportadora".center(23) + "|") 
print("|" + "MLS - Manda Longa Simples".center(29) + "|" + "R$ 2,10".center(21) + "|" + "Sedex".center(23) + "|")
print("|" + "MCE - Manga Curta com Estampa".center(13) + "|" + "R$ 2,90".center(21) + "|" + "Retirada na fábrica".center(23) + "|")
print("|" + "MLE - Manga Longa com Estampa".center(13) + "|" + "R$ 3,20".center(21) + "|" + "|".center(48))
print("=" * 80)
#Novamente, criei a variável de pedido pra poder usar o append e fazer um resumo do pedido mais bonitinho
pedido = []
print("\nEspero que tenha gostado das opções, vamos iniciar seu pedido...\n")
#Início da função usando return, looping e condicionais
def escolha_modelo():
    while True:
            modelo = input(
                "\nQual o modelo desejado de camiseta? Escolha entre MCS, MLS, MCE e MLE:\n"
                "MCS - Manga Curta Simples\n"
                "MLS - Manga Longa Simples\n"
                "MCE - Manga Curta com Estampa\n"
                "MLE - Manga Longa com Estampa\n"
                ">>")
            if modelo == "MCS":
                return modelo, 1.80
            elif modelo == "MLS":
                return modelo, 2.10
            elif modelo == "MCE":
                return modelo, 2.90
            elif modelo == "MLE":
                return modelo, 3.20
            else:
                print("Tente novamente digitando MCS, MLS, MCE ou MLE.\n")
#Coloquei para o return trazer o modelo, quantidade, e frete escolhidos pelo cliente, para imprimir no resumo.
#Comecei a usar o try e except focando no uso de int e float pelo usuário
def num_camisetas():
    while True:
        try:
            quantidade = int(input("Qual a quantidade desejada de camisetas?\n>>"))
            if quantidade <20:
                return quantidade, 0 / 100
            elif 20 <= quantidade < 200:
                return quantidade, 5 / 100
            elif 200 <= quantidade < 2000:
                return quantidade, 7 / 100
            elif 2000 <= quantidade <= 20000:
                return quantidade, 12 / 100
            elif quantidade > 20000:
                print("Não aceitamos pedidos nessa quantidade. Tente novamente com quantidade entre 1 e 20.000\n")
        except:
            print("Tente novamente digitando entre 0 e 20.000.\n")
        
def frete():
    while True:
        try:
            frete = int(input(
                "\nDeseja qual serviço de entrega? Digite entre 0, 1 ou 2\n"
                "0 - Retirada na fábrica - R$ 0\n"
                "1 - Frete por Transportadora - R$ 100,00\n"
                "2 - Frete por Sedex - R$ 200,00\n"
                ">>"))
            if frete == 1:
                return "Transportadora", 100
            elif frete == 2:
                return "Sedex", 200
            elif frete == 0:
                return "Retirada", 0
        except: 
            print("Tente novamente digitando 0, 1 ou 2.")


modelo_camiseta, modelo_escolhido = escolha_modelo()
qtd_escolhida, desconto = num_camisetas()
qtd_desconto = qtd_escolhida * (1 - desconto)
opcao_frete, adicional = frete()
total = (modelo_escolhido * qtd_desconto) + adicional
pedido.append(f"Quantidade: x{qtd_escolhida} | Modelo: {modelo_camiseta} | Valor unitário: R${modelo_escolhido:.2f} | Desconto: {desconto*100:.0f}% | Desconto aplicado: R${qtd_desconto:.0f} | Frete: {opcao_frete} | Adicional de frete: R${adicional}")

print("\nRESUMO FINAL DO PEDIDO: \n")
#Impressão do resumo do pedido criado na variável e no append
for item in pedido:
    print(f" - {item}\n")

print(f"Seu pedido ficou no total de R${total:,.0f}".replace(",", "."))
