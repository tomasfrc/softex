#MÓDULO 04 AULA 04
#ALUNO: TOMÁS DE FARIAS RIBEIRO CALDAS

#Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. Depois, desenvolva três ou mais objetos para testar o código.

#Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo. 


class Carro: 
    incremento = 0
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano 

    def minhaf(self, incremento):
        print(f"Você tem o carro da marca {self.marca}, do ano {self.ano}. Em {incremento} anos o seu carro vai está no ano de {self.ano + incremento}.")


p1 = Carro("hyundai", 2000)
p1.minhaf(5)


p2 = Carro("Volkswagen", 2005)
p2.minhaf(3)


p3 = Carro("Fiat", 2016)
p3.minhaf(10)
