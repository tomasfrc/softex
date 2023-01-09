const { consultarCep } = require('correios-brasil');

const cep = '50030210'; 

consultarCep(cep).then(response => {
  console.log(response.data);
});