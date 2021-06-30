#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por el usuario.

"""Ejercicio 13"""

class Sum_Prod:
    def __init__(self):
        pass
    def control_condicion(self):
        suma=0
        produc=1
        resp=input("Desea ingresar (S/N)?: ")
        while(resp != 'N') and (resp != 'n'):
            num = int(input('Ingrese número: '))
            suma = suma + num
            produc = produc * num
            print('Desea continuar (S/N)?: ')
            resp = input("Ingrese: ")
        print('CONTROLADO POR CONDICION: Total suma: {} - Total producto: {}'.format(suma,produc))

bucles = Sum_Prod()
bucles.control_condicion()

