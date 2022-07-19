# Aluno: Tomás de Farias Ribeiro Caldas
# Aula 11 do Módulo 3
# Desenvolva um código que simule uma eleição com três candidatos.
# - candidato_X => 889
# - candidato_Y => 847
# - candidato_Z => 515
# - branco => 0

# O código deve perguntar se deseja finalizar a votação depois do voto. 
# Caso o número do voto não corresponda a nenhum candidato ou seja branco, 
# ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, 
# o código deve retornar uma mensagem para votar novamente.

# Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele 
# com o maior número de votos e, também, a quantidade de votos de cada 
# candidato, os brancos e nulos 

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e 
# compartilhe o link desse projeto no campo ao lado para que outros 
# desenvolvedores possam analisá-lo. 

import time

print('Bem Vindo as Eleições 2022')
time.sleep(2)
print('Iniciando a processo de votação')
time.sleep(2)

leonardo = 0
raphael = 0
michelangelo = 0
branco = 0

while True:
    print('Escolha sua opção de voto:')
    print('Leonardo Número: 889.')
    print('Raphael Número: 847.')
    print('Michelangelo Número: 515.')
    print('Branco Número: 0.')
    try:
        voto = int(input('Digite seu voto (Número do seu candidato):\n'))
        time.sleep(1)
        if voto == 889:
            leonardo += 1
            print('Você votou no Leonardo!')
        elif voto == 847:
            raphael += 1
            print('Você votou no Raphael!')
        elif voto == 515:
            michelangelo += 1
            print('Você votou no Michelangelo!')
        elif voto == 0:
            branco += 1 
            print('Você votou em branco!')
        else:
            print('Digite uma opção válida!')
            continue
        time.sleep(1)
        sair = str(input('Deseja finalizar a votação? [sim] para finalizar [nao] para continuar votando:'))
        if sair == 'sim':
            time.sleep(1)
            print('O Total de votos para o Leonardo foi de:',leonardo)
            time.sleep(1)
            print('O Total de votos para o Raphael foi de:',raphael)
            time.sleep(1)
            print('O Total de votos para o Michelangelo foi de:', michelangelo)
            time.sleep(1)
            print('O Total de votos em branco foi de:',branco)
            time.sleep(1)
            
            if leonardo > raphael and leonardo > michelangelo:
                print('Leonardo foi o vencedor das eleições!')
                time.sleep(1)
            
            elif raphael > leonardo and raphael > michelangelo:
                print('Raphael foi o vencedor das eleições!')
                time.sleep(1)
            
            elif michelangelo > leonardo and michelangelo > raphael:
                print('Michelangelo foi o vencendor das eleições!')
                time.sleep(1)
           
            elif branco > leonardo and branco > raphael and branco > michelangelo:
                print('O voto em branco foi a opção mais votada')
                time.sleep(1)
            print('Saindo do sistema..')
            time.sleep(1)
            break
        
        elif sair == 'nao':
            continue
        else:
            print('Digite S ou N ')
            continue
        
    except(ValueError):
        print('Vote novamente digitando uma opção válida!') 