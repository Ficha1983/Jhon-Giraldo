Voltaje = int(input('Ingrese el valor del voltaje del circuito: '))
Resistencia = int(input('Ingrese el valor de la resistencia del circuito: '))
Intensidad = Voltaje/Resistencia #Intesidad entiendase por amperaje
print('Al conectar un resistor de R',Resistencia,'ohm'' a una fuente de V',Voltaje,'voltage circulara una corriente de',Intensidad,'amperios')