
#Usando sintaxis de símbolos (recomendado):
diccionario_simbolos = {
  marca: "ford",
  color: "rojo",
  modelo: "sedan",
  placa: "abc123"
}

#Usando strings:
diccionario_strings = {
  "marca" => "ford",
  "color" => "rojo",    
  "modelo" => "sedan",
  "placa" => "abc123"
}


puts diccionario_simbolos[:marca]
puts diccionario_simbolos[:color]
puts diccionario_simbolos[:modelo]
puts diccionario_simbolos[:placa]

puts diccionario_strings["marca"]
puts diccionario_strings["color"]
puts diccionario_strings["modelo"]
puts diccionario_strings["placa"]

