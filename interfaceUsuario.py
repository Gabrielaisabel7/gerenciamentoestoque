from armazenamentoEstoque import carregar_arquivo, adicionar_estoque, mostrar_estoque, atualizar_quantidade, atualizar_preco, remover_estoque
from armazenamentoFuncionario import carregar_arquivo_funcionario, adicionar_pessoa, mostrar_rh, atualizar_usuario, atualizar_senha, remover_pessoa

def entrada_valida(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        print('Entrada inválida! Por favor, digite algo.')

def entrada_numerica(mensagem, tipo=float):
    while True:
        try:
            entrada = tipo(input(mensagem).replace(',', '.'))
            return entrada
        except ValueError:
            print('Valor inválido! Tente novamente.')

def CadastroDeProduto():
    estoque = carregar_arquivo()
    produto = entrada_valida('Digite o nome do produto que deseja cadastrar: ')
    if produto not in estoque:
        categoria = entrada_valida('Digite a categoria: ')
        quantidade = entrada_numerica('Insira a quantidade (Kg): ', int)
        preco = entrada_numerica('Insira o preço por quilo R$: ')
        adicionar_estoque(produto, categoria, quantidade, preco)
        print('Produto cadastrado com sucesso!')
    else:
        print('O produto já existe no estoque.')

def ListarEstoque():
    estoque = carregar_arquivo()
    if not estoque:
        print('O estoque está vazio.')
    else:
        mostrar_estoque()

def AtualizarProduto(produto):
    print('Selecione uma opção:')
    print('1 - Para atualizar a quantidade')
    print('2 - Para atualizar o preço')
    opcao = entrada_valida('Escolha uma opção: ')
    if opcao == '1':
        valor = entrada_numerica('Digite a nova quantidade: ')
        atualizar_quantidade(produto, valor)
        print('Quantidade atualizada com sucesso!')
    elif opcao == '2':
        valor = entrada_numerica('Digite o novo preço: ')
        atualizar_preco(produto, valor)
        print('Preço atualizado com sucesso!')
    else:
        print('Opção inválida.')

def ProcessarAtualizacaoProduto():
    estoque = carregar_arquivo()
    produto = entrada_valida('Digite o nome do produto que deseja atualizar: ')
    if produto in estoque:
        AtualizarProduto(produto)
    else:
        print('Esse produto não existe no estoque.')

def RemoverProduto():
    estoque = carregar_arquivo()
    produto = entrada_valida('Digite o nome do produto que deseja remover: ')
    if produto in estoque:
        remover_estoque(produto)
        print('Produto removido com sucesso!')
    else:
        print('O produto não existe no estoque.')

def menu_estoque():
    while True:
        print('\n------- Estoque -------')
        print('1 - Adicionar Produto')
        print('2 - Mostrar Estoque')
        print('3 - Atualizar Estoque')
        print('4 - Remover Produto')
        print('5 - Voltar ao Menu Principal')
        ent1 = entrada_valida('Selecione uma opção: ')
        if ent1 == '1':
            CadastroDeProduto()
        elif ent1 == '2':
            ListarEstoque()
        elif ent1 == '3':
            ProcessarAtualizacaoProduto()
        elif ent1 == '4':
            RemoverProduto()
        elif ent1 == '5':
            print('Saindo do estoque...')
            break
        else:
            print('Opção inválida. Tente novamente.')

def CadastroDePessoa():
    rh = carregar_arquivo_funcionario()
    nome = entrada_valida('Digite o nome da pessoa que deseja cadastrar: ')
    if nome not in rh:
        usuario = entrada_valida('Digite o usuário: ')
        senha = entrada_valida('Digite a senha: ')
        adicionar_pessoa(nome, usuario, senha)
        print('Pessoa cadastrada com sucesso!')
    else:
        print('A pessoa já existe no RH.')

def ListarPessoas():
    rh = carregar_arquivo_funcionario()
    if not rh:
        print('O RH está vazio.')
    else:
        mostrar_rh()

def AtualizarPessoas(nome):
    print('1 - Para atualizar o usuário')
    print('2 - Para atualizar a senha')
    opcao = entrada_valida('Escolha uma opção: ')
    if opcao == '1':
        novo_usuario = entrada_valida('Digite o novo usuário: ')
        atualizar_usuario(nome, novo_usuario)
        print('Usuário atualizado com sucesso!')
    elif opcao == '2':
        nova_senha = entrada_valida('Digite a nova senha: ')
        atualizar_senha(nome, nova_senha)
        print('Senha atualizada com sucesso!')
    else:
        print('Opção inválida.')

def RemoverPessoas():
    rh = carregar_arquivo_funcionario()
    nome = entrada_valida('Digite o nome da pessoa que deseja remover: ')
    if nome in rh:
        remover_pessoa(nome)
        print('Pessoa removida com sucesso!')
    else:
        print('A pessoa não existe no RH.')

def menu_rh():
    while True:
        print("\n------- Menu RH -------")
        print("1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Atualizar Pessoas")
        print("4 - Remover Pessoas")
        print("5 - Voltar ao Menu Principal")
        opcao = entrada_valida('Escolha uma opção: ')
        if opcao == '1':
            CadastroDePessoa()
        elif opcao == '2':
            ListarPessoas()
        elif opcao == '3':
            nome = entrada_valida('Digite o nome da pessoa que deseja atualizar: ')
            AtualizarPessoas(nome)
        elif opcao == '4':
            RemoverPessoas()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n------- Menu Principal -------")
        print("1 - Menu Estoque")
        print("2 - Menu RH")
        print("3 - Sair")
        opcao = entrada_valida('Escolha uma opção: ')
        if opcao == '1':
            menu_estoque()
        elif opcao == '2':
            menu_rh()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
