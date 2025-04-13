require 'mongo'

client = Mongo::Client.new(['127.0.0.1:27017'], database: 'mi_base')
collection = client[:mi_coleccion]

puts 'Conectado a MongoDB'
