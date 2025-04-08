resultados = [
  5 > 3,      # true
  10 % 2 != 0, # false
  7 * 2 == 15, # false
  4 <= 4      # true
]

resultados.each do |resultado|
  puts resultado
end