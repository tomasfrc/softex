var readline = require('readline-sync')
var nome = ""
var n1 = 0
var n2 = 0
var n3 = 0
var media = 0

console.log("Programa que calcula a média do aluno")
nome = readline.question("Qual o seu nome ?: ")
n1 = parseFloat(readline.question("Informe a primeira nota: "))
n2 = parseFloat(readline.question("Informe a segunda nota: "))
n3 = parseFloat(readline.question("Informe a terceira nota: "))

media = (n1 + n2 + n3)/3

console.log("Media: "+media)

if(media < 5){
    console.log(nome + "Você foi reprovado!! \nTente novamente.")
}

else{
    console.log(nome + "Você foi aprovado! \nparabéns !!")
}
