<<<<<<< HEAD
import numpy as np

#Criando arrays
arr1 = np.random.random((4,3)) #4 linhas e 3 colunas com valores aleatórios
print(arr1)
print("---")


arr2 = np.random.randint(26, size=(3,5)) #3 linhas, 5 colunas, aleatórios e inteiros
print(arr2)
print("---")


arr3 = np.zeros((5, 10)) #5 linhas, 10 colunas e inicizados com zero
print(arr3)
print("---")


arr4 = np.arange(0, 90, 4) #entre 0 e 90 pulando de 4 em 4
print(arr4)
print("---")


arr5a = np.random.random((5, 7)) #reduzindo a uma dimensão
arr5b = arr5a.ravel()
print(arr5b)
print("---")


arr6 = np.random.randint(1, 31, size=(10, 4, 3)) #10 cartelas de bingo com 4 linhas e 3 colunas
print(arr6)
print("---")


arr7 = arr6.reshape(5, 4, 6) #reshape da cartela para ter 5 cartelas de 4 linhas e 6 colunas
print(arr7)
print("---")
print("---")


#Manipulando arrays
especies = np.array([[747, 89, 33, 5],
            [623, 123, 32, 13],
            [501, 22, 49, 2],
            [116, 101, 42, 10],
            [297, 56, 69, 22],
            [613, 64, 27, 7],
            [295, 84, 29, 14],
            [692, 105, 72, 16],
            [229, 103, 35, 5],
            [374, 124, 70, 1]])
print("---")


qtd_especies = especies[:, 1] #quantidade de espécies, segunda coluna
print(qtd_especies)
print("---")


print(qtd_especies[:3]) #3 primeiras quantidades
print("---")


print(qtd_especies[-5:]) #5 últimas quantidades de espécies
print("---")


tamanho = np.sort(especies[:, 3]) #tamanho das espécies por ordem crescente
print(tamanho)
print("---")


maior_especie = especies[especies[:, 3] == 22] #index boolean, array com os dados da maior espécie
print(maior_especie)
print("---")


especie297 = especies[especies[:, 0] == 297] #fancy index id 297
#mask especies[especie297]
print(especie297)
print("---")


especie_105_representantes = especies[np.where(especies[:, 1] == 105)] #dados da espécie com 105 representantes
print(especie_105_representantes)
print("---")


profundo = np.where(especies[:, 2] > 60, "Profundo", especies[:, 2]) #profundidade maior que 60 é substituído por Profundo
print(profundo)
print("---")


novas_especies = np.array([[204, 10, 40, 12], [392, 11, 81, 11]]) #adicionando dados de 2 espécies
especies = np.concatenate((especies, novas_especies))
print(especies)
print("---")


enxerga = np.array([0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]).reshape((12, 1)) #nova coluna que indica se o animal enxerga ou não
especies = np.concatenate((especies, enxerga), axis=1)
print(especies)
print("---")


#Calculando com arrays
acidentes = np.array([[1, 3, 2],
            [0, 1, 0],
            [2, 1, 4],
            [0, 0, 0],
            [1, 1, 0]])
print("---")


media_ultimos_dois_anos = np.mean(acidentes[:, -2:], axis=1) #cliente com acidentes abaixo da média
clientes_com_acidentes_abaixo_media = np.where(media_ultimos_dois_anos < np.mean(media_ultimos_dois_anos))
print(clientes_com_acidentes_abaixo_media)
print("---")


clientes_sem_acidentes_dois_anos = np.where(np.sum(acidentes[:, -2:], axis=1) == 0) #cliente que teve pelo menos 2 anos sem cometer acidentes
print(clientes_sem_acidentes_dois_anos)
print("---")


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])
resultado = 3 * x + 2 * y + x * y
print(resultado)
print("---")


notas_trabalhos = np.array([1, 2, 1]) #nota adicionada a cada prova
acidentes_notas_trabalhos = acidentes + notas_trabalhos #estudante = linha e coluna = prova
print(acidentes_notas_trabalhos)
print("---")
=======
import numpy as np

#Criando arrays
arr1 = np.random.random((4,3)) #4 linhas e 3 colunas com valores aleatórios
print(arr1)
print("---")


arr2 = np.random.randint(26, size=(3,5)) #3 linhas, 5 colunas, aleatórios e inteiros
print(arr2)
print("---")


arr3 = np.zeros((5, 10)) #5 linhas, 10 colunas e inicizados com zero
print(arr3)
print("---")


arr4 = np.arange(0, 90, 4) #entre 0 e 90 pulando de 4 em 4
print(arr4)
print("---")


arr5a = np.random.random((5, 7)) #reduzindo a uma dimensão
arr5b = arr5a.ravel()
print(arr5b)
print("---")


arr6 = np.random.randint(1, 31, size=(10, 4, 3)) #10 cartelas de bingo com 4 linhas e 3 colunas
print(arr6)
print("---")


arr7 = arr6.reshape(5, 4, 6) #reshape da cartela para ter 5 cartelas de 4 linhas e 6 colunas
print(arr7)
print("---")
print("---")


#Manipulando arrays
especies = np.array([[747, 89, 33, 5],
            [623, 123, 32, 13],
            [501, 22, 49, 2],
            [116, 101, 42, 10],
            [297, 56, 69, 22],
            [613, 64, 27, 7],
            [295, 84, 29, 14],
            [692, 105, 72, 16],
            [229, 103, 35, 5],
            [374, 124, 70, 1]])
print("---")


qtd_especies = especies[:, 1] #quantidade de espécies, segunda coluna
print(qtd_especies)
print("---")


print(qtd_especies[:3]) #3 primeiras quantidades
print("---")


print(qtd_especies[-5:]) #5 últimas quantidades de espécies
print("---")


tamanho = np.sort(especies[:, 3]) #tamanho das espécies por ordem crescente
print(tamanho)
print("---")


maior_especie = especies[especies[:, 3] == 22] #index boolean, array com os dados da maior espécie
print(maior_especie)
print("---")


especie297 = especies[especies[:, 0] == 297] #fancy index id 297
#mask especies[especie297]
print(especie297)
print("---")


especie_105_representantes = especies[np.where(especies[:, 1] == 105)] #dados da espécie com 105 representantes
print(especie_105_representantes)
print("---")


profundo = np.where(especies[:, 2] > 60, "Profundo", especies[:, 2]) #profundidade maior que 60 é substituído por Profundo
print(profundo)
print("---")


novas_especies = np.array([[204, 10, 40, 12], [392, 11, 81, 11]]) #adicionando dados de 2 espécies
especies = np.concatenate((especies, novas_especies))
print(especies)
print("---")


enxerga = np.array([0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]).reshape((12, 1)) #nova coluna que indica se o animal enxerga ou não
especies = np.concatenate((especies, enxerga), axis=1)
print(especies)
print("---")


#Calculando com arrays
acidentes = np.array([[1, 3, 2],
            [0, 1, 0],
            [2, 1, 4],
            [0, 0, 0],
            [1, 1, 0]])
print("---")


media_ultimos_dois_anos = np.mean(acidentes[:, -2:], axis=1) #cliente com acidentes abaixo da média
clientes_com_acidentes_abaixo_media = np.where(media_ultimos_dois_anos < np.mean(media_ultimos_dois_anos))
print(clientes_com_acidentes_abaixo_media)
print("---")


clientes_sem_acidentes_dois_anos = np.where(np.sum(acidentes[:, -2:], axis=1) == 0) #cliente que teve pelo menos 2 anos sem cometer acidentes
print(clientes_sem_acidentes_dois_anos)
print("---")


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])
resultado = 3 * x + 2 * y + x * y
print(resultado)
print("---")


notas_trabalhos = np.array([1, 2, 1]) #nota adicionada a cada prova
acidentes_notas_trabalhos = acidentes + notas_trabalhos #estudante = linha e coluna = prova
print(acidentes_notas_trabalhos)
print("---")
>>>>>>> origin/main
