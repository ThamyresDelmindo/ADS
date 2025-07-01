"""QUESTÃO 1 de 4"""

#Criei essa variável para o caso de futuramente mudar o nome do App
app = "Parcela Aí"

print(f"\nSeja bem vindo(a) ao {app.upper()} by Thamyres Delmindo!\n")

print("Vamos iniciar seu processo de parcelamento do pedido")

#Exigência de código importante com float e int para permitir o cálculo dos valores obtidos
valorDoPedido = float(input("\nQual o valor do seu pedido?\n"))
quantidadeParcelas = int(input("\nQuer parcelar em quantas vezes?\n"))

print(f"\nVocê escolheu parcelar R${valorDoPedido:.2f} em {quantidadeParcelas} vezes\n")

print("Aguarde um momento que vamos calcular...")

#"quantidadeParcelas" no centro para referenciar a aplicação do comparativo das regras
def calcular_juros(quantidadeParcelas):
    if quantidadeParcelas < 4:
        return 0 / 100
    elif 4 <= quantidadeParcelas < 6:
        return 4 / 100
    elif 6 <= quantidadeParcelas < 9:
        return 8 / 100
    elif 9 <= quantidadeParcelas < 13:
        return 16 / 100
    else:
        return 32 /100

#variáveis logo após as regras comparativas para o Python conseguir executar linha após linha
juros = calcular_juros(quantidadeParcelas)
valorDaParcela = (valorDoPedido * (1 + juros))/quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

#prints logo depois das variáveis chave, para que o python identifique os dados coletados e os imprima corretamente
print("\nSeu juros foi aplicado!\n")  

print(f"Conforme o parcelamento escolhido, você teve o juros aplicado de:\n {juros * 100:.0f}%\n")

print(f"Cada parcela ficou no valor de:\n R${valorDaParcela:.2f}\n")

print(f"Seu pedido, com o parcelamento escolhido, ficou no total de:\n R${valorTotalParcelado:.2f}\n")

print("\nParabéns! Parcelamento concluído com sucesso!")

