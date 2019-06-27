def espaco():
    print(20*"=")

#MENUS ABAIXO

def menuClientes():
    espaco()
    print("MENU CLIENTES")
    espaco()
    print("1 - CADASTRAR CLIENTE")
    print("2 - EXCLUIR CLIENTE")
    print("3 - EXIBIR CLIENTE")
    print("4 - RETORNAR PARA O MENU PRINCIPAL")
    espaco()
    opcaoClientes = int(input("DIGITE A OPÇÃO DESEJADA: "))

    while (opcaoClientes < 4):
        if (opcaoClientes == 4):
            return
        opcaoClientes = int(input("DIGITE A OPÇÃO DESEJADA: "))

    return opcaoClientes



def menuProdutos():
    espaco()
    print("MENU PRODUTOS")
    espaco()
    print("1 - CADASTRAR PRODUTO")
    print("2 - EXCLUIR PRODUTO")
    print("3 - BUSCAR PRODUTO")
    print("4 - CARDÁPIO")
    print("5 - RETORNAR PARA O MENU PRINCIPAL")
    espaco()
    opcaoProdutos = int(input("DIGITE A OPÇÃO DESEJADA: "))
    return opcaoProdutos

def menuPedidos():
    espaco()
    print("MENU PEDIDOS")
    espaco()
    print("1 - CADASTRO PEDIDO")
    print("2 - EXCLUIR PEDIDO")
    print("3 - BUSCAR PEDIDO")
    print("4 - RETORNAR PARA O MENU PRINCIPAL")
    espaco()
    opcaoPedidos = int(input("DIGITE A OPÇÃO DESEJADA: "))
    return opcaoPedidos

def menuPrincipal():
    espaco()
    print("MENU PRINCIPAL!")
    espaco()
    print("Selecione a OPÇÃO desejada.")
    print("1 - OPÇÕES CLIENTES")
    print("2 - OPÇÕES PRODUTOS")
    print("3 - OPÇÕES PEDIDOS")
    print("4 - SAIR DO SISTEMA")
    espaco()
    opcao = int(input("DIGITE A OPCAO DESEJADA: "))
    return opcao



opcao = menuPrincipal()

while (opcao < 4):


    if (opcao == 1):
        menuClientes()

    if (opcao == 2):
        if (menuProdutos() == 5):
            menuPrincipal()

    if (opcao == 3):
        opcaoPedidos = menuPedidos()
        if (opcaoPedidos == 4):
            menuPrincipal()


