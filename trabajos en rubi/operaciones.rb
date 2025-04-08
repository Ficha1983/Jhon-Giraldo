print "Por favor, ingresa una variable: "
A = gets.chomp.to_i
puts "La primera variable es: #{A}"

print "Por favor, ingresa una variable: "
B = gets.chomp.to_i
puts "La segunda variable es: #{B}"


suma=A+B
print('la suma de los numeros es: ',suma)
puts
res=A-B
print('la resta de los numeros es: ',res)
puts
multi=A*B
print('la multiplicacion de los numeros es: ',multi)
puts
div=A/B 
print('la division de los numeros es: ',div)
puts
igual=A==B
print('el numero es igual: ',A)
puts
mayor=A>B
print('el numero menor es: ',A)
puts
print('el numero mayor es: ',B)
puts
print ("fin de la ejecucion_ escriba exit para salir:")
Z = gets.chomp.to_i
