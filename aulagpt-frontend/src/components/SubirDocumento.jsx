import React, { useState } from 'react';

export default function UploadDocument() {
  const [selectedClass, setSelectedClass] = useState('');
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(null);

    if (!selectedClass) {
      setMessage('Selecciona una clase');
      return;
    }
    if (!file) {
      setMessage('Selecciona un archivo');
      return;
    }

    const formData = new FormData();
    formData.append('class_id', selectedClass);
    formData.append('file', file);

    setLoading(true);
    try {
      const res = await fetch('/api/documents/', {
        method: 'POST',
        body: formData,
      });
      if (!res.ok) {
        const errorData = await res.json();
        setMessage('Error al subir: ' + (errorData.detail || JSON.stringify(errorData)));
      } else {
        setMessage('Documento subido con éxito');
        setFile(null);
        setSelectedClass('');
      }
    } catch (error) {
      setMessage('Error de conexión');
    }
    setLoading(false);
  };

  return (
    <div className="container mt-4" style={{ maxWidth: '500px' }}>
      <h3>Subir documento</h3>
      {message && <div className="alert alert-info">{message}</div>}
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="classSelect" className="form-label">Clase</label>
          <select
            id="classSelect"
            className="form-select"
            value={selectedClass}
            onChange={e => setSelectedClass(e.target.value)}
            disabled
          >
            <option value="">(Funcionalidad pendiente)</option>
          </select>
        </div>

        <div className="mb-3">
          <label htmlFor="fileInput" className="form-label">Archivo</label>
          <input
            type="file"
            id="fileInput"
            className="form-control"
            onChange={e => setFile(e.target.files[0])}
            required
          />
        </div>

        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? 'Subiendo...' : 'Subir'}
        </button>
      </form>
    </div>
  );
}
