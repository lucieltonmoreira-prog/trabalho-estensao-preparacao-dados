import pandas as pd

df = pd.read_excel(r'C:\Users\lucie\Downloads\Preparação de Dados (Respostas).xlsx')

# Limpando espaços em branco nos nomes das colunas para evitar erros
df.columns = df.columns.str.strip()

# selecionando somente as colunas que serão analisadas no Power BI
dicionario_colunas = {
    'Idade:': 'Faixa_Etaria_Original',
    '1. Qual é o seu nível de escolaridade?': 'Escolaridade',
    '4. Em sua juventude, você considerou fazer o ensino superior?': 'Considerou_Superior',
    '5. Quais dificuldades você acredita que podem impedir uma pessoa de fazer faculdade?': 'Barreiras_Acesso',
    '6. Você acredita que hoje está mais fácil acessar o ensino superior do que no passado?': 'Percepcao_Facilidade'
}

df.rename(columns=dicionario_colunas, inplace=True)

# criando uma coluna para dividir as gerações dentro do Power BI
df['Grupo_Geracional'] = df['Faixa_Etaria_Original']

colunas_selecionadas = [
    'Grupo_Geracional',
    'Escolaridade',
    'Considerou_Superior',
    'Barreiras_Acesso',
    'Percepcao_Facilidade'
]

df_final = df[colunas_selecionadas]

# criando uma coluna de contagem para facilitar no Power BI
df_final['Quantidade'] = 1

# Exportando para o Excel
df_final.to_excel('dados_principais_tratado.xlsx', index=False)

print("Arquivo 'dados_principais_tratado.xlsx' gerado com sucesso!")
print("Colunas incluídas:", df_final.columns.tolist())
