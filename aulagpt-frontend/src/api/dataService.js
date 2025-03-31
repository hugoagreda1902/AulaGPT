import axios from "axios";

export const fetchData = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/endpoint/");
    return response.data;
  } catch (error) {
    console.error("Error al obtener los datos:", error);
    throw error;
  }
};
