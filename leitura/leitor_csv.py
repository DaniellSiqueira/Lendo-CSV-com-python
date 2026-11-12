
import csv

caminho_arquivo = 'publicacoes.csv'

with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        print(f"Plataforma: {linha['plataforma']}")
        print(f"Publicação: {linha['publicacao']}")
        print(f"Impressões: {linha['impressoes']}")
        print()