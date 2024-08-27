# %%
import pandas as pd

# %%
file = 'empresaABC.xlsx'
df = pd.read_excel(file)
df.head()

# %%
df.info()

# %%
df_copy = df.copy()

# %%
df_copy = df_copy[df_copy.loc[:,"Identificação"].isna() == False]

# %%
df_copy.info()

# %%
df_copy.iloc[:5,:17]

# %%
df_copy.iloc[:5,17:]

# %% [markdown]
# ### As seguintes colunas vão ser as consideradas para a análise dos dados, visto que as outras ou não possuem dados suficientes ou não são relevantes para análise em uma forma geral:
# 
#     * Responsável pelo acionamento ABC	
# 
#     * Data da validação do orçamento	
# 
#     * ITEM LPU2	
# 
#     * Contratação	
# 
#     * Cidade	
# 
#     * UF	
# 
#     * STATUS	
# 
#     * Ação XYZ ou ABC	
# 
#     * Responsável\nXYZ	
# 
# 
# 

# %%
db = df_copy.iloc[:,[1, 2, 4, 5, 10, 11, 12, 13, 14]]

# %%
db

# %%
db.info()

# %%
for column in db.columns:
    print(db[column].unique())

# %%
db[db.loc[:,"Data da validação do orçamento"].isna() == True]

# %%
db[db.loc[:,"Ação XYZ ou ABC "].isna() == True]

# %%
df_original = df.copy()
df = db.copy()

# %%
import matplotlib.pyplot as plt

# 1. Distribuição do Status dos Projetos
plt.figure(figsize=(10, 6))
df['STATUS'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribuição do Status dos Projetos')
plt.xlabel('Status')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.show()

# 2. Validação de Orçamento ao Longo do Tempo
plt.figure(figsize=(10, 6))
df['Data da validação do orçamento'].value_counts().sort_index().plot(kind='line', marker='o', color='orange')
plt.title('Validação de Orçamento ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Quantidade de Validações')
plt.grid(True)
plt.show()

# 3. Contratação por Cidade
plt.figure(figsize=(10, 6))
df['Cidade'].value_counts().plot(kind='bar', color='purple')
plt.title('Distribuição de Contratações por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Contagem')
plt.xticks(rotation=90)
plt.show()


# %%



