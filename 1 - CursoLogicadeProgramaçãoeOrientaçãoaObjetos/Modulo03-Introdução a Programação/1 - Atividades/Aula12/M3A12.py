# Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”.
# O arquivo deve ter a seguinte estrutura:

# aluno: Nome do aluno;
# nota_1: Primeira nota;
# nota_2: Segunda nota;
# faltas: Número de faltas;

# O programa lerá esse arquivo e criará duas colunas. A primeira coluna 
# será “media”, que terá a média das duas notas do aluno. 
# A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

# O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado.
# O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

# Por fim, o programa deverá mostrar na tela:
# - o maior número de faltas;
# - a média geral das notas dos alunos;
# - e a maior média.

# Veja em anexo um exemplo do arquivo “notas_alunos.csv”.

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe 
# o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

import pandas as pd


table = {'aluno': ['aluno-1', 'aluno-2', 'aluno-3', 'aluno-4'],
        'nota-1': [7, 3, 9, 10],
        'nota-2': [7, 10, 4, 6],
        'faltas': [1, 7, 2, 9]
        }
df = pd.DataFrame(table)

df['media'] = df['nota-1'] + df['nota-2']
df['media'] = df['media'] / 2
df['Aprovação'] = 0

df.loc[df['media'] >= 7, 'Aprovação'] = "APROVADO"
df.loc[df['media'] < 7, 'Aprovação'] = "REPROVADO"
df.loc[df['faltas'] > 5, 'Aprovação'] = "REPROVADO"

media = df['media'].median()
falta = df['faltas'].max()
maiorMedia = df['media'].max()

print(df)

print('A média geral dos alunos foi: ' +str (media))
print('O maior numero de faltas foi: ' +str (falta))
print('A maior média foi: ' +str (maiorMedia))