# Aluno: Tomás de Farias Ribeiro Caldas
# Módulo 3 Aula09

# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
# No início, o programa mostrará a seguinte lista de operações:
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
# Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, 
# o sistema irá parar. 

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o 
# link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.  

def soma(num1, num2, soma):
    soma = num1 + num2
    print('Resuldado =', soma)
    return soma


def subtracao(num1, num2, subtracao):
    subtracao = num1 - num2
    print('Resuldado =', subtracao)
    return subtracao


def multiplicacao(num1, num2, multiplicacao):
    multiplicacao = num1 * num2
    print('Resuldado =', multiplicacao)
    return multiplicacao


def divisao(num1, num2, divisao):
    divisao = num1 / num2
    print('Resuldado =', divisao)
    return divisao

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
print('Sabendo que: \n 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão \n 0: Sair')
operador = str(input('Digite o valor correspondente a operação que deseja realizar: '))

while operador != 0:
    if '1' in operador:
        soma(num1, num2, soma)
        break
    elif '2' in operador:
        subtracao(num1, num2, subtracao)
        break
    elif '3' in operador:
        multiplicacao(num1, num2, multiplicacao)
        break
    elif '4' in operador:
        divisao(num1, num2, divisao)
        break
    elif '0' in operador:
        print('Saindo de calculadora')
        break
    else:
        print('# ERROR #')
        break