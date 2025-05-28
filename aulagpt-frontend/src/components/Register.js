// src/components/Register.js
import React, { useState } from "react";
import { auth, db } from "../firebase";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { doc, setDoc } from "firebase/firestore";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const handleRegister = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      // Guardar usuario en Firestore
      await setDoc(doc(db, "users", userCredential.user.uid), {
        email: userCredential.user.email,
        createdAt: new Date()
      });
      alert("Usuario registrado correctamente");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <h2>Registro</h2>
      <input
        type="email"
        placeholder="Correo electrónico"
        value={email}
        onChange={e => setEmail(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={e => setPassword(e.target.value)}
        required
      />
      <button type="submit">Crear cuenta</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  );
}
