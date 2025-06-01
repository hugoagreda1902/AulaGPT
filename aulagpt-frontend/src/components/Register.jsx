import React, { useState } from "react";
import axios from "axios";

function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "", role: "student" });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
    setError(""); // Borra errores al escribir
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("https://tu-backend.com/api/register", form);
      // Redirigir a página de gracias si se registra bien
      window.location.href = "/thank-you";
    } catch (err) {
      if (err.response && err.response.status === 409) {
        // 409 Conflict: email ya usado
        setError("Este email ya está registrado.");
      } else {
        setError("Hubo un error al registrar.");
      }
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-6">
      <form onSubmit={handleSubmit} className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h2 className="text-2xl mb-6 font-bold">Registrarse en AulaGPT</h2>

        {error && <p className="text-red-600 mb-4">{error}</p>}

        <input
          type="text"
          name="username"
          placeholder="Nombre de usuario"
          value={form.username}
          onChange={handleChange}
          className="w-full mb-4 p-2 border rounded"
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Correo electrónico"
          value={form.email}
          onChange={handleChange}
          className="w-full mb-4 p-2 border rounded"
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={form.password}
          onChange={handleChange}
          className="w-full mb-4 p-2 border rounded"
          required
        />

        <select
          name="role"
          value={form.role}
          onChange={handleChange}
          className="w-full mb-6 p-2 border rounded"
        >
          <option value="student">Alumno</option>
          <option value="teacher">Profesor</option>
        </select>

        <button
          type="submit"
          className="w-full bg-blue-600 hover:bg-blue-700 text-white p-2 rounded"
        >
          Registrarse
        </button>
      </form>
    </div>
  );
}

export default Register;
