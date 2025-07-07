print("\nSeja bem vindo(a) ao Gerenciador de Funcionários by Thamyres Delmindo")
print("-" * 70)

#Dicionario criado aguardando a lista para armazenar os dados
lista_funcionarios = []
id_global = "5352217" #id global sendo minha RU

#funções criadas fora da estrutura principal, aguardando a chamada
def cadastrar_funcionario(id):
    print("-" * 70)
    print("MENU DE CADASTRO DE FUNCIONÁRIO".center(60))
    print("-" * 70)
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = input("Digite o salário do funcionário: ")
    funcionario = {
        "id_": id, 
        "nome": nome, 
        "setor": setor, 
        "salario": salario}
    lista_funcionarios.append(funcionario.copy()) #Aqui adiciono a lista ao dicionário criado inicialmente

def consultar_funcionarios():
    while True:
        print("-" * 70)
        print("MENU DE CONSULTA DE FUNCIONÁRIOS".center(60))
        print("-" * 70)
        opcao_consulta = input("Escolha a opção desejada:\n"
        "1 - Consultar Todos\n"
        "2 - Consultar por Id\n"
        "3 - Consultar por Setor\n"
        "4 - Retornar ao menu\n"
        ">>") 
        if opcao_consulta == "1":
            for funcionario in lista_funcionarios:
                print(f"id: {funcionario['id_']}")
                print(f"nome: {funcionario['nome']}")
                print(f"setor: {funcionario['setor']}")
                print(f"salário: {funcionario['salario']}")
                print("-" * 70)
        elif opcao_consulta == "2":
            consulta_id = input("Informe o id do funcionário:\n>>")
            for funcionario in lista_funcionarios: #Aqui faço uma consulta nos itens da lista dentro do dicionário e as imprimo
                if consulta_id == funcionario["id_"]:
                    print(f"id: {funcionario['id_']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salário: {funcionario['salario']}")
                    print("-" * 70)
        elif opcao_consulta == "3":
            consulta_setor = input("Informe o setor do funcionário: \n>>")
            for funcionario in lista_funcionarios:
                if consulta_setor == funcionario["setor"]:
                    print(f"id: {funcionario['id_']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salário: {funcionario['salario']}")
                    print("-" * 70)
        elif opcao_consulta == "4":
            return
        else:
            print("Opção inválida. Tente novamente digitando 1, 2, 3 ou 4")

def remover_funcionario():
    while True:
        print("-" * 70)
        print("MENU DE REMOÇÃO DE FUNCIONÁRIO".center(60))
        print("-" * 70)
        func_removido = input("Digite o ID do funcionário a ser removido: \n>>")
        for funcionario in lista_funcionarios:
            if func_removido == funcionario["id_"]:
                lista_funcionarios.remove(funcionario)
                print(f"\nFuncionário removido com sucesso!")
                return
        else:
            print("Id inválido. Tente novamente.")

#inicio da execução do programa no geral chamando as funções
while True:
    print("-" * 70)
    print("MENU PRINCIPAL".center(60))
    print("-" * 70)
    escolha_inicial = input("\nEscolha a opção desejada:\n"
    "1 - Cadastrar Funcionários\n"
    "2 - Consultar Funcionário(s)\n"
    "3 - Remover Funcionário\n"
    "4 - Encerrar programa\n>>")
    if escolha_inicial == "1":
        cadastrar_funcionario(id_global)
        id_global = str(int(id_global) + 1)
    elif escolha_inicial == "2":
        consultar_funcionarios()
    elif escolha_inicial == "3":
        remover_funcionario()
    elif escolha_inicial == "4":
        print("-" * 70)
        print("Encerrando o programa... Até a próxima!")
        break 
    else:
        print("Opção inválida. Tente novamente digitando as opções 1, 2, 3 ou 4")
        

