import React, { useState } from "react";
import { signInWithEmailAndPassword, createUserWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase";

function Login({ onLogin }) {
  const [isRegister, setIsRegister] = useState(false); // toggle login/registro
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (isRegister) {
      // Registrar nuevo usuario
      try {
        await createUserWithEmailAndPassword(auth, email, password);
        onLogin(); // cambiar a Home tras registro
      } catch (err) {
        setError(err.message);
      }
    } else {
      // Login usuario existente
      try {
        await signInWithEmailAndPassword(auth, email, password);
        onLogin(); // cambiar a Home tras login
      } catch (err) {
        setError("Correo o contraseña incorrectos.");
      }
    }
  };

  return (
    <div>
      <h2>{isRegister ? "Crear Cuenta" : "Iniciar Sesión"}</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Correo"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        /><br />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        /><br />
        <button type="submit">{isRegister ? "Registrarse" : "Entrar"}</button>
      </form>
      <hr />
      <p>
        {isRegister ? "¿Ya tienes cuenta?" : "¿No tienes cuenta?"}{" "}
        <button onClick={() => setIsRegister(!isRegister)} style={{ cursor: "pointer", color: "blue", background: "none", border: "none", padding: 0 }}>
          {isRegister ? "Iniciar Sesión" : "Crear Cuenta"}
        </button>
      </p>
    </div>
  );
}

export default Login;
