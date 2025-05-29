import axios from 'axios';

const API = axios.create({
  baseURL: 'https://TU_BACKEND_URL/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para incluir el token JWT si existe
API.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default API;
