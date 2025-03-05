database = r"recursos_humanos.txt"

def carregar_arquivo_funcionario(): 
    rh = {}
    with open(database, "r") as file:
        for line in file:
            nome, usuario, senha = line.strip().split(",")
            rh[nome] = {
                "usuario": usuario,
                "senha": senha
            }
    return rh     

def salvar_arquivo(rh):
    with open(database, "w") as file:
        for nome, dados in rh.items():
            file.write(f"{nome},{dados['usuario']},{dados['senha']}\n")

def adicionar_pessoa(nome, user, senha):
    rh = carregar_arquivo_funcionario()
    rh[nome] = {
        'usuario': user,
        'senha': senha
    }
    salvar_arquivo(rh)

def mostrar_rh():
    rh = carregar_arquivo_funcionario() 
    for nome, dados in rh.items():
        print(f"Nome: {nome}, Usuario: {dados['usuario']}, Senha: {dados['senha']}\n")
            
def atualizar_usuario(nome, valor):
    rh = carregar_arquivo_funcionario()
    if nome in rh:
        rh[nome]['usuario'] = valor
        salvar_arquivo(rh)
    else:
        print(f"Pessoa com nome {nome} não encontrada.")

def atualizar_senha(nome, valor):
    rh = carregar_arquivo_funcionario()
    if nome in rh:
        rh[nome]['senha'] = valor
        salvar_arquivo(rh)
    else:
        print(f"Pessoa com nome {nome} não encontrada.")

def remover_pessoa(nome):
    rh = carregar_arquivo_funcionario()
    if nome in rh:
        del rh[nome]
        salvar_arquivo(rh)
        print(f"Pessoa {nome} removida com sucesso.")
    else:
        print(f"Pessoa com nome {nome} não encontrada.")

def exibir_menu():
    print("\n------- Menu de Gerenciamento de Funcionários -------")
    print("1 - Adicionar Funcionário")
    print("2 - Mostrar Funcionários")
    print("3 - Atualizar Nome de Usuário")
    print("4 - Atualizar Senha")
    print("5 - Remover Funcionário")
    print("6 - Sair")
    opcao = input("Selecione uma opção (1-6): ")
    return opcao

def processar_opcao(opcao):
    if opcao == '1':
        nome = input("Digite o nome do funcionário: ")
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        adicionar_pessoa(nome, usuario, senha)
        print(f"Funcionário {nome} adicionado com sucesso.")
    elif opcao == '2':
        mostrar_rh()
    elif opcao == '3':
        nome = input("Digite o nome do funcionário: ")
        novo_usuario = input("Digite o novo nome de usuário: ")
        atualizar_usuario(nome, novo_usuario)
    elif opcao == '4':
        nome = input("Digite o nome do funcionário: ")
        nova_senha = input("Digite a nova senha: ")
        atualizar_senha(nome, nova_senha)
    elif opcao == '5':
        nome = input("Digite o nome do funcionário: ")
        remover_pessoa(nome)
    elif opcao == '6':
        print("Saindo do programa...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")

def main():
    while True:
        opcao = exibir_menu()
        processar_opcao(opcao)

if __name__ == "__main__":
    main()
