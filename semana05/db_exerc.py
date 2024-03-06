import pandas as pd


alunos_data = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Ana', 'Leandro', 'Isabelle', 'Paulo', 'Adrian'],
    'idade': [18, 27, 24, 29, 17],
    'curso': ['Engenharia', 'Matemática', 'Engenharia', 'Física', 'Química']
}
alunos_df = pd.DataFrame(alunos_data) #criando a tabela alunos e inserindo registros


todos_registros = alunos_df #consulta de todos os registros de alunos


nome_idade_acima_20 = alunos_df[['nome', 'idade']][alunos_df['idade'] > 20] #seleção de nome e idade de alunos com mais de 20 anos


curso_engenharia = alunos_df[alunos_df['curso'] == 'Engenharia'].sort_values(by='nome') #seleção dos alunos de engenharia em ordem alfabética


total_alunos = len(alunos_df) #total de alunos na tabela


alunos_df.loc[alunos_df['nome'] == 'Alice', 'idade'] = 19 #atualização da idade de um aluno na tabela


alunos_df = alunos_df.drop(alunos_df[alunos_df['id'] == 5].index) #remoção de um aluno pela id


clientes_data = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Giselle', 'Max', 'Henry', 'Naomi', 'John'],
    'idade': [35, 40, 28, 50, 45],
    'saldo': [1500.50, 3000.75, 800.20, 25000.30, 500.00]
}
clientes_df = pd.DataFrame(clientes_data) #criando a tabela de clientes e inserindo dados


clientes_idade_acima_30 = clientes_df[['nome', 'idade']][clientes_df['idade'] > 30] #seleção de clientes com idade acima de 30 anos


saldo_medio = clientes_df['saldo'].mean() #cálculo do saldo médio dos clientes


saldo_maximo = clientes_df.loc[clientes_df['saldo'].idxmax()] #cliente com saldo máximo


saldo_acima_1000 = len(clientes_df[clientes_df['saldo'] > 1000]) #quantidade de clientes com saldo acima de 1000


clientes_df.loc[clientes_df['nome'] == 'Gabriela', 'saldo'] = 3500.00 #atualização de saldo de cliente


clientes_df = clientes_df.drop(clientes_df[clientes_df['id'] == 5].index) #remoção de cliente pelo id


compras_data = {
    'id': [1, 2, 3, 4, 5],
    'cliente_id': [1, 3, 2, 4, 1],
    'produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
    'valor': [100.00, 150.00, 200.00, 80.00, 120.00]
}
compras_df = pd.DataFrame(compras_data) #criando a tabela compras e inserindo dados


nome_produto_valor = pd.merge(clientes_df, compras_df, left_on='id', right_on='cliente_id')[['nome', 'produto', 'valor']] #ixibir nome do cliente, produto e valor de cada compra

print("Alunos:")
print(todos_registros)
print("\nAlunos com mais de 20 anos:")
print(nome_idade_acima_20)
print("\nAlunos do curso de Engenharia:")
print(curso_engenharia)
print("\nQuantidade de alunos de Engenharia:", total_alunos)

print("\nClientes acima de 30 anos:")
print(clientes_idade_acima_30)
print("\nSaldo médio dos clientes:", saldo_medio)
print("\nCliente com saldo máximo:")
print(saldo_maximo)
print("\nClientes com saldo acima de 1000:", saldo_acima_1000)

print("\nCliente, produto e valor da compra:")
print(nome_produto_valor)
