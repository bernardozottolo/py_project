import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Carregar o arquivo Excel
file = 'empresaABC.xlsx'
df = pd.read_excel(file)

# Filtrar os dados
df_copy = df[df["Identificação"].notna()]
db = df_copy.iloc[:, [1, 2, 4, 5, 10, 11, 12, 13, 14]]

# Criar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div(children=[
    html.H1(children='Análise de Projetos da Empresa ABC'),

    # Gráfico 1: Distribuição do Status dos Projetos
    html.Div(children='''
        Distribuição do Status dos Projetos
    '''),
    dcc.Graph(
        id='status-projetos',
        figure=px.bar(df['STATUS'].value_counts(), labels={'index': 'Status', 'value': 'Contagem'}, title='Distribuição do Status dos Projetos')
    ),

    # Gráfico 2: Validação de Orçamento ao Longo do Tempo
    html.Div(children='''
        Validação de Orçamento ao Longo do Tempo
    '''),
    dcc.Graph(
        id='validacao-orcamento',
        figure=px.line(df['Data da validação do orçamento'].value_counts().sort_index(), labels={'index': 'Data', 'value': 'Quantidade de Validações'}, title='Validação de Orçamento ao Longo do Tempo')
    ),

    # Gráfico 3: Contratação por Cidade
    html.Div(children='''
        Distribuição de Contratações por Cidade
    '''),
    dcc.Graph(
        id='contratacao-cidade',
        figure=px.bar(df['Cidade'].value_counts(), labels={'index': 'Cidade', 'value': 'Contagem'}, title='Distribuição de Contratações por Cidade')
    ),
])

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)

# %%



