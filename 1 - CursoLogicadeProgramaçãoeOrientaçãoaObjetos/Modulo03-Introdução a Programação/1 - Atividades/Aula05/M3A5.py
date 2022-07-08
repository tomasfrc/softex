# ATIVIDADE APROVAÇÃO DO ALUNO
# ATIVIDADE DO MODULO 3 AULA 5


print("Olá estudante, confira aqui se você foi aprovado nesse semestre!\n")

nome = input("Digite o nome seu nome Completo: ")
nota1 = float(input("Quanto você tirou na PRIMEIRA prova ?: "))
nota2 = float(input("Quanto você tirou na SEGUNDA prova ?: "))
faltas = int(input("Quantas vezes você faltou nesse periodo?: "))

media = (nota1 + nota2) / 2

print("Você ficou com a média de", media)
print("Faltas: ", faltas)

if media < 7:
    print("Infelizmente você (",nome,")foi Reprovado(a) por média")
if faltas > 3 :
    print("Infelizmente você (",nome,")foi Reprovado(a) por falta")
if media >= 7 and faltas <= 3:
    print("Parabéns!! você (",nome,")foi APROVADO(a) por média")