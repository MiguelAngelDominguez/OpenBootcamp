## Ejercicios tema 4

# En este ejercicio practicarás las estructuras de control, para ello deberás crear:
# Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
# Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
# Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
#    - Incrementar el valor de la variable en uno cada vez que se ejecute.
#    - Mostrarlo por pantalla cada vez que se ejecute.
# Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.
# Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.
# Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.

if __name__ == '__main__':
    numeroIf = int(input(' - ingrese un numero : '))
    if numeroIf > 0 : print("numero mayor que 0 ")
    elif numeroIf < 0 : print("numoer menor que 0")
    else: print("el numeoro es 0")
    print("__________________")
    numeroWhile = -5
    while numeroWhile<= 3:
        numeroWhile +=1
        print(numeroWhile)
    print("__________________")
    condicion = True
    numeroWhile = 4   
    while(condicion):
        numeroWhile +=1
        print(numeroWhile)
        if(numeroWhile > 3):
            condicion = False
    print("__________________")
    for numeroFor in range(4):
        print(numeroFor)
    print("__________________")
    estacion = input(" ingrese la estacion de año actual : ")
    if estacion == "primavera":
        print("Estamos en primavera")
    elif estacion == "verano":
        print("Estamos en verano")
    elif estacion == "otoño":
        print("Estamos en otoño")
    elif estacion == "invierno":
        print("Estamos en Invierno")
    else:
        print("valor ingresado es desconocido ...")
