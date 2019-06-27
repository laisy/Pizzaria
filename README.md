# Projeto_Pizzaria
Projeto de um software para uma Pizzaria
Você foi contratado para desenvolver um programa para uma pizzaria. Para tal, o programa deverá ser desenvolvido na linguagem Python e implementar as seguintes funcionalidades: 
.
1. Manter o cadastro de todos os clientes da pizzaria em um arquivo texto chamado “clientes.txt”. O arquivo deverá conter as seguintes informações de cada cliente 
a. Telefone 
b. Nome completo 
c. Endereço 
d. Código do cliente (número atribuído sequencialmente para cada cliente,  respeitando os outros já cadastrados previamente) 
O programa deverá fornecer opções para cadastrar os clientes (através da solicitação dos dados acima). Todos os clientes serão gravados no arquivo “clientes.txt”. Cada informação deverá ocupar uma linha do arquivo (modo texto). 
.
2. Manter o cadastro das pizzas e demais produtos, armazenando as seguintes  informações no arquivo “produtos.txt”: 
a. Código do produto (número atribuído sequencialmente para cada produto,  respeitando os outros já cadastrados previamente) 
b. Nome do produto 
c. Tempo máximo de preparação 
d. Ativo (0 ou 1) 
e. Preço por unidade (real) 
O programa deverá fornecer opção para cadastrar os produtos (através da solicitação dos dados acima). No caso do cadastro das pizzas, o usuário deverá realizar vários cadastros (um para cada tamanho, além da opção de metade da pizza). Usuário também irá cadastrar a taxa de entrega neste item
.
3. Criar opção para a realização dos pedidos (arquivo: “pedidos.txt”) 
a. Código do pedido 
b. Quantidade de produtos (quantos produtos vão ter nesse pedido) 
c. Código do produto (para cada produto) 
d. Quantidade (para cada produto) 
e. Código do cliente 
f. Data do pedido (DD/MM) 
g. Hora do pedido (HH:MM) 
h. Hora prevista para entrega (HH:MM) 
.
4. Criar opção buscar pedido (consulta dos pedidos já realizados) 
a. Busca de todos os pedidos realizados no dia 
b. Busca do último pedido realizado 
Quando um cliente realizar um pedido (considerar que os pedidos são realizados por telefone), o programa deverá permitir a compra de vários produtos de uma só vez. No início da ligação, o cliente deverá informar o número do seu telefone e, caso conste no cadastro, seus dados serão exibidos na tela (inclusive seu código) para o atendente. Caso existam vários cadastros com o mesmo telefone, considerar somente o último. Ao finalizar um pedido, o programa deverá verificar qual é a previsão de entrega (selecionar o maior tempo de preparo dentre os produtos que foram escolhidos - verificar no arquivo “produtos.txt”). Na tela, o programa deverá exibir o valor total do pedido após o término da digitação de todos os produtos. Deve haver 2 opções para a seleção dos produtos: digitando o código do mesmo ou parte do seu nome. 
