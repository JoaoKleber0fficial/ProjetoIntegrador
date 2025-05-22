import streamlit as st
import pandas as pd

st.set_page_config(page_title="Insight: Entrevista x Aprovação", layout="wide")
st.title("📊 Insight: Entrevista Concluída x Aprovado na Entrevista")

# Carrega CSV
df = pd.read_csv("processos_seletivos_filtrado.csv")
df.columns = df.columns.str.strip()

# Seleciona colunas e limpa nulos
df = df[['Entrevista Concluída?', 'Aprovado na Entrevista']].dropna()

# Limpa strings para evitar erros (remove espaços e padroniza maiúsculas)
df['Entrevista Concluída?'] = df['Entrevista Concluída?'].str.strip().str.title()
df['Aprovado na Entrevista'] = df['Aprovado na Entrevista'].str.strip().str.title()

# Agrupa e cria tabela pivot
tabela = df.groupby(['Entrevista Concluída?', 'Aprovado na Entrevista']).size().unstack(fill_value=0)

# Renomeia índice para legibilidade no gráfico
tabela.index = ['Entrevista Não', 'Entrevista Sim']

# st.subheader("📋 Tabela de Frequência")
# st.dataframe(tabela)

# Calcula total de alunos entrevistados e não entrevistados
totais_entrevista = tabela.sum(axis=1)
totais_entrevista.name = "Total Alunos"

# st.subheader("📈 Total de alunos por status de entrevista")
# st.dataframe(totais_entrevista)

st.subheader("📊 Gráfico - Entrevista")
st.bar_chart(tabela.loc['Entrevista Sim'])

# =================================================================================================================================================== #

st.title("📊 Gráfico: Etapa de Desqualificação")

# Carrega o CSV
df = pd.read_csv("processos_seletivos_filtrado.csv")
df.columns = df.columns.str.strip()

# Filtra e limpa os dados
df = df[['Etapa de Desqualificação']].dropna()
df['Etapa de Desqualificação'] = df['Etapa de Desqualificação'].str.strip().str.title()

# Conta a quantidade de cada etapa
contagem = df['Etapa de Desqualificação'].value_counts().sort_values(ascending=False)

# st.subheader("📋 Quantidade por Etapa de Desqualificação")
contagem_df = contagem.reset_index()
contagem_df.columns = ['Etapa', 'Quantidade']
# st.dataframe(contagem_df) 

# Mostra o gráfico corrigido
st.subheader("📊 Gráfico de Barras - Etapas de Desqualificação")
st.bar_chart(contagem_df.set_index('Etapa'))

# ================================================================================================================================================== #

st.title("📊 Status do Processo (apenas Formulário Socioeconômico)")

# Carrega o CSV
df = pd.read_csv("processos_seletivos_filtrado.csv")
df.columns = df.columns.str.strip()  # Remove espaços invisíveis

# 🔁 USE OS NOMES CORRETOS AQUI:
df['Etapa de Desqualificação'] = df['Etapa de Desqualificação'].astype(str).str.strip().str.title()
df['Status do Processo'] = df['Status do Processo'].astype(str).str.strip().str.title()

# Filtra apenas a etapa do formulário socioeconômico
df_socio = df[df['Etapa de Desqualificação'] == 'Formulário Socioeconômico']

# Conta os status do processo
status_counts = df_socio['Status do Processo'].value_counts()

# Exibe o gráfico
st.subheader("📊 Gráfico de Barras - Status do Processo (Formulário Socioeconômico)")
st.bar_chart(status_counts)

st.title("📊 Status do Processo (Formulário Socioeconômico)")

# Carrega o CSV
df = pd.read_csv("processos_seletivos_filtrado.csv")
df.columns = df.columns.str.strip()  # Remove espaços invisíveis

# 🔁 USE OS NOMES CORRETOS AQUI:
df['Etapa de Desqualificação'] = df['Etapa de Desqualificação'].astype(str).str.strip().str.title()
df['Status do Processo'] = df['Status do Processo'].astype(str).str.strip().str.title()

# Filtra apenas a etapa do formulário socioeconômico
df_socio = df[df['Etapa de Desqualificação'] == 'Entrevista de Engajamento']

# Conta os status do processo
status_counts = df_socio['Status do Processo'].value_counts()

# Exibe o gráfico
st.subheader("📊 Gráfico de Barras - Status do Processo (Formulário Socioeconômico)")
st.bar_chart(status_counts)