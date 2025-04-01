// src/App.js
import React, { useState, useEffect } from 'react';
import { getUsuarios } from './api/dataService'; // Importa la función para obtener usuarios

function App() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    getUsuarios().then(data => {
      setUsuarios(data);  // Guarda los usuarios obtenidos en el estado
    });
  }, []);

  return (
    <div>
      <h1>Lista de Usuarios</h1>
      <ul>
        {usuarios.map(usuario => (
          <li key={usuario.id}>
            {usuario.nombre} - {usuario.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
