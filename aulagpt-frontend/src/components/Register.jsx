import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';  // Para redirigir después
import { addUser } from '../api/dataService';    // Ajusta la ruta si hace falta

const Register = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await addUser({ name, email, password });  // Guardamos en la base de datos
      navigate('/thank-you');  // Redirigimos a la página de agradecimiento
    } catch (error) {
      console.error('Error al registrar usuario:', error);
      alert('Error al registrar usuario. Intenta de nuevo.');
    }
  };

  return (
    <div>
      <h2>Registro de Usuario</h2>
      <form onSubmit={handleSubmit}>
        <label>Nombre:</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />

        <label>Email:</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />

        <label>Contraseña:</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />

        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
};

export default Register;
