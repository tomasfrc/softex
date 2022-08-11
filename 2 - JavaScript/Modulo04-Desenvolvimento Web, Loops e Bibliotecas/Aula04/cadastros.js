
//usuarios que irá simular um banco de dados
let usuarios = [
    {id: 1, nome: "Tomás", age: 24},
    {id: 2, nome: "Pedro", age: 22},
    {id: 3, nome: "Francisco", age: 20}
]

function cadastraUsuario(usuarioNovo){
    usuarios.push(usuarioNovo);
}
export{usuarios, cadastraUsuario};