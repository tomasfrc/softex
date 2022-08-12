/*
    Aluno: Tomás de Farias Ribeiro Caldas
    Aula: M4A6

    Desenvolva um código e crie nele:

- um objeto com, no mínimo, três propriedades;
- um array de tamanho três no mínimo;
- duas funções, a primeira lista as propriedades do objeto e a segunda, os elementos do array.

*/
const time = {
    nome: "Palmeiras",
    fundacao: 1914,
    estadio: "Allianz Parque"
}
const array = ["3 Libertadores", "4 Copa do Brasil", "10 Campeonato Brasileiro", "26 Campeonato Paulista"]


console.log("Melhor time do Brasil: \n")
for(const propriedade in time){
    console.log(`${propriedade}: ${time[propriedade]}`)
}


console.log("\nTítulos conquistados em sua história: \n")
for(const elemento of array){
    console.log(`${elemento}`)
}