import React, { useState } from "react";
import { Plus } from "lucide-react";

interface ProductoFormProps {
  categorias: { id: string; nombre: string }[];
  onAgregar: (producto: any) => void;
}

export const FormularioProducto: React.FC<ProductoFormProps> = ({
  categorias,
  onAgregar,
}) => {
  const [producto, setProducto] = useState({
    nombre: "",
    descripcion: "",
    precio: 0,
    stock: 0,
    categoriaId: categorias[0]?.id || "",
    tallas: [] as string[],
    colores: [] as string[],
  });
  const [nuevaTalla, setNuevaTalla] = useState("");
  const [nuevoColor, setNuevoColor] = useState("");

  const agregarTalla = () => {
    if (nuevaTalla && !producto.tallas.includes(nuevaTalla)) {
      setProducto({ ...producto, tallas: [...producto.tallas, nuevaTalla] });
      setNuevaTalla("");
    }
  };

  const agregarColor = () => {
    if (nuevoColor && !producto.colores.includes(nuevoColor)) {
      setProducto({ ...producto, colores: [...producto.colores, nuevoColor] });
      setNuevoColor("");
    }
  };

  const manejarEnvio = (e: React.FormEvent) => {
    e.preventDefault();
    onAgregar(producto);
    setProducto({
      ...producto,
      nombre: "",
      descripcion: "",
      precio: 0,
      stock: 0,
      tallas: [],
      colores: [],
    });
  };

  return (
    <form onSubmit={manejarEnvio} className="p-6 bg-white rounded shadow-md">
      <div className="flex gap-2 items-center mb-4">
        <Plus className="text-blue-600" />
        <h2 className="text-xl font-bold">Nuevo Producto</h2>
      </div>
      <input
        className="w-full mb-3 border p-2 rounded"
        type="text"
        placeholder="Nombre"
        value={producto.nombre}
        onChange={(e) => setProducto({ ...producto, nombre: e.target.value })}
        required
      />
      <textarea
        className="w-full mb-3 border p-2 rounded"
        placeholder="Descripción"
        value={producto.descripcion}
        onChange={(e) =>
          setProducto({ ...producto, descripcion: e.target.value })
        }
        required
      />
      <select
        className="w-full mb-3 border p-2 rounded"
        value={producto.categoriaId}
        onChange={(e) =>
          setProducto({ ...producto, categoriaId: e.target.value })
        }
      >
        {categorias.map((c) => (
          <option key={c.id} value={c.id}>
            {c.nombre}
          </option>
        ))}
      </select>
      <div className="grid grid-cols-2 gap-2 mb-3">
        <input
          type="number"
          className="border p-2 rounded"
          placeholder="Precio"
          value={producto.precio}
          onChange={(e) =>
            setProducto({ ...producto, precio: +e.target.value })
          }
        />
        <input
          type="number"
          className="border p-2 rounded"
          placeholder="Stock"
          value={producto.stock}
          onChange={(e) =>
            setProducto({ ...producto, stock: +e.target.value })
          }
        />
      </div>
      <div className="mb-3">
        <label className="block mb-1">Tallas:</label>
        <div className="flex gap-2">
          <input
            type="text"
            value={nuevaTalla}
            onChange={(e) => setNuevaTalla(e.target.value)}
            className="flex-1 border p-2 rounded"
          />
          <button
            type="button"
            onClick={agregarTalla}
            className="bg-blue-500 text-white px-4 rounded"
          >
            Agregar
          </button>
        </div>
        <div className="mt-2 flex gap-2">
          {producto.tallas.map((t) => (
            <span key={t} className="bg-blue-100 px-2 py-1 rounded text-sm">
              {t}
            </span>
          ))}
        </div>
      </div>
      <div className="mb-4">
        <label className="block mb-1">Colores:</label>
        <div className="flex gap-2">
          <input
            type="text"
            value={nuevoColor}
            onChange={(e) => setNuevoColor(e.target.value)}
            className="flex-1 border p-2 rounded"
          />
          <button
            type="button"
            onClick={agregarColor}
            className="bg-blue-500 text-white px-4 rounded"
          >
            Agregar
          </button>
        </div>
        <div className="mt-2 flex gap-2">
          {producto.colores.map((c) => (
            <span key={c} className="bg-gray-100 px-2 py-1 rounded text-sm">
              {c}
            </span>
          ))}
        </div>
      </div>
      <button
        type="submit"
        className="bg-green-600 text-white py-2 px-4 w-full rounded hover:bg-green-700"
      >
        Agregar Producto
      </button>
    </form>
  );
};