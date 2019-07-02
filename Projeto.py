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
    arq.write(str('Telefone: ' + telefone + '\n'))
    nome = raw_input('Informe o nome completo do Cliente: ')
    arq.write(str('Nome: ' + nome + '\n'))
    endereco = raw_input('Informe o endereco do Cliente: ')
    arq.write(str('Endereco: ' + endereco + '\n'))
    codigo = input('Informe o codigo do Cliente: ')
    arq.write(str('Codigo: ' + codigo + '\n'))
    arq.close()
    espaco()
    print('CLIENTE CADASTRADO COM SUCESSO!')
    espaco()

def exibirCliente():
    espaco()
    tel = input('INFORME O TELEFONE DO CLIENTE: ')
    nTel = str('Telefone: ' + tel  + '\n')
    espaco()

    listaCliente = []
    lista = []
    try:
        with open( 'clientes.txt', 'r' ) as a:
            for linha in a.readlines():
                lista.append(linha)
            for k in range(0, len(lista), 3):
                flag = nTel in lista[k]
                if (flag == True):
                    if lista[k] == nTel:
                        listaCliente.append(lista[k].rstrip('\n'))
                        listaCliente.append(lista[k+1].rstrip('\n'))
                        listaCliente.append(lista[k+2].rstrip('\n'))
                        listaCliente.append(lista[k+3].rstrip('\n'))

                        for k in listaCliente:
                            print(k)

    except IOError:
        criarArquivo(clientes)
        return


#OPCOES COM PRODUTOS ABAIXO

def cadastrarProduto():
        arq = open('produtos.txt', 'a')

        espaco()
        cod = input('Informe o codigo do Produto: ')
        arq.write(str('Codigo: ' + cod + '\n'))
        nome = raw_input('Informe o nome do Produto: ')
        arq.write(str('Nome: ' + nome + '\n'))
        tempoMax = raw_input('Informe o tempo maximo de preparo: ')
        arq.write(str('TempoMax: ' + tempoMax + '\n'))
        ativo = input('Informe se produto esta ativo (0 - Ativo ou 1 - Inativo): ')
        arq.write(str('Ativo: ' + ativo + '\n'))
        preco = input('Informe o preco do Produto: R$ ')
        arq.write(str('Preco: ' + preco + '\n'))

        arq.close()

        espaco()
        print('PRODUTO CADASTRADO COM SUCESSO!')
        espaco()

#OPCOES COM PEDIDOS ABAIXO

def cadastrarPedido():

        arq = open('pedidos.txt', 'a')

        espaco()
        codPed = input('Informe o codigo do Pedido: ')
        arq.write(str('CodigoPedido: ' + codPed + '\n'))

        quantProd = int(input('Informe a quantidade de Produtos: '))
        arq.write(str('QuantidadeProd: ' + str(quantProd) + '\n'))
        if (quantProd == 1):
            codProd = input('Informe o codigo do produto: ')
            arq.write(str('CodigoProduto: ' + codProd + '\n'))
            quantDoProd = input('Informe a quantidade desse Produto: ')
            arq.write(str('QuantDoProd: ' + quantDoProd + '\n'))
        else:
            while(quantProd > 0):
                codProd = input('Informe o codigo do produto: ')
                arq.write(str('CodigoProduto: ' + codProd + '\n'))
                quantDoProd = input('Informe a quantidade desse Produto: ')
                arq.write(str('QuantDoProd: ' + quantDoProd + '\n'))
                quantProd -= 1

        codClien = input('Informe o codigo do cliente: ')
        arq.write(str('CodCliente: ' + codClien + '\n'))
        data = raw_input('Informe a data (DD/MM) do Pedido: ')
        arq.write(str('Data: ' + data + '\n'))
        hora = input('Informe a hora (HH/MM) do Pedido: ')
        arq.write(str('Hora: ' + hora + '\n'))
        horaEnt = input('Informe a hora (HH/MM) prevista para entrega: ')
        arq.write(str('horaEnt: ' + horaEnt + '\n'))

        arq.close()

        espaco()
        print('PEDIDO CADASTRADO COM SUCESSO!')
        espaco()

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
            cadastrarCliente()
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
        nomeArq = 'produtos'
        if (opcaoProdutos == 1):
            criarArquivo(nomeArq)
            cadastrarProduto()
            return
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
        nomeArq = 'pedidos'
        if (opcaoPedidos == 1):
            criarArquivo(nomeArq)
            cadastrarPedido()
            return
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
