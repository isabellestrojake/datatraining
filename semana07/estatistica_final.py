import pandas as pd



df = pd.read_json("enem_2023.json") #lendo o arquivo json
print(df)
df_numeric = df.apply(pd.to_numeric, errors='coerce') #convertendo todas as colunas para números para evitar erros na resolução
df_numeric = df_numeric.drop(columns=['Sexo']) #excluindo a coluna sexo antes de calcular a média para evitar erros na resolução


df.iloc[:, 4:] = df.iloc[:, 4:].apply(pd.to_numeric, errors='coerce')
amplitude_por_disciplina = df.max() - df.min()
disciplina_maior_amplitude = amplitude_por_disciplina.idxmax()
maior_amplitude = amplitude_por_disciplina.max()
print(f"A disciplina com a maior amplitude de nota é '{disciplina_maior_amplitude}' "
      f"com uma amplitude de {maior_amplitude:.2f}.")


media_por_disciplina = df_numeric.mean()
print("\n1. Média por disciplina:")
print(media_por_disciplina)


mediana_por_disciplina = df_numeric.median()
print("\n2. Mediana por disciplina:")
print(mediana_por_disciplina)


desvio_padrao_por_disciplina = df_numeric.std()
print("\n3. Desvio padrão por disciplina:")
print(desvio_padrao_por_disciplina)


amplitude_por_disciplina = df_numeric.max() - df_numeric.min()
print("\n4. Amplitude por disciplina:")
print(amplitude_por_disciplina)


df_sem_nan = df_numeric.dropna() #exclusão de linhas com valores ausentes
media_sem_nan = df_sem_nan.mean(axis=1)
print("\n5. Média das notas dos alunos sem valores ausentes:")
print(media_sem_nan)


top_500 = df_sem_nan.head(500) #seleção dos 500 primeiros alunos
media_top_500 = top_500.mean().sum()
print("\n6. Média das notas dos top 500 alunos:")
print(media_top_500)


media_total = df_numeric.mean().mean()
print("\n7. Média das notas de todos os alunos (incluindo NaN):")
print(media_total)


total_alunos = df_numeric.shape[0]
print("\n8. Total de alunos:")
print(total_alunos)


alunos_com_nan = df_numeric.shape[0] - df_sem_nan.shape[0]
print("\n9. Número de alunos com pelo menos uma nota faltante:")
print(alunos_com_nan)


porcentagem_alunos_com_nan = (alunos_com_nan / total_alunos) * 100
print("\n10. Porcentagem de alunos com pelo menos uma nota faltante:")
print(f"{porcentagem_alunos_com_nan:.2f}%")
