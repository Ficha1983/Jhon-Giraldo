print "escriba sus nombres completos: "
a = gets.chomp

print "escribas sus Apellidos completos: "
b = gets.chomp

print "escriba su profesion: "
c = gets.chomp

print "escriba su año de nacimiento: "
d = gets.chomp.to_i

e = 2025 - d
puts "su nombre es #{a} #{b}, su profesion es #{c} y su edad es #{e}"

print ("fin de la ejecucion_ escriba exit para salir:")
Z = gets.chomp.to_i