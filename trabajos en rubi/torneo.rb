def simular_partido(equipo1, equipo2)
  puts "Partido: #{equipo1} vs #{equipo2}"
  print "Ingrese el marcador de #{equipo1}: "
  goles_equipo1 = gets.chomp.to_i
  print "Ingrese el marcador de #{equipo2}: "
  goles_equipo2 = gets.chomp.to_i

  if goles_equipo1 > goles_equipo2
    return equipo1
  elsif goles_equipo2 > goles_equipo1
    return equipo2
  else
    puts "Empate. Definición por penales."
    print "Ingrese el ganador por penales (#{equipo1} o #{equipo2}): "
    return gets.chomp
  end
end

def simular_fase(equipos)
  ganadores = []
  while equipos.length > 0
    equipo1 = equipos.shift
    equipo2 = equipos.shift
    ganador = simular_partido(equipo1, equipo2)
    ganadores << ganador
  end
  return ganadores
end

# Equipos participantes
equipos = ["Colombia", "Panama", "Peru", "Ecuador", "Brasil", "Argentina", "Chile", "Uruguay", "Paraguay", "Venezuela", "Bolivia", "Mexico", "Costa Rica", "Honduras", "Estados Unidos", "Canada", "Jamaica", "Haiti", "Guatemala", "El Salvador", "Nicaragua", "Cuba", "Puerto Rico", "Republica Dominicana", "Trinidad y Tobago", "Barbados", "Granada", "San Vicente y las Granadinas", "Santa Lucia", "Antigua y Barbuda", "San Cristobal y Nieves", "Bahamas", "Belice", "Guyana", "Surinam", "Guyana Francesa", "Brasil", "Argentina", "Chile", "Uruguay", "Paraguay", "Venezuela", "Bolivia", "Mexico", "Costa Rica", "Honduras", "Estados Unidos", "Canada", "Jamaica", "Haiti", "Guatemala", "El Salvador", "Nicaragua", "Cuba", "Puerto Rico", "Republica Dominicana", "Trinidad y Tobago", "Barbados", "Granada", "San Vicente y las Granadinas", "Santa Lucia", "Antigua y Barbuda", "San Cristobal y Nieves", "Bahamas", "Belice", "Guyana", "Surinam", "Guyana Francesa", "Brasil", "Argentina", "Chile", "Uruguay", "Paraguay", "Venezuela", "Bolivia", "Mexico", "Costa Rica", "Honduras", "Estados Unidos", "Canada", "Jamaica", "Haiti", "Guatemala", "El Salvador", "Nicaragua", "Cuba", "Puerto Rico", "Republica Dominicana", "Trinidad y Tobago", "Barbados", "Granada", "San Vicente y las Granadinas", "Santa Lucia", "Antigua y Barbuda", "San Cristobal y Nieves", "Bahamas", "Belice", "Guyana", "Surinam", "Guyana Francesa"]

# Simulación del torneo
fase = 1
while equipos.length > 1
  puts "\n--- Fase #{fase} ---"
  puts "Partidos de la Fase #{fase}:"
  equipos_fase = equipos.dup # Crear una copia para mostrar los partidos
  while equipos_fase.length > 0
    puts "#{equipos_fase.shift} vs #{equipos_fase.shift}"
  end
  equipos = simular_fase(equipos)
  puts "Ganadores de la Fase #{fase}: #{equipos.join(", ")}"
  fase += 1
end

puts "\n¡El ganador del torneo es: #{equipos[0]}!"
puts
print ("fin de la ejecucion_ escriba exit para salir:")
Z = gets.chomp.to_i