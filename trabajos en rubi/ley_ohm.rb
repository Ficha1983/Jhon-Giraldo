print "Ingrese el valor del voltaje del circuito: "
V = gets.chomp.to_i
puts
print "Ingrese el valor de la resistencia del circuito: "
R = gets.chomp.to_i
puts
I = V/R
puts "al conectar un voltaje de #{V} volts y una resistencia de #{R} ohms, la intensidad del circuito es de #{I} amperios"

print ("fin de la ejecucion_ escriba exit para salir:")
Z = gets.chomp.to_i
