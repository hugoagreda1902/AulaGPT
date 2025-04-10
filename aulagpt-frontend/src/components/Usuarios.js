// src/components/Usuarios.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Usuarios = () => {
  // Estado para guardar los datos obtenidos
  const [usuarios, setUsuarios] = useState([]);
  const [error, setError] = useState(null);

  // useEffect se ejecuta al cargar el componente
  useEffect(() => {
    // Hacemos la solicitud GET a la API de Django
    axios
      .get('http://localhost:8000/api/usuarios/') // Asegúrate de que esta URL sea correcta
      .then((response) => {
        setUsuarios(response.data); // Guardamos los datos en el estado
      })
      .catch((error) => {
        setError(error); // Si hay error, lo guardamos en el estado
        console.error('Hubo un error al obtener los datos:', error);
      });
  }, []); // El array vacío significa que solo se ejecuta una vez, cuando se monta el componente

  return (
    <div>
      <h1>Lista de Usuarios</h1>
      {error && <p>Hubo un error al cargar los datos.</p>}
      <ul>
        {usuarios.length > 0 ? (
          usuarios.map((usuario) => (
            <li key={usuario.id}>
              {usuario.nombre} {usuario.apellido}
            </li>
          ))
        ) : (
          <p>No se encontraron usuarios.</p>
        )}
      </ul>
    </div>
  );
};

export default Usuarios;
