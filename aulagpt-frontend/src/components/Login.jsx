// Login.jsx
import { useState } from "react";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMsg("");

    try {
      const response = await fetch("https://aulagpt.onrender.com/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        alert("Login correcto");
        console.log("Datos usuario:", data);
        // Aquí puedes guardar datos en localStorage o redirigir al dashboard
      } else {
        setErrorMsg(data.error || "Error al iniciar sesión");
      }
    } catch (err) {
      console.error("Error en login:", err);
      setErrorMsg("Error de conexión con el servidor");
    }
  };

  return (
    <div>
      <h2>Iniciar sesión</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Correo electrónico"
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
        <button type="submit">Entrar</button>
      </form>
      {errorMsg && <p style={{ color: "red" }}>{errorMsg}</p>}
    </div>
  );
}

export default Login;
