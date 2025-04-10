// src/App.js
import React from 'react';
import Usuarios from './components/Usuarios';  // Importa el componente Usuarios

const App = () => {
  return (
    <div>
      <h1>Bienvenido a AulaGPT</h1>
      <Usuarios />  {/* Aquí se renderiza el componente Usuarios */}
    </div>
  );
};

export default App;
