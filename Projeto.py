from six.moves import input                         #biblioteca para manter raw_input e executar usando as duas versoes do Python
import os
import os.path

def espaco():
    print(20*"=")

#Funcoes Genericas

def criarArquivo(nomeArq):
    try:
        with open('%s.txt' %nomeArq, 'r') as f:     #ja existe o arquivo? retorne
            return

    except IOError:                                 #arquivo nao encontrado? crie
         arq = open('%s.txt' %nomeArq, 'w')
         arq.close()

#OPCOES COM CLIENTE ABAIXO

def cadastrarCliente():
    arq = open('clientes.txt', 'a')

    espaco()
    telefone = raw_input('Informe o telefone do Cliente: ')
    arq.write(str(telefone + '\n'))
    nome = raw_input('Informe o nome completo do Cliente: ')
    arq.write(str(nome + '\n'))
    endereco = raw_input('Informe o endereco do Cliente: ')
    arq.write(str(endereco + '\n'))
    codigo = input('Informe o codigo do Cliente: ')
    arq.write(str(codigo + '\n'))
    arq.close()
    espaco()
    print('CLIENTE CADASTRADO COM SUCESSO!')
    espaco()

def exibirCliente():
    arq = open('clientes.txt', 'r')
    espaco()
    tel = input('Informe o telefone do Cliente: ')
    espaco()

    listCliente = []
    if tel in arq:
        for linha in arq:
            for i in linha:
                listCliente.append(linha[i])
                listCliente.append(linha[i+1])
                listCliente.append(linha[i+2])
                listCliente.append(linha[i+3])

    arq.close()
    for k in range(len(listCliente)):
            print(listCliente[k])


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
        nomeArq = 'clientes'
        if (opcaoClientes == 1):
            criarArquivo(nomeArq)               #Conferir se o arquivo ja existe, caso nao criar
            cadastrarCliente()                  #falta ajustes
            return

        if (opcaoClientes == 3):
            exibirCliente()
            return

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
