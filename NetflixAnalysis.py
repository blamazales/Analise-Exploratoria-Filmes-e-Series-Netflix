# -*- coding: utf-8 -*-
"""DesafioSquad2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DlHpLzuPWiAc4dIhicYYR0CoBZD-Hvut
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('/content/netflix_titles_nov_2019.csv')

"""Esse desafio tem como objetivo responder algumas perguntas através da análise de dados, aprofundando o conhecimento em frequência e medidas.
Os dados que deverão ser utilizado nesse script foram baixados do kaggle, e podem ser acessados através do link:

https://www.kaggle.com/code/shivamb/netflix-shows-and-movies-exploratory-analysis

Este conjunto de dados consiste na lista de fi lmes e suas respectivas e suas informações.

Variáveis:

● show_id - id único do filme/série.

● title - título do filme ou série

● director - diretor do filme ou série

● cast - elenco do filme ou série

● country - país do filme ou série

● date_added - data que foi adicionado no Netflix

● reading score - ano de lançamento original do filme

● rating - classificação da televisão

● duration - duração total do filme ou série.

● listed_in - categoria ou gênero do filme ou série.

● description -descrição do filme ou série.

● type - tipo de filme ou série

Os dados são arquivos em .csv.

### 1. Exploração inicial:
○ Quantas linhas e colunas tem o dataset?
"""

df.shape

print(f'O dataset tem {df.shape[0]} linhas e {df.shape[1]} colunas')

"""○ Quais são os tipos das variáveis e se há valores ausentes?"""

df.info

df.isna().sum()

"""### 2. Análises de frequência:
○ Qual a proporção de filmes vs. séries no catálogo?

"""

df.head()

total_linhas = df.shape[0]
total_linhas

total_filmes = df[df['type'] == 'Movie'].shape[0]
total_filmes

total_series = df[df['type'] == 'TV Show'].shape[0]
total_series

proporcao_filmes = (total_filmes / total_linhas) *100
proporcao_filmes

proporcao_series = (total_series / total_linhas) *100
proporcao_series

print(f'A proporção de filmes é de {proporcao_filmes:.2f}% e a proporção de séries é de {proporcao_series:.2f}%')

"""○ Qual o gênero mais frequente?"""

# Agrupa os gêneros e conta a frequência de cada um
cont_genero = df['listed_in'].str.split(', ', expand=True).stack().value_counts()
cont_genero

# Exibe o gênero mais frequente
print(f"O gênero mais frequente é: {cont_genero.index[0]} ({cont_genero.iloc[0]} vezes)")

"""### 3. Análises estatísticas:
○ Qual a média, mediana e moda do tempo de duração dos filmes?

"""

df.head()

# Crie um novo DataFrame apenas com as linhas que contêm filmes
df_filmes = df[df['type'] == 'Movie']

# Exiba as primeiras linhas do novo DataFrame para verificação
print(df_filmes.head())

# Converte a coluna 'duration' para numérico, tratando possíveis erros
df_filmes.loc[:, 'duration'] = df_filmes['duration'].astype(str).str.replace(' min', '').astype(float)

df_filmes.head()

media = df_filmes['duration'].mean()
media

mediana = df_filmes['duration'].median()
mediana

moda = df_filmes['duration'].mode()
moda

"""○ Qual o filme mais curto e mais longo?

"""

df_filmes.sort_values('duration').reset_index(drop=True)
df_filmes.head()

filme_longo = df_filmes.loc[df_filmes['duration'].idxmax()]
filme_longo

filme_curto = df_filmes.loc[df_filmes['duration'].idxmin()]
filme_curto

"""### 4. Visualização de dados:
○ Criar um gráfico de barras para mostrar a quantidade de títulos por gênero.

"""

# Contagem dos gêneros
cont_genero

# Criando o gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x=cont_genero.index, y=cont_genero.values)
plt.xticks(rotation=90)
plt.xlabel("Gêneros")
plt.ylabel("Quantidade de títulos")
plt.title("Quantidade de Títulos por Gênero")
plt.show()

"""○ Criar um histograma para analisar a distribuição da duração dos filmes."""

df_filmes.head()

# Criar o histograma da duração dos filmes
plt.figure(figsize=(12, 6))
sns.histplot(df_filmes['duration'], bins=20)

# Configurações do gráfico
plt.xlabel("Duração (minutos)")
plt.ylabel("Quantidade de títulos")
plt.title("Distribuição da duração dos filmes")
plt.show()

"""### Atividade extra:
● Quais são os 5 países que possuem mais produções no catálogo?
"""

# Contar a frequência de cada país
cont_paises = df['country'].value_counts()

# Obter os 5 países com mais produções
top_5 = cont_paises.head(5)

# Imprimir os resultados
print("Os 5 países com mais produções no catálogo são:")
top_5