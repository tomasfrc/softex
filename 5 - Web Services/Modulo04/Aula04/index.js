import { getPeople } from "./StarWarsService.js";

async function main(){
    const pagina = 3;
    const starWarsPeoples = await getPeople(pagina);

    let starPeopleNames =  starWarsPeoples.map((p) => {
        const name = p.name
        const height = p.height
       return {name, height};
    })
   console.log(`Nomes referentes a pagina ${pagina}`)
   console.log(starPeopleNames)
   
}


main();