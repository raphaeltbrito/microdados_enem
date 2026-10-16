<<<<<<< HEAD
import os
import pandas as pd

CAMINHO = r"C:\Users\thiag\Downloads\microdados_enem_2017\DADOS\MICRODADOS_ENEM_2017.csv"
SAIDA = "saida"

COLUNAS = [
    "TP_SEXO","TP_COR_RACA","TP_FAIXA_ETARIA","SG_UF_PROVA","Q007","Q023",
    "TP_ST_CONCLUSAO","NU_ANO","Q001","Q002","Q003","Q004",
]

NOTAS = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT","NU_NOTA_REDACAO"]
todas = COLUNAS + NOTAS
os.makedirs(SAIDA, exist_ok=True)

df = pd.read_csv(CAMINHO, sep=";", encoding="latin-1", usecols=todas)

df.to_csv(os.path.join(SAIDA, "enem_2017_organizado.csv"), index=False, sep=";")

completos = df.dropna(subset=todas)
completos.to_csv(os.path.join(SAIDA, "enem_2017_com_notas.csv"), index=False, sep=";")

print(f"Linhas no arquivo organizado: {len(df)}")
print(f"Linhas com as 4 notas: {len(completos)}")
=======
import pandas as pd

CAMINHO = r"C:\Users\thiag\Downloads\microdados_enem_2017\DADOS\MICRODADOS_ENEM_2017.csv"

df = pd.read_csv(CAMINHO, sep=";", encoding="latin-1", nrows=5)
count = 0
for coluna in df.columns:
    print(coluna)
    count += 1
print(count)
>>>>>>> ff3211db982db1707a60943ddcae96bb6c6f9b10
