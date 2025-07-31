import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_API,
  timeout: 0,
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
