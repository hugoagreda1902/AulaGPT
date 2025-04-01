// database.js
import { getFirestore } from "firebase/firestore";  // Importa Firestore desde Firebase

const db = getFirestore();  // Inicializa Firestore

export { db };  // Exporta la instancia para usarla en otros archivos
