// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAuth, createUserWithEmailAndPassword } from 'firebase/auth';
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyATJSL069zmqyzeNQrhNUHa4g1MWSVNNEw",
  authDomain: "aulagpt202.firebaseapp.com",
  projectId: "aulagpt202",
  storageBucket: "aulagpt202.firebasestorage.app",
  messagingSenderId: "432687553619",
  appId: "1:432687553619:web:526dd856755edbaa047aa6",
  measurementId: "G-1E1NEQJT9C"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);

// En tu componente Register.js o similar
import React, { useState } from 'react';
import { auth, db } from './firebase';
import { createUserWithEmailAndPassword } from 'firebase/auth';
import { doc, setDoc } from 'firebase/firestore';

function Register() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      const user = userCredential.user;

      // Guardar info del usuario en Firestore en colección "users"
      await setDoc(doc(db, 'users', user.uid), {
        email: user.email,
        createdAt: new Date(),
        // otros datos que quieras guardar
      });

      alert('Usuario creado y datos guardados');
    } catch (error) {
      console.error('Error creando usuario:', error.message);
      alert(error.message);
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} required />
      <input type="password" placeholder="Contraseña" value={password} onChange={e => setPassword(e.target.value)} required />
      <button type="submit">Crear cuenta</button>
    </form>
  );
}

export default Register;