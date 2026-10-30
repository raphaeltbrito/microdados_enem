# Microdados do ENEM

Projeto da disciplina de Introdução a Ciência de Dados da UFPB no semestre 26.2, ministrada pelo professor Yuri Malheiros.
Participantes: Raphael Brito, Matheus Meira, Thiago Dias e Hugo Suassuna.

O conjunto de dados é disposto no site do gov.br em uma pasta com outras pastas dividas em "DADOS", "DICIONÁRIO", "INPUTS", "LEIA-ME E DOCUMENTOS TÉCNICOS" e "PROVAS E GABARITOS". Cada ano dos 16 avaliados tem quase a mesma estrutura, mas há algumas divergências em relação a não existir a coluna, como em 2009, ou ter colunas equivalentes, que possuem a mesma resposta mas com números ou nomes diferentes. <img width="1520" height="558" alt="image" src="https://github.com/user-attachments/assets/2ca7e9a1-51aa-42ca-a469-d0d925f192f2" />

Para coletarmos os dados que vamos manipular de fato, foi necessário a criação de um notebook para cada ano filtrando resultados nulos e as colunas que não fariam sentido para o nosso trabalho. Através da biblioteca pandas, usamos funções como ".read.csv" e ".to_csv" para leitura e criação dos dados limpos, respectivamente. 

Após todo o trabalho de coleta e processamento dos dados, criamos um Google Drive para acessar todos os arquivos dos anos manipulados. 

| Nome da coluna | Descrição da coluna | Exemplo |
|----------------|---------------------|---------|
| TP_SEXO | Sexo do participante | M |
| TP_COR_RACA | Cor/raça | Indígena |
| TP_FAIXA_ETARIA | Faixa etária | Entre 26 e 30 anos |
| SG_UF_PROVA | Estado que a prova foi aplicada | PB |
| TP_ESCOLA | Tipo de escola durante ensino médio | Pública|
| TP_ST_CONCLUSAO | Situação de conclusão do ensino médio | Já concluiu o ensino médio|
| NU_ANO | Ano do ENEM| 2023 |
| Q001 | Escolaridade do pai/responsável | Nunca estudou |
| Q002 | Escolaridade da mãe/responsável | Completou a pós-graduação |
| Q003 | Grupo que corresponde a ocupação do pai | Grupo 1: lavrador, pescador, lenhador...|
| Q004 | Grupo que corresponde a ocupação da mãe | Grupo 5: médico, engenheiro, delegado...|
| Q006 | Renda mensal familiar | De R$1.320,01 até R$1980,00|
| NU_NOTA_CN | Nota da prova de Ciências da Natureza| 702.1|
| NU_NOTA_CH | Nota da prova de Ciências Humanas| 658.3|
| NU_NOTA_LC | Nota da prova de Linguagens e Códigos| 615.3|
| NU_NOTA_MT | Nota da prova de Matemática| 897.5|
| NU_NOTA_REDACAO | Nota da prova de Redação| 800|
