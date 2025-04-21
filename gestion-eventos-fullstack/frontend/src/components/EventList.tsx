import { useEffect, useState } from 'react';
import { fetchEvents } from '../services/api';

interface Evento {
  id: number;
  nombre: string;
  fecha: string;
  descripcion?: string;
}

const EventList = () => {
  const [eventos, setEventos] = useState<Evento[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const cargarEventos = async () => {
      try {
        const response = await fetchEvents();
        setEventos(response.data);
      } catch (error) {
        console.error('Error al cargar eventos:', error);
      } finally {
        setLoading(false);
      }
    };

    cargarEventos();
  }, []);

  if (loading) {
    return <div className="p-4 text-center">Cargando eventos...</div>;
  }

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Lista de Eventos</h2>
      
      {eventos.length === 0 ? (
        <p>No hay eventos disponibles</p>
      ) : (
        <ul className="space-y-3">
          {eventos.map((evento) => (
            <li 
              key={evento.id} 
              className="bg-white p-4 rounded-lg shadow hover:shadow-md transition-shadow"
            >
              <h3 className="font-semibold text-lg">{evento.nombre}</h3>
              <p className="text-gray-600">
                {new Date(evento.fecha).toLocaleDateString('es-ES', {
                  weekday: 'long',
                  year: 'numeric',
                  month: 'long',
                  day: 'numeric',
                  hour: '2-digit',
                  minute: '2-digit'
                })}
              </p>
              {evento.descripcion && (
                <p className="mt-2 text-gray-700">{evento.descripcion}</p>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default EventList;