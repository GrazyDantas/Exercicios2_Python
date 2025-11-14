estoque = []
sair = 1

while sair != 0:
    print("\n================== Menu ==================")
    print("Adicionar produto = 1")
    print("Listar produtos = 2")
    print("Atualizar estoque = 3")
    print("Apagar produtos = 4")
    print("Sair = 5")

    try:
        opcao = int(input("Digite o número da opção escolhida: "))
    except :
        print("Digite apenas números.")
        continue

    if opcao == 1:
        print("\n=========== Adicionar Produto ===========")
        produto = input("Digite o nome do produto: ")
        try:
            qtde = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
            novoProduto = (produto, qtde, preco)
            estoque.append(novoProduto)
            print("Produto adicionado com sucesso!")
        except:
            print("Erro! A quantidade e o preço devem ser números.")

    elif opcao == 2:
        print("\n=========== Listar Produtos ===========")
        if estoque == []:
            print("Não há produtos no estoque.")
        else:
            i = 0
            while i < len(estoque):
                print(estoque[i])
                i += 1

    elif opcao == 3:
        print("\n========== Atualizar Estoque ===========")
        produto_atualizar = input("Digite o nome do produto que deseja atualizar: ")
        encontrado = False
        i = 0
        while i < len(estoque):
            if produto_atualizar == estoque[i][0]:
                encontrado = True
                try:
                    qtde_nova = int(input("Digite a nova quantidade: "))
                    preco_novo = float(input("Digite o novo preço: "))
                    novoProduto = ({produto_atualizar}, {qtde_nova}, {preco_novo})
                    estoque[i] = novoProduto
                    print("Produto atualizado com sucesso!")
                except:
                    print("Erro! A quantidade e o preço devem ser números.")
                break
            i += 1

        if encontrado == False:
            print("Produto não encontrado!")

    elif opcao == 4:
        print("\n=========== Apagar Produtos ===========")
        apagarProd = input("Digite o nome do produto que deseja apagar: ")
        encontrado = False
        i = 0
        while i < len(estoque):
            if apagarProd == estoque[i][0]:
                estoque.pop(i)
                encontrado = True
                print("Produto apagado com sucesso!")
                break
            i += 1

        if encontrado == False:
            print("Produto não encontrado!")

    elif opcao == 5:
        print("\n=========== Sair ===========")
        sair = 0
    else:
        print("Opção inválida. Digite um número de 1 a 5.")