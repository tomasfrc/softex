#Desenvolva um código que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

#Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
#E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

#Aluno: Tomás de Farias Ribeiro Caldas

print("Olá, Esse programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir de algumas condições")

quantidadeRodas = int(input("Digite a quantidade de rodas possui o veículo: "))
pesoBruto = float(input("Digite o peso bruto do veículo em kilograma: "))
quantidadePessoas = int(input("Digite a quantidade de pessoas que o veículo comporta: "))

if quantidadeRodas == 1:
    print("Olá, informo que esse veículo não necessita de habilitação. Muito Obrigado!")

elif quantidadeRodas == 2 or quantidadeRodas == 3:
    print("Olá, informo que a melhor categoria de habilitação para esse veículo é a categoria A")

elif quantidadeRodas == 4 and quantidadePessoas <= 8 and pesoBruto <= 3500:
    print("Olá, informo que a melhor categoria de habilitação para esse veículo é a categoria B")

elif quantidadeRodas >= 4 and quantidadePessoas > 8:
    print("Olá, informo que a melhor categoria de habilitação para esse veículo é a categoria D")

elif quantidadeRodas >= 4 and pesoBruto > 3500 and pesoBruto <= 6000:
    print("Olá, informo que a melhor categoria de habilitação para esse veículo é a categoria C")

elif quantidadeRodas >= 4 and pesoBruto > 6000:
    print("Olá, informo que a melhor categoria de habilitação para esse veículo é a categoria E")
else:
    print("Infelizmente não conseguimos identificar o veículo, por gentileza renicie o programa e preencha as informações novamente")