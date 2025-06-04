import React, { useState } from "react";

function SubirDocumento() {
  const [file, setFile] = useState(null);
  const [classId, setClassId] = useState("");
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file || !classId) {
      setMessage("Por favor selecciona un archivo y una clase.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("class_id", classId); // Asegúrate de que esto coincida con tu backend

    try {
      const res = await fetch("https://aulagpt.onrender.com/api/documents/upload/", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: formData,
      });

      if (res.ok) {
        setMessage("Documento subido correctamente.");
        setFile(null);
        setClassId("");
      } else {
        const data = await res.json();
        setMessage(data.error || "Error al subir el documento.");
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("Error de conexión.");
    }
  };

  return (
    <div>
      <h2>Subir Documento</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="ID de la clase"
          value={classId}
          onChange={(e) => setClassId(e.target.value)}
          required
        />
        <input type="file" onChange={handleFileChange} required />
        <button type="submit">Subir</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default SubirDocumento;
