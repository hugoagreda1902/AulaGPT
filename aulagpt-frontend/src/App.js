import React, { useState } from 'react';
import { addUser } from './api/dataService';  // Importa el servicio para agregar un usuario
import './App.css';

function App() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const user = { name, email, password };
    const userId = await addUser(user);
    alert(`Usuario agregado con ID: ${userId}`);
  };

  return (
    <div className="App">
      <h1>Formulario de Usuario</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Nombre"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="email"
          placeholder="Correo"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Agregar Usuario</button>
      </form>
    </div>
  );
}

export default App;
