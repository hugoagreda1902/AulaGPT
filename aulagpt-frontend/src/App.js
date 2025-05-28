// src/App.js
import React, { useState, useEffect } from "react";
import { auth } from "./firebase";
import { onAuthStateChanged, signOut } from "firebase/auth";

import Login from "./components/Login";
import Register from "./components/Register";

function App() {
  const [user, setUser] = useState(null);
  const [showRegister, setShowRegister] = useState(false);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
    });
    return () => unsubscribe();
  }, []);

  const handleLogout = () => {
    signOut(auth);
  };

  if (user) {
    return (
      <div>
        <h1>Bienvenido, {user.email}</h1>
        <button onClick={handleLogout}>Cerrar sesión</button>
      </div>
    );
  }

  return (
    <div>
      {showRegister ? (
        <>
          <Register />
          <p>
            ¿Ya tienes cuenta?{" "}
            <button onClick={() => setShowRegister(false)}>Iniciar sesión</button>
          </p>
        </>
      ) : (
        <>
          <Login onLogin={() => {}} />
          <p>
            ¿No tienes cuenta?{" "}
            <button onClick={() => setShowRegister(true)}>Regístrate</button>
          </p>
        </>
      )}
    </div>
  );
}

export default App;
