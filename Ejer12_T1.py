#Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100.

"""Ejercicio 12"""

class num_1a100:
    def __init__(self):
        pass
    def variables(self):
        print("Números hasta el 100 con While")
        i=1
        while i <=100:
            print(i)
            i=i+1
        print()
        
resultado=num_1a100()
resultado.variables()
