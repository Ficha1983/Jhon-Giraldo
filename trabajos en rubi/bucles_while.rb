contador = 1
limite = 9
suma = 0

while contador <= limite
  suma += contador
  contador += 1
  print "contador: #{contador} suma: #{suma}\n"
end

puts "La suma de los números del 1 al #{limite} es: #{suma}"