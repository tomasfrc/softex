import "./App.css";
import HelloWorld from "./components/HelloWorld";
import SayMyName from "./components/SayMyName";
import Pessoa from "./components/Pessoa";
import { useState } from "react";

function App() {
  const name = "Tomás";
  const newName = name.toUpperCase();
  const url = "https://via.placeholder.com/150";
  const name2 = "Maria";
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <h2>Alterando o JSX</h2>
      <p>Olá, {newName}</p>
      <img src={url} alt="minha Imagem"></img>
      <HelloWorld></HelloWorld>
      <SayMyName nome={name2}></SayMyName>
      <Pessoa nome="Paulo" idade="28" profissao="Programador" foto="https://via.placeholder.com/150"></Pessoa>
      <p>Você clicou {count} vezes</p>
      <button onClick={() => setCount(count + 1)}>Clique Aqui</button>
    </div>
  );
}

export default App;
