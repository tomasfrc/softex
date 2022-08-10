/*
ALUNO: TOMÁS DE FARIAS RIBEIRO CALDAS

Crie um programa que contenha os seguintes tipos de funções:

1. uma função tradicional com a palavra reservada “Function” e sem nenhum parâmetro;
2. uma função tradicional com parâmetros e um retorno de valor;
3. uma arrow function com parâmetros e que retorne um valor.

Crie um programa que utilize essas três funções de forma lógica, por exemplo: um programa de calculadora.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo. */


var dataAtual = new Date();
var anoAtual = dataAtual.getFullYear();

function apresentação() {
    alert(" Bom dia, Boa tarde e Boa Noite !! Irei descobrir quantos anos você vai ter ou irá completar esse ano.")
    idade(parseInt(prompt("Digite seu ano de nascimento: ")));
}

function calculo(ano) {
    return anoAtual - ano; 
}

idade = (ano) =>{
    alert(`Deixa eu ver se acertei, Você terá em ${anoAtual} ${calculo(ano)} anos`);
}


apresentação();