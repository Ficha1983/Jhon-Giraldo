print "ingresa la figura que desea calcular: 0 para cuadrado, 1 para triangulo, 2 para circulo: "
figura = gets.chomp.to_i

if figura == 0
    puts "ingresa el lado del cuadrado: "
    lado = gets.chomp.to_i
    area = lado * lado
    puts "el area del cuadrado es: #{area}"
elsif figura == 1
    puts "ingresa la base del triangulo: "
    base = gets.chomp.to_i
    puts "ingresa la altura del triangulo: "
    altura = gets.chomp.to_i
    area = (base * altura) / 2
    puts "el area del triangulo es: #{area}"
elsif figura == 2

    puts "ingresa el radio del circulo: "
    radio = gets.chomp.to_i
    area = 3.1416 * radio * radio
    puts "el area del circulo es: #{area}"
else
    puts "ingresa una opcion valida"
end
print ("fin de la ejecucion_ escriba exit para salir:")
Z = gets.chomp.to_i