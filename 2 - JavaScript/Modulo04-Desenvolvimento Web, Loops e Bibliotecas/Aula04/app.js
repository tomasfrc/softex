/*ALUNO: TOMÁS DE FARIAS RIBEIRO CALDAS*/

    import  express  from "express";
    import * as bancoDeDados  from "./cadastros.js" 
    import { json } from "express";
    
    const app = express();

    app.use(express.json())
    let usuarios = []

    app.listen(3000, () =>{
        console.log("Servidor iniciado")
    });

    app.get('/users', (requisicao, resposta) =>{
        return resposta.send(bancoDeDados.usuarios)
    });

    app.post('/users', (requisicao, resposta) =>{
        const novoUsuario = requisicao.body;
        bancoDeDados.cadastraUsuario(novoUsuario)
    
        return resposta.send(`Usuario ${novoUsuario.nome} cadastrado com sucesso`)
    })
    