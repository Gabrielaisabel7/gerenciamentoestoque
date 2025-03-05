database = r"estoque.txt"

def carregar_arquivo():
    estoque = {}
    with open(database, "r") as file:
        for line in file:
            produto, categoria, quantidade, preco = line.strip().split(",")           
            estoque[produto] = {
                "categoria": categoria,
                "quantidade": int(quantidade),
                "preco": float(preco)     
            }
    return estoque

def salvar_arquivo(estoque):
    with open(database, "w") as file:
        for produto, dados in estoque.items():
            file.write(f"{produto},{dados['categoria']},{dados['quantidade']},{dados['preco']}\n")

def adicionar_estoque(prod, cat, quant, preco):
    estoque = carregar_arquivo()
    estoque[prod] = {
        'categoria': cat,
        'quantidade': int(quant),
        'preco': float(preco),
    }
    salvar_arquivo(estoque)

def mostrar_estoque():
    estoque = carregar_arquivo() 
    for produto, dados in estoque.items():
        print(f"Produto: {produto}, Categoria: {dados['categoria']}, Quantidade: {dados['quantidade']}, Preço: {dados['preco']:.2f}")        

def atualizar_quantidade(prod, valor):
    estoque = carregar_arquivo()
    estoque[prod]['quantidade'] = int(valor)
    salvar_arquivo(estoque)

def atualizar_preco(produto, novo_preco):
    estoque = carregar_arquivo()
    if produto in estoque:
        estoque[produto]['preco'] = novo_preco
        salvar_arquivo(estoque)
    else:
        print("Produto não encontrado.")

def remover_estoque(prod):
    estoque = carregar_arquivo()
    del estoque[prod]
    salvar_arquivo(estoque)

if __name__ == "__main__":
    print("\n------- Menu de Gerenciamento do Estoque -------")
    print("Selecione uma opção:")
    print("1. Mostrar Estoque")
    print("2. Adicionar Produto")
    print("3. Atualizar Quantidade")
    print("4. Atualizar Preço")
    print("5. Remover Produto")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_estoque()
    elif opcao == "2":
        prod = input("Digite o nome do produto: ")
        cat = input("Digite a categoria do produto: ")
        quant = input("Digite a quantidade do produto: ")
        preco = input("Digite o preço do produto: ")
        adicionar_estoque(prod, cat, quant, preco)
    elif opcao == "3":
        prod = input("Digite o nome do produto: ")
        quant = input("Digite a nova quantidade: ")
        atualizar_quantidade(prod, quant)
    elif opcao == "4":
        prod = input("Digite o nome do produto: ")
        preco = input("Digite o novo preço: ")
        atualizar_preco(prod, preco)
    elif opcao == "5":
        prod = input("Digite o nome do produto a ser removido: ")
        remover_estoque(prod)
    else:
        print("Opção inválida.")
