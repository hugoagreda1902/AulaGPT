import React from 'react';
import ReactDOM from 'react-dom/client'; // Asegúrate de que estás importando desde 'react-dom/client'
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Crea el root y renderiza la app
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
