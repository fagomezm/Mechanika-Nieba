# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
#Definicion de Variables
a=26
b=11.3
c=5
d=3.5

#Operaciones Matematicas Basicas
print(a+b) 
print(c-a)
print(d*c)
print(c**2) #Exponente
print(c/a)
print(int(c/a)) #Division Entera
print(7%3) #Modulo

#Textos
cads="Texto entre comillas simples"
cadd="""

    Texto entre
    comillas dobles

linea 1
linea 2
linea 3
.
.
.
linea N 
"""
print(type(cads))
print (cads)
print (cadd)

cad="Cadena "*3
print(cad)

cad1="Cadena 1"
cad2="Cadena 2"
print(cad1+", "+cad2)

#Booleanos

bTrue=True
bFalse=False

bAnd=True and False
bOr=True or False
bNot=not True
print(bAnd)
print(bOr)
print(bNot)

#Cadenas
cadena=[2,"tres",True,["uno", 10]]
print(cadena)

index=cadena[1] #Adquisicion de datos desde la cadena. Index [0,1,2,3]
print(index)
index2=cadena[3][0] #Extraer item dentreo de subcadena
print(index2)

cadena[1]="cuatro" #Reemplazo de contenido en Array
print(cadena)

index2=cadena[0:3]#Copiar contenido de Index 0 a Index 3
print(index2)

index2=cadena[0:3:2] #Copiar de Index 0 a Index 3, Saltando de 0,2,4,6,...
print(index2)

index2=cadena[1::2]#Copiar de 1 a n, saltos de a dos
print(index2)

cadena[0:2]=[4,3]#Reemplazo de elementos en Array
print(cadena)

cadena[0:2]=[4]#Reemplazo total de los dos primeros elementos por el valor "4"
print(cadena)

index2=cadena[-1] #Extraer el último elemento del Array
print(index2)

#Tuplas
#La diferencia entre tuplas y Arrays son que la tupla no es modificable (No es
#posible añadir valores nuevos ni editar los presentes)
t=(3,"Hola",False)
print(t)
print(type(t))
print (t[1])

#Diccionarios, En los diccionarios se pueden agregar Tuplas y Otras Variables,
#Pero no se puede listas ni otros diccionarios
#Se pueden modificar los valores del diccionario, pero no la clave
dict={'Clave1':[1,2,3],
      'Clave2':True}
print (dict["Clave2"])

dict["Clave2"]=False
print(dict)

#Operadores Relacionales - No recomendado para cadenas
v=4
c=5
r=c==v #Comparador de Igualdad (True or False)
print(r)
r=c!=v #Comparador de Diferencia (True or False)
print(r)
r=c<v
print(r)
r=c>=v
print(r)

#Graficas 2D
"""from pylab import *
x = linspace(0, 1)
figure()
plot(x, x**2)
show()
"""

#Sentencias Condicionales
#encoding: utf-8
edad=18
m_edad=18

if edad>=0 and edad<18:
    print("Eres un niño")
elif edad>=18 and edad<27:
    print("Eres un Joven")
elif edad>=27 and edad<60:
    print("Eres un Adulto")
else:
    print("Eres de la tercera edad")
    
#While
edad=0
while edad<=20:
    if edad==15:
        edad=edad+1
        continue#Salta el siguiente ciclo
    print("Tienes "+str(edad)+" Años")
    edad=edad+1

edad=0    
while edad<=20:
    if edad==15:
        break #Salta todos los ciclos
    print("Tienes "+str(edad)+" Años")
    edad=edad+1
    
lista=["Elem1","Elem2","Elem3"]

for cosa in lista:
    print(cosa)
for cosa in "Cadena": #reemplazo de variable "Cosa" con los valores de la lista
                        #En caso de que sea un String, cada letra del string
                        #será el valor que asuma la variable "Cosa"
    print(cosa)