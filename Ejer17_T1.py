#Calcular el factorial de N números enteros leídos de teclado.
#El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.

"""Ejercicio 17"""

class Fac_Num:
    def __init__(self):
        pass
    def bucle_anidado(self):
        numero = int(input('Ingresar número: '))
        factorial = 1
        for i in range(1, numero+1):
            factorial *= i
        print('El factorial del número {} es: {} '.format(numero, factorial)) 

calculo = Fac_Num()
calculo.bucle_anidado()
