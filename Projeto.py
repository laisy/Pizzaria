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
    nome = raw_input('Informe o nome completo do Cliente: ')
    endereco = raw_input('Informe o endereco do Cliente: ')

    arq.close()

    arq = open('clientes.txt', 'r')
    linhas = arq.readlines()
    arq.close()

    if not linhas:
        code = '1'
    else:
        codeLinha = linhas[len(linhas) - 1]
        code = int(codeLinha[3:5])
        code += 1
        code = str(code)

    arq = open('clientes.txt', 'a')

    arq.write(str('Telefone: ' + telefone + '\n'))
    arq.write(str('Nome: ' + nome + '\n'))
    arq.write(str('Endereco: ' + endereco + '\n'))
    arq.write(str('cC ' + code + '\n'))

    espaco()
    print "O CODIGO atribuido a este CLIENTE e: " + code
    espaco()
    print('CLIENTE CADASTRADO COM SUCESSO!')
    espaco()

def excluirCliente():
    espaco()
    codCliente = raw_input('INFORME O CODIGO DO CLIENTE: ')
    confirma = raw_input('CONFIRMA A EXCLUSAO DO CLIENTE? ')
    espaco()

    codCliente = (str('cC ' + codCliente + '\n'))
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

def buscaCliente(nCod):

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

    arq = open('produtos.txt', 'r')

    linhas = arq.readlines()
    arq.close()

    if not linhas:
        code = '1'
    else:
        codeLinha = linhas[len(linhas) - 5]
        code = int(codeLinha[3:5])
        code += 1
        code = str(code)

    arq = open('produtos.txt', 'a')

    espaco()
    print "O CODIGO deste PRODUTO e: ", code
    arq.write(str('cP ' + code + '\n'))
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

        cod = (str('cP ' + str(cod) + '\n'))
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
    listaPrint = []

    arq = open('pedidos.txt', 'r')
    linhas = arq.readlines()
    arq.close()

    if not linhas:
        code = '1'
    else:
        codeLinha = linhas[0]
        code = int(codeLinha[3:5])
        code += 1
        code = str(code)

    arq = open('pedidos.txt', 'a')

    espaco()
    arq.write(str('CD ' + str(code) + '\n'))
    pcodPed = str('Codigo do Pedido: ' + str(code) + '\n')
    listaPrint.append(pcodPed)
    global ultimopedido
    ultimopedido = pcodPed

    quantProd = int(input('INFORME A QUANTIDADE DE PRODUTOS: '))
    quantP = quantProd
    arq.write(str('QuantidadeProd: ' + str(quantProd) + '\n'))
    pquantProd = str('QuantidadeProd: ' + str(quantProd) + '\n')
    listaPrint.append(pquantProd)

    if (quantP == 1):
        espaco()
        cod = int(raw_input('INFORME O CODIGO DO PRODUTO: '))
        nCod = str('cP ' + str(cod)  + '\n')
        espaco()

        quantDoProd = int(input('INFORME A QUANTIDADE DESSE PRODUTO: '))
        for i in range(0, quantDoProd):
            listaPedidos.extend(buscarProduto(nCod))
            listaPrint.extend(buscarProduto(nCod))

    else:
        while(quantP > 0):
            espaco()
            cod = int(raw_input('INFORME O CODIGO DO PRODUTO: '))
            nCod = str('cP ' + str(cod)  + '\n')
            espaco()

            quantDoProd = int(input('INFORME A QUANTIDADE DESSE PRODUTO: '))
            for i in range(0, quantDoProd):
                listaPedidos.extend(buscarProduto(nCod))
                listaPrint.extend(buscarProduto(nCod))
            quantP -= 1

    espaco()
    codClien = int(raw_input('INFORME O CODIGO DO CLIENTE: '))
    nCod = str('cC ' + str(codClien)  + '\n')
    espaco()
    listaPedidos.extend(buscaCliente(nCod))
    listaPrint.extend(buscaCliente(nCod))
    arq.writelines(listaPedidos)

    data = (formatardata())
    arq.write(str('data: ' + str(data)  + '\n'))
    pdata = str('data: ' + str(data)  + '\n')
    listaPrint.append(pdata)

    hora = (formatarhora())
    arq.write(str('Hora: ' + str(hora) + '\n'))
    phora = str('Hora: ' + str(hora) + '\n')
    listaPrint.append(phora)

    entrega = (somarHoras())
    arq.write(str('HoraEnt: ' + str(entrega) + '\n'))
    pentrega = str('Hora de Entrega: ' + str(entrega) + '\n')
    listaPrint.append(pentrega)

    arq.close()
    arq = open('pedidos.txt', 'a')

    valorPed = (calcularPreco())
    arq.write(str('ValorPed: ' + str(valorPed) + '\n'))
    pvalorPed = str('Valor do Pedido: R$' + str(valorPed) + '\n')
    listaPrint.append(pvalorPed)

    taxaEntrega = float(2.00)
    arq.write(str('taxaEntrega: ' + str(taxaEntrega) + '\n'))
    ptaxaEntrega = str('taxaEntrega: R$' + str(taxaEntrega) + '\n')
    listaPrint.append(ptaxaEntrega)

    valorTotal = float(taxaEntrega + valorPed)
    arq.write(str('valorTotal: ' + str(valorTotal) + '\n'))
    pvalorTotal = str('valorTotal: R$' + str(valorTotal) + '\n')
    listaPrint.append(pvalorTotal)

    arq.close()

    espaco()
    print('PEDIDO CADASTRADO COM SUCESSO!')
    espaco()

    for k in range(len(listaPrint)):
        print listaPrint[k]
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

    lista = []
    listaTemps = []
    maiorTemp = 0
    temp = 0

    with open('pedidos.txt', 'r') as a:
        for linha in a:
            linha.rstrip('\n')
            operacao = linha[0:10]
            if operacao == 'TempoMax: ':
                temp = int(linha[10:len(linha)-1])
                listaTemps.append(temp)

    listaTemps.sort(reverse = True)
    for k in range(len(listaTemps)):
        if k == 0:
            maiorTemp = listaTemps[0]

    return maiorTemp

def calcularPreco():

    soma = 0
    precos = 0

    with open('pedidos.txt', 'r') as a:
        for linha in a:
            linha.rstrip('\n')
            operacao = linha[0:10]
            if operacao == 'Preco: R$ ':
                precos = float(linha[10:len(linha)-1])
                precos += precos

                return float(precos)


def buscaUltimoPedido(ultimopedido):

    listaPedido = []
    lista = []
    novaLista = []

    arq = open('pedidos.txt', 'r')
    linhas = arq.readlines()
    arq.close()
    if not linhas:
        print "NENHUM PEDIDO CADASTRADO! "

    with open('pedidos.txt', 'r') as a:
        for linha in a.readlines():
            lista.append(linha)

        lista.reverse()

        for k in range(len(lista)):
            listaPedido.append(lista[k])
            if lista[k] == ultimopedido:
                listaPedido.append(lista[k])
                break

        listaPedido.reverse()

        espaco()
        for i in range(len(listaPedido)):
            novaLista.append(listaPedido[i].rstrip('\n'))
            print novaLista[i]
        espaco()

def buscaPedidoDia():
    data = formatardata()
    pdata = str('data: ' + str(data))

    datan = str('data: ' + str(data) + '\n')

    listaPedido = []
    lista = []
    novaLista = []

    arq = open('pedidos.txt', 'r')
    linhas = arq.readlines()
    arq.close()
    if not linhas:
        print "NENHUM PEDIDO CADASTRADO! "
    else:
        espaco()
        print "PEDIDOS REALIZADOS EM", pdata
        espaco()
        with open('pedidos.txt', 'r') as a:
            espaco()
            for linha in a.readlines():
                print linha

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
            nCod = str('cP ' + str(cod)  + '\n')
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
    print("2 - BUSCAR PEDIDO")
    print("3 - RETORNAR PARA O MENU PRINCIPAL")
    print("4 - ENCERRAR")
    espaco()
    opcaoPedidos = int(input())

    while (opcaoPedidos != 4):
        nomeArq = 'pedidos'
        if (opcaoPedidos == 1):
            criarArquivo(nomeArq)
            cadastrarPedido()
            return

        if (opcaoPedidos == 2):
            menuBuscaPedidos()
            return
        if (opcaoPedidos == 3):
            return
        opcaoPedidos = int(input("DIGITE A OPCAO DESEJADA: "))

    exit(0)

def menuBuscaPedidos():
    espaco()
    print("1 - BUSCA DO ULTIMO PEDIDO REALIZADO ")
    print("2 - BUSCA DE TODOS OS PEDIDOS REALIZADOS NO DIA ")
    print("3 - RETORNAR PARA O MENU PRINCIPAL")
    print("4 - ENCERRAR")
    espaco()
    opcaoBUSCAPedidos = int(input())

    while (opcaoBUSCAPedidos != 4):
        if (opcaoBUSCAPedidos == 1):
            buscaUltimoPedido(ultimopedido)
            return

        if (opcaoBUSCAPedidos == 2):
            buscaPedidoDia()
            return

        if (opcaoBUSCAPedidos == 3):
            return
        opcaoBUSCAPedidos = int(input("DIGITE A OPCAO DESEJADA: "))

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

ultimopedido = ''
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
