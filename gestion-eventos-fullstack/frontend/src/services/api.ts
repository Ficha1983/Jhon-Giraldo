import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000/api', // Asegúrate que coincida con tu backend
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchEvents = () => API.get('/eventos/');