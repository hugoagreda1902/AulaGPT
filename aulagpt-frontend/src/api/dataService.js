// src/API/dataService.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/'; // La URL de tu backend (ajusta según tu configuración)

export const getUsuarios = () => {
  return axios.get(API_URL + 'usuarios/')
    .then(response => response.data)
    .catch(error => console.error('Error al obtener usuarios:', error));
};
