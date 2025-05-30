import React, { useState } from 'react';
import { addUser } from '../api/dataService';

export default function Register() {
  const [user, setUser] = useState({
    name: '',
    surname: '',
    email: '',
    password: '',
    role: 'student' // puedes poner 'student' o 'teacher' por defecto
  });
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setUser({ ...user, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      await addUser(user);
      setSubmitted(true);
    } catch (err) {
      setError('Error al registrar usuario. Inténtalo de nuevo.');
      console.error(err);
    }
  };

  if (submitted) {
    return <h2>¡Gracias por registrarte!</h2>;
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Registro de usuario</h2>

      <label>
        Nombre:
        <input
          type="text"
          name="name"
          value={user.name}
          onChange={handleChange}
          required
        />
      </label>

      <label>
        Apellido:
        <input
          type="text"
          name="surname"
          value={user.surname}
          onChange={handleChange}
          required
        />
      </label>

      <label>
        Email:
        <input
          type="email"
          name="email"
          value={user.email}
          onChange={handleChange}
          required
        />
      </label>

      <label>
        Contraseña:
        <input
          type="password"
          name="password"
          value={user.password}
          onChange={handleChange}
          required
        />
      </label>

      <label>
        Rol:
        <select name="role" value={user.role} onChange={handleChange} required>
          <option value="student">Estudiante</option>
          <option value="teacher">Profesor</option>
        </select>
      </label>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <button type="submit">Registrar</button>
    </form>
  );
}
