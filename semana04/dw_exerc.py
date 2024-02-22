<<<<<<< HEAD
import pandas as pd 
import numpy as np

df = pd.read_csv("collected research people.csv")


#Data Wrangling
df = df.drop(columns=['Unnamed: 0']) #retirando a coluna desnecessária "unnamed"
cols_novas = {'Endereerço': 'Endereço',
              'phone': 'Telefone',
              'anual_income': 'Renda Anual',
              'n_filhos': 'No. Filhos',
              'diariamente_sun blocker': 'Usa protetor solar diariamente',
              'Food_restrictions': 'Restrição Alimentar',
              'streaming': 'Streaming'
}
df.rename(columns=cols_novas, inplace=True) #nome corrigido das colunas
print(df.head)
print('----')
df.Nome = df.Nome.str.replace('[^a-zA-Zà-úÀ-Ú0-9 ]', '') #retirar os caracteres especiais
print(df.Nome)
print('----')
df.Telefone = df.Telefone.str.replace('[^0-9() -+]', '') #consertando telefone
df.loc[df.Telefone.str.contains('[*]', na=False), 'Telefone'] = np.nan
print(df['Telefone'])
print('----')
df['Estado Civil'] = df['Estado Civil'].replace({ #consertando estado civil
              'S': 'Solteiro',
              'C': 'Casado',
              'D': 'Divorciado',
              'V': 'Viúvo'
})
print(df['Estado Civil'])
print('----')


#Cenário 1, construtora quer saber possíveis compradores
df_carri = df.copy()
drop_carri = {'Restrição Alimentar',
              'Streaming',
              'Usa protetor solar diariamente',
              'Quantidade de Livros Comprados',
              'Autor Favorito'
}
df_carri.drop(columns=drop_carri, inplace=True) #tirando colunas desnecessárias para essa análise
df_carri['Minha Casa Minha Vida'] = True #quem pode participar do programa
print(df_carri['Minha Casa Minha Vida'])
print('----')
#df_carri['Investimento'] = np.where((df_carri.Moradia == "Quitada") | (df_carri.Moradia == "Financiamento", True, False)) #possíveis compradores


#Cenário 2, empresas de Streaming com maior retorno de investimento
df_hillo = df.copy()
df_hillo = df_hillo.drop(columns={'Moradia', #retirando colunas desnecessárias apara a análise
                                  'Restrição Alimentar',
                                  'Usa protetor solar diariamente',
                                  'Vai na Praia Mensalmente',
                                  'Faz Academia',
                                  'Compra e Lê Livros Todos os Anos',
                                  'Quantidade de Livros Comprados',
                                  'Autor Favorito'
})
print(df_hillo.head)
print('----')
df_hillo_stream = df_hillo['Streaming'].str.get_dummies(sep=' e ')
df_hillo.Streaming = df_hillo.Streaming.replace({"Todos": "Globo Play e Netflix e HBO e Disney Plus e Crunchroll"})
df_hillo.Streaming = df_hillo.Streaming.replace({"Netflix e Disney": "Netflix e Disney Plus"})
df_hillo = pd.concat([df_hillo, df_hillo_stream], axis=1) #melhorando a df
print(df_hillo.head)
print('----')


#Cenário 3, análise de propostas de empreendimentos
df_inf = df.copy()
df_inf = df_inf.drop(columns={'Moradia', 'Streaming'})
restricao = df_inf['Restrição Alimentar'].str.get_dummies(sep=' e ').drop(columns=['Nenhuma'])
df_inf = pd.concat([df_inf, restricao], axis=1) #melhorando a df
print(df_inf.head)
=======
import pandas as pd 
import numpy as np

df = pd.read_csv("collected research people.csv")


#Data Wrangling
df = df.drop(columns=['Unnamed: 0']) #retirando a coluna desnecessária "unnamed"
cols_novas = {'Endereerço': 'Endereço',
              'phone': 'Telefone',
              'anual_income': 'Renda Anual',
              'n_filhos': 'No. Filhos',
              'diariamente_sun blocker': 'Usa protetor solar diariamente',
              'Food_restrictions': 'Restrição Alimentar',
              'streaming': 'Streaming'
}
df.rename(columns=cols_novas, inplace=True) #nome corrigido das colunas
print(df.head)
print('----')
df.Nome = df.Nome.str.replace('[^a-zA-Zà-úÀ-Ú0-9 ]', '') #retirar os caracteres especiais
print(df.Nome)
print('----')
df.Telefone = df.Telefone.str.replace('[^0-9() -+]', '') #consertando telefone
df.loc[df.Telefone.str.contains('[*]', na=False), 'Telefone'] = np.nan
print(df['Telefone'])
print('----')
df['Estado Civil'] = df['Estado Civil'].replace({ #consertando estado civil
              'S': 'Solteiro',
              'C': 'Casado',
              'D': 'Divorciado',
              'V': 'Viúvo'
})
print(df['Estado Civil'])
print('----')


#Cenário 1, construtora quer saber possíveis compradores
df_carri = df.copy()
drop_carri = {'Restrição Alimentar',
              'Streaming',
              'Usa protetor solar diariamente',
              'Quantidade de Livros Comprados',
              'Autor Favorito'
}
df_carri.drop(columns=drop_carri, inplace=True) #tirando colunas desnecessárias para essa análise
df_carri['Minha Casa Minha Vida'] = True #quem pode participar do programa
print(df_carri['Minha Casa Minha Vida'])
print('----')
#df_carri['Investimento'] = np.where((df_carri.Moradia == "Quitada") | (df_carri.Moradia == "Financiamento", True, False)) #possíveis compradores


#Cenário 2, empresas de Streaming com maior retorno de investimento
df_hillo = df.copy()
df_hillo = df_hillo.drop(columns={'Moradia', #retirando colunas desnecessárias apara a análise
                                  'Restrição Alimentar',
                                  'Usa protetor solar diariamente',
                                  'Vai na Praia Mensalmente',
                                  'Faz Academia',
                                  'Compra e Lê Livros Todos os Anos',
                                  'Quantidade de Livros Comprados',
                                  'Autor Favorito'
})
print(df_hillo.head)
print('----')
df_hillo_stream = df_hillo['Streaming'].str.get_dummies(sep=' e ')
df_hillo.Streaming = df_hillo.Streaming.replace({"Todos": "Globo Play e Netflix e HBO e Disney Plus e Crunchroll"})
df_hillo.Streaming = df_hillo.Streaming.replace({"Netflix e Disney": "Netflix e Disney Plus"})
df_hillo = pd.concat([df_hillo, df_hillo_stream], axis=1) #melhorando a df
print(df_hillo.head)
print('----')


#Cenário 3, análise de propostas de empreendimentos
df_inf = df.copy()
df_inf = df_inf.drop(columns={'Moradia', 'Streaming'})
restricao = df_inf['Restrição Alimentar'].str.get_dummies(sep=' e ').drop(columns=['Nenhuma'])
df_inf = pd.concat([df_inf, restricao], axis=1) #melhorando a df
print(df_inf.head)
>>>>>>> origin/main
print('----')