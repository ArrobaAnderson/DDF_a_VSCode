#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela

"""Ejercicio 14"""

class Bucle:
    def __init__(self):
        pass
    def cntrl_cent(self):
        suma = 0
        prod = 1
        n = int(input('Ingresar numero: '))
        while n != -1:
            suma = suma + n
            prod = prod * n
            print('CONTROLADO POR CENTINELA: Total suma: {}  -  Total producto: {}'.format(suma,prod))
            n = int(input('Ingrese numero: '))
            
bucle = Bucle()
bucle.cntrl_cent()
