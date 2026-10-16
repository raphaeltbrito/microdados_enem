import pandas as pd

CAMINHO = r"C:\Users\thiag\Downloads\microdados_enem_2017\DADOS\MICRODADOS_ENEM_2017.csv"

df = pd.read_csv(CAMINHO, sep=";", encoding="latin-1", nrows=5)
count = 0
for coluna in df.columns:
    print(coluna)
    count += 1
print(count)