// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

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
const auth = getAuth(app);

export { auth };