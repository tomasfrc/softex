import "./App.css";
import HelloWorld from "./components/HelloWorld";
import SayMyName from "./components/SayMyName";
import Pessoa from "./components/Pessoa";

function App() {
  const name = "Tomás";
  const newName = name.toUpperCase();
  const url = "https://via.placeholder.com/150";
  const name2 = "Maria";

  return (
    <div className="App">
      <h2>Alterando o JSX</h2>
      <p>Olá, {newName}</p>
      <img src={url} alt="minha Imagem"></img>
      <HelloWorld></HelloWorld>
      <SayMyName nome={name2}></SayMyName>
      <Pessoa nome="Paulo" idade="28" profissao="Programador" foto="https://via.placeholder.com/150"></Pessoa>
    </div>
  );
}

export default App;
