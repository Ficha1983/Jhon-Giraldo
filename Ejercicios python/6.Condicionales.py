Figura= input('selecione la figura a calcular su area: \n\n 1 para rombo\n\n 2 para rectangulo \n\n 3 para cuadrado \n\n 4 para trapecio \n\n: ')
Pi=3.1416
const= int(2)
match Figura:
    case '1':
        Dmayor= int(input('ingresa el valor de la diagonal mayor: '))
        Dmenor= int(input('ingresa el valor de la diagonal menor: '))
        Area=(Dmayor+Dmenor/const)
        print('El area del rombo es: ',Area)
    case '2':
        Largo= int(input('ingresa el valor del largo del rectangulo: '))
        Ancho= int(input('ingresa el valor del ancho del rectangulo: '))
        Area=Largo*Ancho
        print('El area del rectangulo es: ',Area)
    case '3':
        Lado= int(input('ingresa el valor del lado del cuadrado: '))
        Area=Lado*Lado
        print('El area del cuadrado es: ',Area)         
    case '4':
        Bmayor= int(input('ingresa el valor de la base mayor: '))
        Bmenor= int(input('ingresa el valor de la base menor: '))
        H=int (input('ingrese la altura del trapecio: '))
        Area=(((Bmayor+Bmenor)*H)/2)
        print('El area del trapecio es: ',Area)
