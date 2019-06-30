import os
import os.path

def espaco():
    print(20*"=")

#Funcoes Genericas

def criarArquivo(nomeArq):
    try:
        with open('%s.txt' %nomeArq, 'r') as f: #ja existe o arquivo? retorne
            return

    except IOError: #arquivo nao encontraddo? crie
         arq = open('%s.txt' %nomeArq, 'w')
         arq.close()

#OPCOES COM CLIENTE ABAIXO

def cadastrarCliente():
    print ('teste')

#MENUS ABAIXO

def menuClientes():
    espaco()
    print("MENU CLIENTES")
    espaco()
    print("1 - CADASTRAR CLIENTE")
    print("2 - EXCLUIR CLIENTE")
    print("3 - EXIBIR CLIENTE")
    print("4 - RETORNAR PARA O MENU PRINCIPAL")
    print("5 - ENCERRAR")
    espaco()
    opcaoClientes = int(input())

    while (opcaoClientes != 5):

        if (opcaoClientes == 1):
            nomeArq = 'clientes'
            criarArquivo(nomeArq)   #Conferir se o arquivo ja existe, caso nao criar
            cadastrarCliente()  #falta ajustes

        if (opcaoClientes == 4):
            return
        opcaoClientes = int(input("DIGITE A OPCAO DESEJADA: "))

    exit(0)

def menuProdutos():
    espaco()
    print("MENU PRODUTOS")
    espaco()
    print("1 - CADASTRAR PRODUTO")
    print("2 - EXCLUIR PRODUTO")
    print("3 - BUSCAR PRODUTO")
    print("4 - CARDAPIO")
    print("5 - RETORNAR PARA O MENU PRINCIPAL")
    print("6 - ENCERRAR")
    espaco()

    opcaoProdutos = int(input())

    while(opcaoProdutos != 6):
        if (opcaoProdutos == 1):
            nomeArq = 'produtos'
            criarArquivo(nomeArq)

        if (opcaoProdutos == 5):
            return
        opcaoProdutos = int(input("DIGITE A OPCAO DESEJADA: "))

    exit(0)

def menuPedidos():
    espaco()
    print("MENU PEDIDOS")
    espaco()
    print("1 - CADASTRO PEDIDO")
    print("2 - EXCLUIR PEDIDO")
    print("3 - BUSCAR PEDIDO")
    print("4 - RETORNAR PARA O MENU PRINCIPAL")
    print("5 - ENCERRAR")
    espaco()
    opcaoPedidos = int(input())

    while (opcaoPedidos != 5):

        if (opcaoPedidos == 1):
            nomeArq = 'pedidos'
            criarArquivo(nomeArq)

        if (opcaoPedidos == 4):
            return
        opcaoPedidos = int(input("DIGITE A OPCAO DESEJADA: "))

    exit(0)

def menuPrincipal():
    espaco()
    print("MENU PRINCIPAL")
    espaco()
    print("1 - OPCOES CLIENTES")
    print("2 - OPCOES PRODUTOS")
    print("3 - OPCOES PEDIDOS")
    print("4 - SAIR DO SISTEMA")
    espaco()
    opcao = int(input("DIGITE A OPCAO DESEJADA: "))
    return opcao

opcao = menuPrincipal()

while (opcao < 4):

    if (opcao == 1):
        menuClientes()

    if (opcao == 2):
        menuProdutos()

    if (opcao == 3):
        menuPedidos()

    opcao = menuPrincipal()
