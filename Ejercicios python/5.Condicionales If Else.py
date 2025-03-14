a=2
if a ==2:
    print('a vale 2')
else:
    print('a es diferente de 2')

#Concatenar condiciones 

Nombre = 'Esteban'
Edad = 28
Pais='Colombia'

if Nombre =='Esteban' and Edad == 28 and Pais =='Colombia':
    print('Su nombre es', Nombre,'tiene',Edad,'y es de',Pais) 
elif Nombre == 'Esteban'and not Edad==28:
    print('Su nombre es Esteban y no tiene 28 años')
elif Nombre != 'Esteban'and Edad == 28:
    print('Su nombre no es Esteban y tiene 28 años')
else:
    print('No se llama Esteban ni tiene 28 años')         