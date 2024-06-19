import csv
import os
import pandas as pd

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
    return int(produtos[-1]["codigo"]) + 1 if len(produtos) > 0 else 1

def criar_produto(produtos, descricao, unidade, preco_custo, preco_venda , estoque):
    list(produtos)
    codigo = busca_ultimo_codigo(produtos)
    produtos.append({
        'codigo': codigo,
        'descricao': descricao,
        'unidade': unidade,
        'preco_custo': preco_custo,
        'preco_venda': preco_venda,
        'estoque': estoque
    })
    salvar_produtos(produtos)
    return f"Produto criado com sucesso! \nCodigo do produto: {codigo}"

def validar_existencia_descricao(produtos , descricao_codigo):
    for linha in produtos:
        if linha['descricao'] == descricao_codigo or linha['codigo'] == descricao_codigo:
            return True
    return False

def alterar_produto(produtos, codigo_descricao, **parametros):
    for index ,linha in enumerate(produtos):
        if linha['descricao'] == codigo_descricao or linha['codigo'] == codigo_descricao:
            produtos[index].update(parametros)
            salvar_produtos(produtos)
            return "produto atualizado com sucesso!"             

def deletar_produto(produtos, codigo_descricao):
    for index ,linha in enumerate(produtos):
        if linha['descricao'] == codigo_descricao or linha['codigo'] == codigo_descricao:
            del produtos[index]
            salvar_produtos(produtos)
            return "produto removido com sucesso!"

def listar_produto(produtos , tipo_ordenacao):
    tabela = pd.DataFrame(produtos)
    return tabela.sort_values(tipo_ordenacao)

def buscar_produto(produtos , descricao):
    filtro = [item for item in produtos if descricao in item['descricao'].lower()]
    if len(filtro) > 0: 
        return pd.DataFrame(filtro)
    else:
        return 'Nenhum produto encontrado com essa descrição!'
