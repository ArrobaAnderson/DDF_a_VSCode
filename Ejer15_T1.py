# Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero 
# que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódigo.

"""Ejercicio 15"""

class Num_Prim:
    def __init__(self):
        pass
    def cntrl_band(self):
        primo = True
        divisor = 2
        numero = int(input('Ingresar número: '))
        while (divisor < numero) and (primo == True):
            res = numero % divisor
            if res == 0:
                primo = False
            else:
                divisor += 1
        if primo == True:
            print('Numero {} es primo'.format(numero))
        else:
            print('Numero {} no es primo'.format(numero))
bucles = Num_Prim()
bucles.cntrl_band()    
       