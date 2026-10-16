import pandas as pd

def ler_dados_enem(caminho_arquivo):
    COLUNAS = [
    "TP_SEXO","TP_COR_RACA","TP_FAIXA_ETARIA","SG_UF_PROVA","Q007","Q023",
    "TP_ST_CONCLUSAO","NU_ANO","Q001","Q002","Q003","Q004",
    ]

    NOTAS = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT","NU_NOTA_REDACAO"]
    todas = COLUNAS + NOTAS

    # Lê apenas as colunas necessárias
    df = pd.read_csv(caminho_arquivo, sep=";", encoding="latin-1", usecols=todas)

    # Remove as linhas com valores nulos
    completos = df.dropna(subset=todas)

    print(f"Linhas lidas inicialmente: {len(df)}")
    print(f"Linhas retornadas (limpas e com notas): {len(completos)}")

    # Retorna apenas o resultado final
    return completos