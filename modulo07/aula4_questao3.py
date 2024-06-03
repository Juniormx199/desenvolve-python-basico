
def ler_aquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        
        print("Primeiras 25 linhas do texto:")
        for linha in linhas[:25]:
            print(linha.strip())
        
        total_linhas = len(linhas)
        print(f"\nNumero total de linhas: {total_linhas}")
        
        maior_linha = max(linhas, key=len)
        print("\nLinha com maior numero de caracteres:")
        print(maior_linha.strip())
        
        nonato = sum(1 for line in linhas if "Nonato" in line or "nonato" in line)
        iria = sum(1 for line in linhas if "Íria" in line or "íria" in line)
        print(f"\nNumero de menções ao nome Nonato: {nonato}")
        print(f"Numero de menções ao nome Íria: {iria}")

ler_aquivo("estomago.txt")