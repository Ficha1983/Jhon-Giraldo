a=(1,2,3,4,5,)
b=(6,7,8,9,10)
c=[]

for contador in range(len(a)):
    c.append(a[contador]*b[contador])
print(c)    

#Funciones

#Definicion y llamada

def mostrar_texto():
    print('hola')

mostrar_texto()

def multiplicar():
    a = 5
    b = 8
    print(a*b)
multiplicar()

#Ambito de las variables, las variables declaradas dentro de la funcion no son accesibles desde afuera,
#solo desde la propia funcion
#Las de afuera sin embargo, si son accesibles desde dentro de la funcion.

def multiplicar():
    print(a*b)
a = 5
b = 8
multiplicar()

#Las funciones pueden devolver los valores con la instruccion return
#En el siguiente caso devolveremos la multiplicacion, y el resultado lo guardamos en una variable,
#que luego imprimimos sumandole un valor

def multiplicar():
    a = 5
    b = 8
    return a * b
Resultado=multiplicar()
print(Resultado+5)

#Podemos devolver cualquier tipo de dato, y tratarlo como tal fuera de la funcion

def validar_dato():
    if a==5:
        return True
    else:
        return False

a = 5
dato=validar_dato()
print(dato)