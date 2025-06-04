import React, { useState } from 'react';
import axios from 'axios';

function SubirDocumento() {
  const [file, setFile] = useState(null);
  const [classId, setClassId] = useState(''); // Añadido
  const [subject, setSubject] = useState(''); // Opcional
  const [mensaje, setMensaje] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file || !classId) {
      setMensaje('Selecciona un archivo y una clase');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('class_id', classId);
    if (subject) formData.append('subject', subject); // Opcional

    try {
      const token = localStorage.getItem('token');
      const response = await axios.post(
        'https://aulagpt.onrender.com/api/documents/upload/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setMensaje('Documento subido correctamente');
      console.log(response.data);
    } catch (error) {
      console.error('Error al subir el documento:', error);
      setMensaje('Error al subir el documento');
    }
  };

  return (
    <div>
      <h2>Subir Documento</h2>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={handleFileChange} />
        <br />
        <input
          type="text"
          placeholder="ID de la clase"
          value={classId}
          onChange={(e) => setClassId(e.target.value)}
        />
        <br />
        <input
          type="text"
          placeholder="Materia (opcional)"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
        />
        <br />
        <button type="submit">Subir</button>
      </form>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
}

export default SubirDocumento;
