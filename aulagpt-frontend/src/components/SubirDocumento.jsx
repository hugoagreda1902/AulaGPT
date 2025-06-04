import React, { useState, useEffect } from 'react';
import axios from 'axios';

function SubirDocumento() {
  const [file, setFile] = useState(null);
  const [classes, setClasses] = useState([]);
  const [selectedClassId, setSelectedClassId] = useState('');
  const [subject, setSubject] = useState('');
  const [mensaje, setMensaje] = useState('');

  // Cargar clases desde backend cuando carga el componente
  useEffect(() => {
    const fetchClasses = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('https://aulagpt.onrender.com/api/classes/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setClasses(response.data);
        if (response.data.length > 0) {
          setSelectedClassId(response.data[0].class_id || response.data[0].id); // Ajusta según la estructura que devuelvas
        }
      } catch (error) {
        console.error('Error cargando clases:', error);
      }
    };
    fetchClasses();
  }, []);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file || !selectedClassId) {
      setMensaje('Selecciona un archivo y una clase');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('class_id', selectedClassId);
    if (subject) formData.append('subject', subject);

    try {
      const token = localStorage.getItem('token');
      const response = await axios.post(
        'https://aulagpt.onrender.com/api/uploadDocument/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setMensaje('Documento subido correctamente');
      setFile(null);
      setSubject('');
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
        <label>Clase:</label>
        <select
          value={selectedClassId}
          onChange={(e) => setSelectedClassId(e.target.value)}
        >
          {classes.map((cls) => (
            <option key={cls.class_id || cls.id} value={cls.class_id || cls.id}>
              {cls.name || cls.subject || `Clase ${cls.class_id || cls.id}`}
            </option>
          ))}
        </select>
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
