import React, { useState } from 'react';


function Register() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      const user = userCredential.user;

      // Guardar en backend
      await fetch('https://tu-backend-api.com/api/users/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ uid: user.uid, email: user.email }),
      });

      alert('Usuario registrado correctamente');
    } catch (error) {
      console.error(error);
      alert('Error en el registro');
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Contraseña" required />
      <button type="submit">Registrarse</button>
    </form>
  );
}

export default Register;
