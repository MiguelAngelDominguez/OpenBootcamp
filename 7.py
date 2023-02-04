# Primera parte:
# Crear una función con tres parámetros que sean números que se suman entre sí.
# Llamar a la función en el main y darle valores.

# Segunda parte:
# Crear una clase coche.
# Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
# Una función que incremente el número de puertas que tiene el coche.
# Crear un objeto miCoche en el main y añadirle una puerta.
# Mostrar el número de puertas que tiene el objeto.

def SumarTresNumeros(numero_1 : int, numero_2 : int, numero_3 : int):
    return numero_1 + numero_2 + numero_3

class Coche:
    def __init__(self,numeroDePuertas):
        self.numeroDePuertas = numeroDePuertas
    
    def GetNumeroDePuertas(self):
        return self.numeroDePuertas
    
    def MasPuertas(self,masPuertas : int):
        self.numeroDePuertas = self.numeroDePuertas +masPuertas

if __name__ == '__main__':
    print(f"La suma de los numeros 1+2+3 es -> {SumarTresNumeros(1,2,3)}")
    miCoche = Coche(3)
    print(f"Las Puertas del coche son {miCoche.GetNumeroDePuertas()}")
    miCoche.MasPuertas(1)
    print(f"Las Puertas del coche son {miCoche.GetNumeroDePuertas()}")
    


