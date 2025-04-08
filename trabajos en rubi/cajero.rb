# Base de datos de usuarios y claves (simulada)
usuarios = {
  "sebastian" => "1234",
  "reyes" => "5678",
  "andres" => "0000"
}

# Saldo inicial de cada usuario (simulado)
saldos = {
  "sebastian" => 1000,
  "reyes" => 500,
  "andres" => 2000
}

# Función para verificar el acceso del usuario
def verificar_acceso(usuario, clave, usuarios)
  if usuarios.key?(usuario) && usuarios[usuario] == clave
    return true
  else
    return false
  end
end

# Función para mostrar el menú del cajero
def mostrar_menu
  puts "\n--- Menú del Cajero ---"
  puts "1. Consultar saldo"
  puts "2. Retirar dinero"
  puts "3. Depositar dinero"
  puts "4. Salir"
  print "Seleccione una opción: "
end

# Función para consultar el saldo
def consultar_saldo(usuario, saldos)
  puts "Su saldo actual es: $#{saldos[usuario]}"
end

# Función para retirar dinero
def retirar_dinero(usuario, saldos)
  print "Ingrese la cantidad a retirar: $"
  cantidad = gets.chomp.to_i
  if cantidad > 0 && cantidad <= saldos[usuario]
    saldos[usuario] -= cantidad
    puts "Retiro exitoso. Su nuevo saldo es: $#{saldos[usuario]}"
  else
    puts "Cantidad inválida o saldo insuficiente."
  end
end

# Función para depositar dinero
def depositar_dinero(usuario, saldos)
  print "Ingrese la cantidad a depositar: $"
  cantidad = gets.chomp.to_i
  if cantidad > 0
    saldos[usuario] += cantidad
    puts "Depósito exitoso. Su nuevo saldo es: $#{saldos[usuario]}"
  else
    puts "Cantidad inválida."
  end
end

# Inicio del programa
print "Ingrese su usuario: "
usuario_ingresado = gets.chomp

print "Ingrese su clave: "
clave_ingresada = gets.chomp

if verificar_acceso(usuario_ingresado, clave_ingresada, usuarios)
  puts "Acceso concedido."
  loop do
    mostrar_menu
    opcion = gets.chomp.to_i
    case opcion
    when 1
      consultar_saldo(usuario_ingresado, saldos)
    when 2
      retirar_dinero(usuario_ingresado, saldos)
    when 3
      depositar_dinero(usuario_ingresado, saldos)
    when 4
      puts "Gracias por usar el cajero automático."
      break
    else
      puts "Opción inválida."
    end
  end
else
  puts "Acceso denegado. Usuario o clave incorrectos."
end