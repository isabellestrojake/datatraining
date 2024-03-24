import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


df = pd.read_csv("populacao_brasileira.csv")


prob_nao_fluente = 1 - df[df['nível de proficiência em inglês'] == 'Avançado'].shape[0] / df.shape[0]


prob_renda_superior = df[(df['estado'].isin(['AL', 'PA'])) & (df['renda'] > 5000)].shape[0] / df[(df['estado'].isin(['AL', 'PA']))].shape[0]


prob_superior_amazonas = df[(df['estado'] == 'AM') & (df['escolaridade'] == 'Superior')].shape[0] / df[df['estado'] == 'AM'].shape[0]


faixa_renda = int(df['renda'].max() // 1500 + 1) #convertendo em número inteiro para evitar problemas
densidade_probabilidade, bins = np.histogram(df['renda'], bins=faixa_renda, density=True)


media_renda = df['renda'].mean()
variancia_renda = df['renda'].var()
std_renda = np.sqrt(variancia_renda)
x = np.linspace(df['renda'].min(), df['renda'].max(), 1000)
pdf_renda = norm.pdf(x, media_renda, std_renda)


prob_pos_graduacao = df[df['escolaridade'] == 'Pós-graduação'].shape[0] / df.shape[0]
prob_amostral = 243000 / 1000000
probabilidade_final = prob_amostral / prob_pos_graduacao


densidade_acumulada = df['escolaridade'].value_counts(normalize=True).sort_index().cumsum()


n_ingles_intermediario = df[df['nível de proficiência em inglês'] == 'Intermediário'].shape[0]
margem_erro = 1.96 * np.sqrt((prob_nao_fluente * (1 - prob_nao_fluente)) / n_ingles_intermediario)


prob_60_pessoas = norm.cdf(media_renda + 1000, media_renda, std_renda) - norm.cdf(media_renda, media_renda, std_renda)


prob_sudeste_homem = df[(df['estado'].isin(['SP', 'RJ', 'MG', 'ES'])) & (df['sexo'] == 'M') & (df['escolaridade'] == 'Fundamental') & (df['renda'] > 2000)].shape[0] / df[(df['estado'].isin(['SP', 'RJ', 'MG', 'ES']))].shape[0]


print("1. Probabilidade complementar de ser fluente em inglês:", prob_nao_fluente)
print("2. Probabilidade de renda superior a 5 mil reais em Alagoas ou Pará:", prob_renda_superior)
print("3. Probabilidade de uma pessoa ter ensino superior completo no Amazonas:", prob_superior_amazonas)
print("4. Faixa de renda mais comum e função densidade de probabilidade:")
print("   Faixa mais comum de renda:", bins[np.argmax(densidade_probabilidade)], "-", bins[np.argmax(densidade_probabilidade) + 1])
print("5. Média da renda da amostra:", media_renda)
print("   Variância da renda da amostra:", variancia_renda)
print("   Distribuição normal da renda (gráfico incluído)")
plt.plot(x, pdf_renda)
plt.title('Distribuição Normal da Renda')
plt.xlabel('Renda')
plt.ylabel('Densidade de Probabilidade')
plt.show()
print("6. Probabilidade de encontrar 243 mil pessoas com pós-graduação em uma amostra de 1 milhão:", probabilidade_final)
print("7. Função de densidade acumulada para cada nível de escolaridade:\n", densidade_acumulada)
print("8. Margem de erro amostral da proporção populacional de pessoas com nível de inglês intermediário:", margem_erro)
print("9. Probabilidade de encontrar 60 pessoas com renda mil reais superior à média:", prob_60_pessoas)
print("10. Probabilidade de escolher alguém do Sudeste, homem, com ensino fundamental e renda maior que 2 mil reais por mês:", prob_sudeste_homem)
