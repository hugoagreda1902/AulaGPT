// Importa las funciones necesarias de la SDK de Firebase
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";  // Para manejar la autenticación de usuarios

// Tu configuración de Firebase
const firebaseConfig = {
  apiKey: "AIzaSyCrhqwU4xusOJ99RxxdgOXnYveU7X3iWRE",
  authDomain: "aulagpt-f0619.firebaseapp.com",
  projectId: "aulagpt-f0619",
  storageBucket: "aulagpt-f0619.firebasestorage.app",
  messagingSenderId: "1013167061923",
  appId: "1:1013167061923:web:84a6c758150b91405db816",
  measurementId: "G-FLGMYYYENW"
};

// Inicializa Firebase
const app = initializeApp(firebaseConfig);

// Inicializa Firebase Auth
const auth = getAuth(app);

// Exporta la autenticación de Firebase
export { auth };
