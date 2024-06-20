import csv
import os
import pandas as pd

#Função para salvar um novo arquivo dos produtos
def salvar_produtos(produtos):
    with open('produtos.csv', mode='w' , newline='') as arquivo:
        nomes_campos = ['codigo', 'descricao', 'unidade', 'preco_custo', 'preco_venda','estoque']
        linhas = csv.DictWriter(arquivo, fieldnames = nomes_campos)
        linhas.writeheader()
        for linha in produtos:
            linhas.writerow(linha)

#Função para ler o arquivo produtos
def carregar_produtos():
    produtos = []
    if not os.path.exists('produtos.csv'):
        salvar_produtos(produtos)    
    with open('produtos.csv', mode='r') as arquivo:
        linhas = csv.DictReader(arquivo)
        for linha in linhas:
            produtos.append(linha)
    return produtos

#Função para buscar o ultimo codigo cadastrado para incluir um novo produto seguindo a sequencia dos codigos
def busca_ultimo_codigo(produtos):
    return int(produtos[-1]["codigo"]) + 1 if len(produtos) > 0 else 1

#Função para cadastrar um novo produto
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

#Função para ver se o produto existe , pode usar o descrição ou codigo
def validar_existencia_descricao(produtos , descricao_codigo):
    for linha in produtos:
        if linha['descricao'] == descricao_codigo or linha['codigo'] == descricao_codigo:
            return True
    return False

#Função para alterar um produto
def alterar_produto(produtos, codigo_descricao, **parametros):
    for index ,linha in enumerate(produtos):
        if linha['descricao'] == codigo_descricao or linha['codigo'] == codigo_descricao:
            produtos[index].update(parametros)
            salvar_produtos(produtos)
            return "Produto atualizado com sucesso!"             

#Função para excluir um produto
def deletar_produto(produtos, codigo_descricao):
    for index ,linha in enumerate(produtos):
        if linha['descricao'] == codigo_descricao or linha['codigo'] == codigo_descricao:
            del produtos[index]
            salvar_produtos(produtos)
            return "Produto removido com sucesso!"
        
def converter_preco(preco_str):
    return float(preco_str.replace(',', '.'))        

#Função para listar os produtos cadastrados
def listar_produto(produtos , tipo_ordenacao):
    if len(produtos) > 0: 
        if tipo_ordenacao == 'preco_venda':
            produtos_ordenados  = sorted(produtos, key=lambda x: converter_preco(x[tipo_ordenacao]))
        else:
            produtos_ordenados  = sorted(produtos, key=lambda x: x[tipo_ordenacao])  
        tabela = pd.DataFrame(produtos_ordenados)
        return tabela
    else:
        return 'Nenhum produto cadastrado'
    
#Função para buscar os produtos pela descrição
def buscar_produto(produtos , descricao):
    filtro = [item for item in produtos if descricao in item['descricao'].lower()]
    if len(filtro) > 0: 
        return pd.DataFrame(filtro)
    else:
        return 'Nenhum produto encontrado com essa descrição!'
