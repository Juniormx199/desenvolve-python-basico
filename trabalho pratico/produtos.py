import csv
import os
import pandas as pd

linha_estilo = lambda: print("-----------------------------------------")

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
            linha_estilo()
            print("Produto ja existe")
            linha_estilo()
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
    linha_estilo()
    print("produto criado com sucesso!")
    linha_estilo()

def alterar_produto(produtos, codigo_descricao, **parametros):
    for index ,linha in enumerate(produtos):
        if linha['descricao'] == codigo_descricao or linha['codigo'] == codigo_descricao:
            produtos[index].update(parametros)
            salvar_produtos(produtos)
            linha_estilo()
            print("produto atualizado com sucesso!")
            linha_estilo()
            return
    linha_estilo()    
    print("produto não encontrado")
    linha_estilo()
    return                  

def deletar_produto(produtos, codigo_descricao):
    for index ,linha in enumerate(produtos):
        if linha['descricao'] == codigo_descricao or linha['codigo'] == codigo_descricao:
            del produtos[index]
            salvar_produtos(produtos)
            linha_estilo()
            print("produto removido com sucesso!")
            linha_estilo()
            return
    linha_estilo()    
    print("produto não encontrado")
    linha_estilo()
    return        

def listar_produto(produtos , tipo_ordenacao):
      linha_estilo()
      print("Lista de produtos")
      tabela = pd.DataFrame(produtos)
      print(tabela.sort_values(tipo_ordenacao))
      linha_estilo()

def buscar_produto(produtos , descricao):
    filtro = [item for item in produtos if descricao in item['descricao'].lower()]
    tabela = pd.DataFrame(filtro)
    print(tabela)
