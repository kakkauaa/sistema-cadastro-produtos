produtos = []
option = ''

def cadastrar_produto():

    cod = int(input('Qual o código do produto?'))
    cat = str(input('Qual a categoria do produto?'))
    nome = str(input('Qual o nome do produto?'))
    preco = float(input('Qual o valor do produto?'))



    produto = {
        'codigo':cod,
        'nome': nome,
        'categoria':cat,
        'preco':preco
    }
    produtos.append(produto)

def listar_produtos():
    if len(produtos) == 0:
     print('Não há produtos na lista')
     return

    if len(produtos) > 0:
     print('Os produtos são:')

    for produto in produtos:
     print(f"Código do produto: {produto['codigo']}")
     print(f"Produto: {produto['nome']}")
     print(f"Categoria: {produto['categoria']}")
     print(f"Preço: R${produto['preco']:.2f}")



def buscar_produtos():

    if len(produtos) == 0:
      print('Não foi possível buscar o produto pois não há nenhum produto cadastrado')
      return
    search = int(input('Qual o código do produto que deseja buscar?'))
    for produto in produtos:
       if produto['codigo'] == search:
         print('Produto encontrado!')
         print(produto['nome'])
         return

    print('O produto não foi encontrado')


def atualizar_produtos():
    if len(produtos) == 0:
     print('Não há nenhum produto cadastrado')
     return

    old_code = int(input('Qual o código do produto que deseja atualizar?'))
    new_code = int(input('Qual o código do produto que deseja adicionar na lista?'))

    for i, produto in enumerate(produtos):
     if produto['codigo'] == old_code:
        produto['codigo'] = new_code
        cat = str(input('Qual a categoria do novo produto?'))
        name = str(input('Qual o nome do novo produto?'))
        price = float(input(f'Qual o preço do {name}?'))
        produto['categoria'] = cat
        produto['nome'] = name
        produto['preco'] = price
        return

    print('Produto não encontrado')

def excluir_produto():

    if len(produtos) == 0:
        print('Não há produtos cadastrados')

    else:
     excluir = int(input('Qual o código do produto que deseja excluir?'))
     for i, produto in enumerate(produtos):

        if excluir == produto['codigo']:
            produtos.pop(i)
            print('Produto excluído com sucesso')
            return

     print('O produto não foi encontrado')


while option != 6:

    print('1- cadastrar produto\n2- listar produtos\n3- buscar produtos\n4- atualizar produto\n5- excluir produto\n6- sair')
    option = int(input('o que deseja fazer?'))

    if option == 1:
        cadastrar_produto()

    elif option == 2:
        listar_produtos()

    elif option == 3:
        buscar_produtos()

    elif option == 4:
        atualizar_produtos()

    elif option == 5:
        excluir_produto()

    elif option == 6:
        print('Programa encerrado')


