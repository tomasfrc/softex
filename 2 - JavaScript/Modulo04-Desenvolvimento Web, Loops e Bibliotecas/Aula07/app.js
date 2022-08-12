/**
 * Aluno: Tomás de Farias Ribeiro Caldas
 * Implemente e trate uma conexão com o seu banco de dados, 
 * usando JavaScript. Caso a conexão com o banco tenha sucesso, ele deve 
 * retornar uma frase positiva. Se isso não ocorrer, retorne uma frase informando o erro.
 */

const express = require('express');
const app = express();
const User = require('./models/User');

app.use(express.json());

app.get("/", async (req, res) => {
    res.send("Página inicial - Celke");
});

app.post("/cadastrar", async (req, res) => {
    //console.log(req.body);

    await User.create(req.body)
    .then(() => {
        return res.json({
            erro: false,
            mensagem: "Usuário cadastrado com sucesso!"
        });
    }).catch(() => {
        return res.status(400).json({
            erro: true,
            mensagem: "Erro: Usuário não cadastrado com sucesso!"
        });
    });

    //res.send("Página cadastrar");
});

app.listen(8080, () => {
    console.log("Servidor iniciado na porta 8080: http://localhost:8080");
});