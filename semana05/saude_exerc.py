import pandas as pd


df_saude = pd.read_csv('saude_do_sono_estilo_vida.csv')



df_saude.rename(columns={'ID': 'Identificador',
                   'Pressão sanguíneaaaa': 'Pressao_sanguinea',
                   'Ocupação': 'Profissao',
                   'Categoria BMI': 'Categoria_IMC'}, inplace=True) #Renomeando as colunas
print("Colunas renomeadas")
print("---")


df_saude['Duração do sono'] = df_saude['Duração do sono'].astype(str)
df_saude = df_saude[df_saude['Duração do sono'].str.isnumeric()]
df_saude['Duração do sono'] = pd.to_numeric(df_saude['Duração do sono'], errors='coerce')
mmm_prof = df_saude.groupby('Profissao')['Duração do sono'].agg(['mean', 'median', lambda x: x.mode()[0]]) #média, moda e mediana de horas por profissão
print("Média, moda e mediana de horas de sono para cada profissão:\n", mmm_prof)
print("---")


#total_eng_software = df_saude[df_saude['Profissao'] == 'Eng. de Software'].shape[0]
#obesos_eng_software = df_saude[(df_saude['Profissao'] == 'Eng. de Software') & (df_saude['Categoria_IMC'] == 'Obesidade')].shape[0]
#porcentagem_obesos = (obesos_eng_software / total_eng_software) * 100 #% obesos entre os engenheiros de software
#print("Porcentagem de obesos entre os engenheiros de software:\n", porcentagem_obesos)
#print("---")


adv_rep = df_saude[df_saude['Profissao'].isin(['Advogado', 'Representante de Vendas'])].groupby('Profissao')['Duração do sono'].mean() #advogados ou representantes de vendas dormem menos?
print("Média de horas de sono para advogados e representantes de vendas:\n", adv_rep)
print("---")


med_enf = df_saude[df_saude['Profissao'].isin(['Enfermagem', 'Medicina'])].groupby('Profissao')['Duração do sono'].mean() #quem entre médicos e enfermeiros dorme menos?
print("Média de horas de sono para médicos e enfermeiros:\n", med_enf)
print("---")


subconjunto = df_saude[['Identificador', 'Gênero', 'Idade', 'Pressao_sanguinea', 'Frequência cardíaca']] #id, gênero, idade, pressão sanguínea e frequência cardíaca
print("Subconjunto com Identificador, Gênero, Idade, Pressão sanguínea e Frequência cardíaca:\n", subconjunto)
print("---")


prof_menos_freq = df_saude['Profissao'].value_counts().idxmin() #profissão menos frequente
print("Profissão menos frequente:\n", prof_menos_freq)
print("---")


pres_sang = df_saude.groupby('Gênero')['Pressao_sanguinea'].mean().idxmax() #maior pressão sanguínea média entre mulheres e homens
print("Gênero com maior pressão sanguínea média:\n", pres_sang)
print("---")


oito_horas_dia = df_saude['Duração do sono'].mode()[0] == 8 #predominância em dormir oito horas por dia
print("Predominância de dormir 8 horas por dia:\n", oito_horas_dia)
print("---")


media_passos_acima_70 = df_saude[df_saude['Frequência cardíaca'] > 70]['Passos'].mean()
media_passos_abaixo_igual_70 = df_saude[df_saude['Frequência cardíaca'] <= 70]['Passos'].mean()
res_media = media_passos_acima_70 > media_passos_abaixo_igual_70 #pessoas com frequências cardíacas acima de 70 dão mais passos?
print("Média de passos para pessoas com frequências cardíacas acima de 70:\n", res_media)
