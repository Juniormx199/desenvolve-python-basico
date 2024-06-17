import csv
import os

def salvar_produtos(produtos):
    with open('produtos.csv', mode='w' , newline='') as arquivo:
        nomes_campos = ['codigo', 'descricao', 'unidade', 'preco_custo', 'preco_venda','estoque']
        linhas = csv.DictWriter(arquivo, fieldnames = nomes_campos)
        linhas.writeheader()
        for linha in produtos:
            linhas.writerow(linha)

def carregar_produtos():
    produtos = []
    if not os.path.exists('produtos.csv'):
        salvar_produtos(produtos)    
    with open('produtos.csv', mode='r') as arquivo:
        linhas = csv.DictReader(arquivo)
        for linha in linhas:
            produtos.append(linha)
    return produtos

produtos = carregar_produtos()

def busca_ultimo_codigo(produtos):
    if len(produtos) > 0:
        codigo = produtos[-1]["codigo"]
        return int(codigo) + 1
    else:
        return 1

def criar_produto(produtos, descricao, unidade, preco_custo, preco_venda , estoque):
    list(produtos)
    codigo = busca_ultimo_codigo(produtos)
    for linha in produtos:
        if linha['descricao'] == descricao:
            print("Produto ja existe")
            return
    produtos.append({
        'codigo': codigo,
        'descricao': descricao,
        'unidade': unidade,
        'preco_custo': preco_custo,
        'preco_venda': preco_venda,
        'estoque': estoque
    })
    salvar_produtos(produtos)
    print("produto criado com sucesso!")
#criar_produto(produtos, 'teste', 'unidade', 'preco_custo', 'preco_venda' , 'estoque')

def alterar_produto(produtos, codigo_descricao, **kwargs):
    for index ,linha in enumerate(produtos):
        if linha['descricao'] == codigo_descricao or linha['codigo'] == codigo_descricao:
            produtos[index].update(kwargs)
            salvar_produtos(produtos)
            print("produto atualizado com sucesso!")
            return
        
    print("produto não encontrado")
    return                  
#alterar_produto(produtos,'descricao',unidade ='UNI',descricao='item')

def deletar_produto(produtos, codigo_descricao):
    for index ,linha in enumerate(produtos):
        if linha['descricao'] == codigo_descricao or linha['codigo'] == codigo_descricao:
            del produtos[index]
            salvar_produtos(produtos)
            print("produto removido com sucesso!")
            return
        
    print("produto não encontrado")
    return        
#deletar_produto(produtos,'item')

def listar_produto(produtos):
      for produto in produtos:
        print(produto)


def buscar_produto(produtos , codigo_descricao):
    for produto in produtos:
        if produto['descricao'] == codigo_descricao or produto['codigo'] == codigo_descricao:
            print(produto)
            return
    return print('Produto não encontrado')
        
