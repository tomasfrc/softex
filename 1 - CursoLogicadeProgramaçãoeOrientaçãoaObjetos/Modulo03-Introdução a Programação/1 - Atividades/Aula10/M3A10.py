# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento 
# que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o 
# nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o
#  sistema informará o erro e continuará perguntando até que um valor correto 
#  preenchido.

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe 
# o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

print("Aluno: Tomás de Farias Ribeiro Caldas, Atividade referente ao módulo 3 aula 10")
nome = input("Por gentileza, informe o seu nome completo: ")
while True:
    try:
        idade = int(input("E por ultimo, gostaria de saber qual o seu ano de nascimento: "))
        if idade >= 1920 and idade <= 2021:
            idade_atual = 2022 - idade
        print(f"{nome},Você tem ou terá nesse ano: {idade_atual} ano(s).")
        
        break
    except:
        print("Ano de nascimento inválido")
        continue