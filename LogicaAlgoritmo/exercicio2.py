"""
Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0,15 por km rodado.
"""

km_percorrido = int(input("Quantos km foram percorridos ?: "))
dias_aluguel = int(input("Por quantos dias o carro foi alugado ?: "))

preco_dia = 60 * dias_aluguel + 0.15 * km_percorrido


print(f"Considerando que ficou {dias_aluguel} dias com o carro e percorreu {km_percorrido} kilômetros.")
print(f"O total a pagar é {preco_dia}")
