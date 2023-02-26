import math
import os
message = " Bienvenidos a la calculadora de IMC "
print(message)
nombre = input('Ingrese su nombre: ')
peso = float(input('Indique su peso en kg '))
estatura = float(input(' Indique su estatura en metros '))
imc = peso / (estatura**2)
print(nombre, 'Su IMC es: ', round(imc))