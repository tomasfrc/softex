# Faça um código que execute uma contagem regressiva de uma bomba, informando o número
# de segundos para explodir. Ele deve mostrar uma mensagem “iniciando contagem regressiva”,
# os segundos passados ​​e, no final, a mensagem “BUM!”.

# Não é necessário, mas, caso deseje tornar o sistema mais realista para que o
# tempo realmente passa em segundos, você pode usar a função time.sleep() que existe
# na Python (acesse o link em anexo). No entanto, é preciso adicionar uma biblioteca antes de executar-la.

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o
# link desse campo ao lado para que outros projetos no podem analisar-lo.

# Aluno: Tomás de Farias Ribeiro Caldas
# Atividade Módulo 3, Aula 07

import time

print("Iniciando contagem regressiva:")

for segundos in range (10, -1, -1):
    print("Restam apenas: ", segundos, "para todos morrerem!")
    time.sleep(1)
    if (segundos == 0):
        print("BUM!")