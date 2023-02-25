#Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
#Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
numeroif = int(input('please enter a number to check '))
if numeroif < 0:
    print("es negativo")
if numeroif > 0:
    print("es positivo")
if numeroif == 0:
    print("es cero")


#Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
#Incrementar el valor de la variable en uno cada vez que se ejecute.
#Mostrarlo por pantalla cada vez que se ejecute.
#Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.
numeroWhile = int(input('please enter a number to check '))
while numeroWhile < 3:
   numeroWhile +1
   print(numeroWhile)
   break 


while numeroWhile < 3:
   numeroWhile += 1 
   print(numeroWhile)
   break 

numeroFor = 0
numeroFor =int(input('please enter a number to check '))
for i in range (4):
    if numeroFor == 0 or numeroFor > 3:
        numeroFor = numeroFor+1
        print (numeroFor)