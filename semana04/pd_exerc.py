<<<<<<< HEAD
import pandas as pd
import numpy as np
from datetime import datetime


#Dataframe e ordenação
df = pd.read_csv('carros.csv') #lendo o arquivo csv
print(df.head(10)) #print com 10 linhas, adaptei para aparecer no meu terminal
print('---')
print(df.columns) #print colunas
print('---')
print(df.index) #print index
print('---')
print(df.sort_values('Quant Carros', ascending=False)) #ordem decrescente com o estado com maior quantidade de carros
proporcao = df['Quant Carros']/ df['População do Estado'] #proporção de carros por população
print('---')
df['Carros por habitante'] = proporcao #add nova coluna
print(df.head()) #checando a alteração
print('---')
df_est_hab = df[['Estado', 'Carros por habitante']] #criando dataframe com estados e proporção
print(df_est_hab)
print('---')


#Agregação de dados
df_concurso = pd.read_csv('dados_concurso.csv')
conversao_data = df_concurso['Data de Nascimento'] = pd.to_datetime(df_concurso['Data de Nascimento']) #convertendo a coluna de Data de Nascimento para datetime
idade = df_concurso['Idade'] = datetime.now().year - df_concurso['Data de Nascimento'].dt.year #calculando a idade
media_idade_regiao = df_concurso.groupby('Estado')['Idade'].mean() #média de idade
print(media_idade_regiao)
print('---')
escolaridade = df_concurso[['Estado', 'Escolaridade', 'Número de Inscrição']].groupby(['Estado', 'Escolaridade']).count()
print(escolaridade)
print('---')
porcentagem_deficiencia = df_concurso['Deficiência'].value_counts(normalize=True) * 100
print(porcentagem_deficiencia)
print('---')
media_pessoas_pi = df_concurso[df_concurso['Estado'] == 'PI']['Número de Inscrição'].count() #media de pessoas no Piauí
print(media_pessoas_pi)
print('---')


#Índice e fatiamento
qtd_piaui = df_concurso.loc[df_concurso['Estado'] == 'PI']
print(qtd_piaui)
print('---')
inscritos = df_concurso[['Número de Inscrição', 'Nome', 'Data de Nascimento']]
print(inscritos)
print('---')
nascidos_antes_95 = df_concurso['Data de Nascimento'].loc[df_concurso['Data de Nascimento'] < np.datetime64('1995')]
print(nascidos_antes_95)
print('---')
qtd_feminino_es = df_concurso.loc[(df_concurso['Estado'] == 'ES') & (df_concurso['Sexo'] == 'F')].shape[0] #quantidade de candidatas femininas no ES
print(qtd_feminino_es)
print('---')
ordernar_numero_inscricao = df_concurso.set_index('Data de Inscrição').sort_index()[:10] #ordernar a data de inscrição e mostrar os 10 primeiros
print(ordernar_numero_inscricao)
print('---')


#Valores faltosos
porcentagem_faltosos = df_concurso.isna().sum() #porcentagem de dados faltosos
print(porcentagem_faltosos)
print('---')
df_concurso = df_concurso.fillna('Falta informação') #colocando a mensagem em dados faltosos
print(df_concurso)
print('---')
=======
import pandas as pd
import numpy as np
from datetime import datetime


#Dataframe e ordenação
df = pd.read_csv('carros.csv') #lendo o arquivo csv
print(df.head(10)) #print com 10 linhas, adaptei para aparecer no meu terminal
print('---')
print(df.columns) #print colunas
print('---')
print(df.index) #print index
print('---')
print(df.sort_values('Quant Carros', ascending=False)) #ordem decrescente com o estado com maior quantidade de carros
proporcao = df['Quant Carros']/ df['População do Estado'] #proporção de carros por população
print('---')
df['Carros por habitante'] = proporcao #add nova coluna
print(df.head()) #checando a alteração
print('---')
df_est_hab = df[['Estado', 'Carros por habitante']] #criando dataframe com estados e proporção
print(df_est_hab)
print('---')


#Agregação de dados
df_concurso = pd.read_csv('dados_concurso.csv')
conversao_data = df_concurso['Data de Nascimento'] = pd.to_datetime(df_concurso['Data de Nascimento']) #convertendo a coluna de Data de Nascimento para datetime
idade = df_concurso['Idade'] = datetime.now().year - df_concurso['Data de Nascimento'].dt.year #calculando a idade
media_idade_regiao = df_concurso.groupby('Estado')['Idade'].mean() #média de idade
print(media_idade_regiao)
print('---')
escolaridade = df_concurso[['Estado', 'Escolaridade', 'Número de Inscrição']].groupby(['Estado', 'Escolaridade']).count()
print(escolaridade)
print('---')
porcentagem_deficiencia = df_concurso['Deficiência'].value_counts(normalize=True) * 100
print(porcentagem_deficiencia)
print('---')
media_pessoas_pi = df_concurso[df_concurso['Estado'] == 'PI']['Número de Inscrição'].count() #media de pessoas no Piauí
print(media_pessoas_pi)
print('---')


#Índice e fatiamento
qtd_piaui = df_concurso.loc[df_concurso['Estado'] == 'PI']
print(qtd_piaui)
print('---')
inscritos = df_concurso[['Número de Inscrição', 'Nome', 'Data de Nascimento']]
print(inscritos)
print('---')
nascidos_antes_95 = df_concurso['Data de Nascimento'].loc[df_concurso['Data de Nascimento'] < np.datetime64('1995')]
print(nascidos_antes_95)
print('---')
qtd_feminino_es = df_concurso.loc[(df_concurso['Estado'] == 'ES') & (df_concurso['Sexo'] == 'F')].shape[0] #quantidade de candidatas femininas no ES
print(qtd_feminino_es)
print('---')
ordernar_numero_inscricao = df_concurso.set_index('Data de Inscrição').sort_index()[:10] #ordernar a data de inscrição e mostrar os 10 primeiros
print(ordernar_numero_inscricao)
print('---')


#Valores faltosos
porcentagem_faltosos = df_concurso.isna().sum() #porcentagem de dados faltosos
print(porcentagem_faltosos)
print('---')
df_concurso = df_concurso.fillna('Falta informação') #colocando a mensagem em dados faltosos
print(df_concurso)
print('---')
>>>>>>> origin/main
