> Atividade 7: 

**Pesquise por aplicações grátis na internet e utilize-as na ferramenta Insomnia para realizar requisições HTTP. Dessa forma, faça três requisições utilizando o método GET**

##

Foi utilizado uma API grátis da franquia de filmes "Star Wars", disponível através da URL:
**https://swapi.dev/api**

Utilizei o fetch do node para fazer as requisições dos personagens por páginas, e cada pagina retorna 10
personagens.  
O arquivo para tratar esta chamada é o **"StarWarsService"**.
> Exemplo: **https://swapi.dev/api/people?=page1**
- Seu resultado é um JSON com informações de 10 personagens, que corresponde a primeira página.

##

Com o arquivo **"Index.js"** tratei os dados que serão apresentados, de modo a retornar apenas as informações de nome e peso. 
A atividade pede para fazer "3 requisições GET", para isso, basta alterar a const "pagina" com o número da pagina que se deseja. Tendo o seguinte retorno:

![preview](./assets/Get1.png)

![preview](./assets/Get2.png)

![preview](./assets/Get3.png)