import pandas as pd

df = pd.DataFrame({
    'nome': ['yasmin', 'íris', 'lucas', 'guilherme', 'vitor', 'ana', 'carol'],
    'idade': [20, 21, 22, 23, 24, 25, 26],
    'nota': [9.5, 8.0, 7.5, 6.0, 5.5, 4.0, 3.5]
})

print(f'média de notas: {df["nota"].mean()}')

print(df.loc[df['nota'] > 7, ['nome', 'nota']])

print(df.loc[0])
print(df.iloc[0])

'''
Saída:

média de notas: 6.285714285714286

     nome  nota
0  yasmin   9.5
1    íris   8.0
2   lucas   7.5

nome     yasmin
idade        20
nota        9.5
Name: 0, dtype: object

nome     yasmin
idade        20
nota        9.5
Name: 0, dtype: object

Explicação da diferença entre loc e iloc: Apesar de ambos os métodos retornarem o mesmo resultado nesse caso, enquanto o .loc acessa os dados com base no índice do DataFrame, o .iloc acessa os dados com base em sua posição numérica, independentemente de seu índice.
'''