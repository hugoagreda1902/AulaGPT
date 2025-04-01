import { db } from '../firebase';  // Importa la instancia de Firebase

export const addUser = async (user) => {
  try {
    const docRef = await db.collection('users').add({
      name: user.name,
      email: user.email,
      password: user.password,  // Asegúrate de manejar contraseñas de manera segura
    });
    console.log("User added with ID: ", docRef.id);
    return docRef.id;
  } catch (error) {
    console.error("Error adding user: ", error);
  }
};

// Esta función obtiene los usuarios de la base de datos (para pruebas)
export const getUsers = async () => {
  try {
    const querySnapshot = await db.collection('users').get();
    const users = querySnapshot.docs.map(doc => doc.data());
    return users;
  } catch (error) {
    console.error("Error getting users: ", error);
  }
};
