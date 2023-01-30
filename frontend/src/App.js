import axios from "axios";
import { useState, useEffect } from "react";
import './App.css';

function App() {
  const baseURL = "https://localhost:8000/productos";
  const [productos, setProductos] = useState(null);

  useEffect(() => {
    fetch(baseURL)
    .then((response) => {
      console.log(response)
    });
  }, []);

  const verProductos = () => {
    axios 
      .get(baseURL)
      .then((res) => {
          console.log(res)
      });
  };

  
  return (
    <div className="App">
      <h1>Bienvenido!</h1>
      <button onClick={verProductos}>ver productos</button>
    </div>
  );
}

export default App;
