# Aluno: Tomás de Farias Ribeiro Caldas
# Módulo 3 Aula 08

# Faça uma função calculadora de dois números com três parâmetros: 
# os dois primeiros serão os números da operação 
# e o terceiro será a entrada que definirá a operação a ser executada. 
# Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe 
# o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

def calculadora(numero1, numero2, operacao):
    if (operacao == 1):
        resultado = (numero1 + numero2)

    elif (operacao == 2):
        resultado = (numero1 - numero2)

    elif (operacao == 3):
        resultado = (numero1 * numero2)

    elif (operacao == 4):
        resultado = (numero1 / numero2)

    else:
        resultado = 0
        print("A operação registrada não é válida.")

    return resultado


n1 = float(input("Digite o primeiro valor da operação: "))
n2 = float(input("Digite o segundo valor da operação: "))
print("Catálogo de operações:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão")
n3 = int(input("Selecione a operação: "))

respostas = calculadora(n1, n2, n3)

print("O resultado da operação é: ", respostas)