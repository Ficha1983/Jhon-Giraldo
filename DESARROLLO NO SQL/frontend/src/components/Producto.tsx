import React from 'react';
import { format } from 'date-fns';
import { es } from 'date-fns/locale';
import { Calendar } from 'lucide-react';

interface ProductoProps {
  producto: any;
  onEliminar: (id: string) => void;
}

export const Producto: React.FC<ProductoProps> = ({ producto, onEliminar }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      <h3 className="text-lg font-bold">{producto.nombre}</h3>
      <p className="text-gray-600">{producto.descripcion}</p>

      <div className="text-green-600 font-semibold mt-2">${producto.precio}</div>

      <div className="text-sm text-blue-800">Stock: {producto.stock}</div>
      {producto.tallas && (
        <div className="mt-2">
          <strong>Tallas:</strong> {producto.tallas.join(', ')}
        </div>
      )}
      {producto.colores && (
        <div className="mt-1">
          <strong>Colores:</strong> {producto.colores.join(', ')}
        </div>
      )}
      <div className="mt-2 flex items-center text-gray-500 text-sm">
        <Calendar className="w-4 h-4 mr-1" />
        Creado el {format(new Date(producto.fechaCreacion), "d 'de' MMMM 'de' yyyy", {
          locale: es,
        })}
      </div>
      <button
        onClick={() => onEliminar(producto._id)}
        className="mt-4 bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600 w-full"
      >
        Eliminar
      </button>
    </div>
  );
};