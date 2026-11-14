
import csv

caminho_arquivo = 'publicacoes.csv'

def calcular_taxa_engajamento(
        impressoes: int,
        engajamentos: int
        
) -> float:
    
    """
    Calcula taxa de engajamento
    """
    
    if impressoes > 0:
        tx_engajamento = (engajamentos / impressoes)*100
    else: 
        tx_engajamento = 0

    return tx_engajamento

def analisar_publicacoes () -> dict:

    """
    Analisa as métricas das publicações de uma plataforma.
    """

    qtd_publicacoes = 0
    impressoes = 0
    engajamentos = 0

    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        publicacoes = csv.DictReader(arquivo)

        for linha in publicacoes:
            qtd_publicacoes += 1 
            impressoes += int(linha["impressoes"])
            engajamentos += int(linha["engajamentos"])

        tx_engajamento = calcular_taxa_engajamento(impressoes, engajamentos)

    resultado: dict = {
        "Publicações": qtd_publicacoes,
        "Impressões": impressoes,
        "Engajamentos": engajamentos,
        "Taxa de engajamento": tx_engajamento
    }

    return resultado

resultado_analise = analisar_publicacoes()
print(resultado_analise)
