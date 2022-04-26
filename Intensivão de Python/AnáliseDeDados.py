import pandas as pd
import openpyxl
import numpy
import plotly.express as px
# Passo 1 - importar a base de dados pro python
# Axis = linha -> 0 / Coluna -> 1

tabela = pd.read_csv(r'C:\Users\Pichau\Downloads\telecom_users.csv')
# Remover uma coluna vazia
tabela = tabela.drop('Unnamed: 0', axis=1)

#print(tabela)
# Passo 2 - Visualizar a base de dados
# Entender a base de dados
# Descobrir as cagadas da base de dados
# Passo 3 - Tratamento de dados

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

# Passo 4 - Análise Global
# Número de clientes que cancelaram

print(tabela['Churn'].value_counts())

# Porcentagem dos clientes que cancelaram

print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# Passo 5 - Análise detalhada
# Criar o gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()
