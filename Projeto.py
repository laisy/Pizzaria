import os
import os.path
from datetime import date, datetime, time, timedelta

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
    codCliente = raw_input('Informe o codigo do Cliente: ')
    arq.write(str('codCliente: ' + codCliente + '\n'))
    arq.close()
    espaco()
    print('CLIENTE CADASTRADO COM SUCESSO!')
    espaco()

def excluirCliente():
    espaco()
    codCliente = raw_input('INFORME O CODIGO DO CLIENTE: ')
    confirma = raw_input('CONFIRMA A EXCLUSAO DO CLIENTE? ')
    espaco()

    codCliente = (str('codCliente: ' + codCliente + '\n'))
    lista = []
    if (confirma == 'sim'):
        with open('clientes.txt', 'r') as a:
            for linha in a.readlines():
                lista.append(linha)

            if (codCliente in lista):
                posi = lista.index(codCliente)

                lista.pop(int(posi))
                lista.pop(int(posi-1))
                lista.pop(int(posi-2))
                lista.pop(int(posi-3))

                arq = open('clientes.txt', 'w')
                arq.writelines(lista)
                arq.close()
                espaco()
                print ('CLIENTE REMOVIDO!')
                espaco()

    elif (confirma == 'nao'):
        return
    else:
        espaco()
        print('OPCAO INVALIDA! ')
        espaco()
        return

def exibirCliente():
    espaco()
    tel = raw_input('INFORME O TELEFONE DO CLIENTE: ')
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
                        listaCliente.append(lista[k].rstrip('\n'))      # .rstrip('\n') serve para retirar o \n
                        listaCliente.append(lista[k+1].rstrip('\n'))
                        listaCliente.append(lista[k+2].rstrip('\n'))
                        listaCliente.append(lista[k+3].rstrip('\n'))

                        for k in listaCliente:
                            print(k)

    except IOError:
        criarArquivo(clientes)
        return

def buscaCliente():
    espaco()
    codClien = int(raw_input('INFORME O CODIGO DO CLIENTE: '))
    nCod = str('codCliente: ' + str(codClien)  + '\n')
    espaco()

    listaCliente = []
    lista = []
    with open( 'clientes.txt', 'r' ) as a:
        for linha in a.readlines():
            lista.append(linha)
        for k in range(len(lista)):
            flag = nCod in lista[k]
            if (flag == True):
                if lista[k] == nCod:
                    listaCliente.append(lista[k])
                    listaCliente.append(lista[k-1])
                    listaCliente.append(lista[k-2])
                    listaCliente.append(lista[k-3])

                    return listaCliente
    return

#OPCOES COM PRODUTOS ABAIXO

def cadastrarProduto():
    arq = open('produtos.txt', 'a')

    espaco()
    codProduto = int(input('Informe o codigo do Produto: '))
    arq.write(str('codProduto: ' + str(codProduto) + '\n'))
    nome = raw_input('Informe o nome do Produto: ')
    arq.write(str('Nome: ' + nome + '\n'))
    tempoMax = raw_input('Informe o tempo maximo de preparo: ')
    arq.write(str('TempoMax: ' + tempoMax + '\n'))
    ativo = raw_input('Informe se produto esta ativo (0 - Ativo ou 1 - Inativo): ')
    arq.write(str('Ativo: ' + ativo + '\n'))
    preco = float(input('Informe o preco do Produto: R$ '))
    arq.write(str('Preco: R$ ' + str(preco) + '\n'))

    arq.close()

    espaco()
    print('PRODUTO CADASTRADO COM SUCESSO!')
    espaco()
    return

def excluirProduto():
        espaco()
        cod = int(raw_input('INFORME O CODIGO DO PRODUTO: '))
        confirma = raw_input('CONFIRMA A EXCLUSAO DO PRODUTO? ')
        espaco()

        cod = (str('codProduto: ' + str(cod) + '\n'))
        lista = []
        if (confirma == 'sim'):
            with open('produtos.txt', 'r') as a:
                for linha in a.readlines():
                    lista.append(linha)

                if (cod in lista):
                    posi = lista.index(cod)

                    lista.pop(int(posi+4))
                    lista.pop(int(posi+3))
                    lista.pop(int(posi+2))
                    lista.pop(int(posi+1))
                    lista.pop(int(posi))

                    arq = open('produtos.txt', 'w')
                    arq.writelines(lista)
                    arq.close()
                    espaco()
                    print ('PRODUTO REMOVIDO!')
                    espaco()

        elif (confirma == 'nao'):
            return
        else:
            espaco()
            print('OPCAO INVALIDA! ')
            espaco()
            return

def buscarProduto(nCod):

    listaProduto = []
    lista = []
    try:
        with open( 'produtos.txt', 'r' ) as a:
            for linha in a.readlines():
                lista.append(linha)
            for k in range(0, len(lista)):
                flag = nCod in lista[k]
                if (flag == True):
                    if lista[k] == nCod:
                        listaProduto.append(lista[k])
                        listaProduto.append(lista[k+1])
                        listaProduto.append(lista[k+2])
                        listaProduto.append(lista[k+3])
                        listaProduto.append(lista[k+4])

                        return listaProduto

    except IOError:
        criarArquivo(produtos)
        return

def tiraBarraN():
    listaProduto = buscarProduto()
    for i in range(0, len(listaProduto)):
        novaLista = listaProduto[i].rstrip('\n')

    return novaLista

def printProduto(nCod):
    listaProduto = buscarProduto(nCod)
    for k in listaProduto:
        print(k)
    return listaProduto

def cardapio():

        listaCard = []
        lista = []

        with open( 'produtos.txt', 'r' ) as a:
            for linha in a.readlines():
                lista.append(linha)
            for k in range(len(lista)):
                if (lista[k] == 'Ativo: 0\n'):
                    listaCard.append(lista[k-3].rstrip('\n'))
                    listaCard.append(lista[k-2].rstrip('\n'))
                    listaCard.append(lista[k+1].rstrip('\n'))
                    listaCard.append('\n')

        espaco()
        print ('CARDAPIO')
        espaco()
        for k in listaCard:
            print(k)
        espaco()

#OPCOES COM PEDIDOS ABAIXO

def cadastrarPedido():

    listaPedidos = []
    arq = open('pedidos.txt', 'a')

    espaco()
    codPed = int(input('INFORME O CODIGO DO PEDIDO: '))
    arq.write(str('CodigoPedido: ' + str(codPed) + '\n'))

    quantProd = int(input('INFORME A QUANTIDADE DE PRODUTOS: '))
    quantP = quantProd
    arq.write(str('QuantidadeProd: ' + str(quantProd) + '\n'))

    if (quantP == 1):
        espaco()
        cod = int(raw_input('INFORME O CODIGO DO PRODUTO: '))
        nCod = str('codProduto: ' + str(cod)  + '\n')
        espaco()

        quantDoProd = int(input('INFORME A QUANTIDADE DESSE PRODUTO: '))
        for i in range(0, quantDoProd):
            listaPedidos.extend(buscarProduto(nCod))

    else:
        while(quantP > 0):
            espaco()
            cod = int(raw_input('INFORME O CODIGO DO PRODUTO: '))
            nCod = str('codProduto: ' + str(cod)  + '\n')
            espaco()

            quantDoProd = int(input('INFORME A QUANTIDADE DESSE PRODUTO: '))
            for i in range(0, quantDoProd):
                listaPedidos.extend(buscarProduto(nCod))
            quantP -= 1

    listaPedidos.extend(buscaCliente())
    arq.writelines(listaPedidos)

    data = (formatardata())
    arq.write(str('data: ' + str(data)  + '\n'))

    hora = (formatarhora())
    arq.write(str('Hora: ' + hora + '\n'))

    entrega = (somarHoras())
    arq.write(str('HoraEnt: ' + entrega + '\n'))

    arq.close()

    espaco()
    print('PEDIDO CADASTRADO COM SUCESSO!')
    espaco()

def formatardata():
    data = datetime.strptime('06/05/2016', '%d/%m/%Y').today()
    dataFormatada = data.strftime('%d/%m/%Y')
    return dataFormatada

def formatarhora():
    hora = datetime.strptime('00:00', '%H:%M').now()
    horaFormatada = hora.strftime('%H:%M')
    return horaFormatada

def somarHoras():
    horaFormatada = formatarhora()
    horas = horaFormatada[0]+horaFormatada[1]
    minutos = horaFormatada[3]+horaFormatada[4]

    min = int(horaEnt())
    dt = datetime.combine(date.today(), time(int(horas), int(minutos))) + timedelta(minutes=min)
    return dt.time()

def horaEnt():

    listaPedido = []
    lista = []
    listaTemps = []
    maiorTemp = 0

    try:
        with open('pedidos.txt', 'r') as a:
            for linha in a:
                operacao = linha[0:9]
                if operacao == 'TempoMax: ':
                    temp = int(linha[10:len(linha)-1])
                    listaTemps.append(temp)

    listaTemps.sort(reverse = True)
    maiorTemp = listaTemps[0].rstrip('\n')
    maiorTemp = int(listaTemps[0].rstrip('TempoMax: '))
    print maiorTemp

    return maiorTemp

def buscarPedido(codPed):

    listaPedido = []
    lista = []

    try:
        with open('pedidos.txt', 'r') as a:
            for linha in a.readlines():
                lista.append(linha)
            for k in range(0, len(lista)):
                flag = codPed in lista[k]
                if (flag == True):
                    if lista[k] == nCod:
                        listaPedido.append(lista[k])
                        listaPedido.append(lista[k+1])
                        listaPedido.append(lista[k+2])
                        listaPedido.append(lista[k+3])
                        listaPedido.append(lista[k+4])
                        listaPedido.append(lista[k+5])
                        listaPedido.append(lista[k+6])
                        listaPedido.append(lista[k+7])
                        listaPedido.append(lista[k+8])
                        listaPedido.append(lista[k+9])
                        listaPedido.append(lista[k+10])
                        listaPedido.append(lista[k+11])
                        listaPedido.append(lista[k+12])
                        listaPedido.append(lista[k+13])

                        return listaPedido

    except IOError:
        criarArquivo(pedidos)
        return


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

        if (opcaoClientes == 2):
            criarArquivo(nomeArq)
            excluirCliente()
            return

        if (opcaoClientes == 3):
            criarArquivo(nomeArq)
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
    print("4 - RETORNAR PARA O MENU PRINCIPAL")
    print("5 - ENCERRAR")
    espaco()

    opcaoProdutos = int(input())

    while(opcaoProdutos != 5):
        nomeArq = 'produtos'
        if (opcaoProdutos == 1):
            criarArquivo(nomeArq)
            cadastrarProduto()
            return

        if (opcaoProdutos == 2):
            excluirProduto()
            return

        if (opcaoProdutos == 3):
            espaco()
            cod = int(raw_input('INFORME O CODIGO DO PRODUTO: '))
            nCod = str('codProduto: ' + str(cod)  + '\n')
            espaco()
            printProduto(nCod)
            return

        if (opcaoProdutos == 4):
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
    print("4 - CARDAPIO")
    print("5 - SAIR DO SISTEMA")
    espaco()
    opcao = int(input("DIGITE A OPCAO DESEJADA: "))
    return opcao

opcao = menuPrincipal()

while (opcao < 5):

    if (opcao == 1):
        menuClientes()

    if (opcao == 2):
        menuProdutos()

    if (opcao == 3):
        menuPedidos()

    if (opcao == 4):
        cardapio()

    opcao = menuPrincipal()
