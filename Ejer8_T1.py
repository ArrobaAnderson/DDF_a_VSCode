#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

"""Ejercicio 8"""

class Mayor_3:
    def __init__(self):
        pass
    def NumMayor(self):
        print("")
        n1 = int(input("Ingrese primer número entero: "))
        n2 = int(input("Ingrese segudo número entero: "))
        n3 = int(input("Ingrese tercer número entero: "))
        print()
        if n1 > n2 and n1 > n3:
            nM = n1
        else:
            if n2 > n3:
                nM = n2
            else:
                nM = n3
        print("El número mayor es:", nM)
        print()
        
mayor = Mayor_3()
mayor.NumMayor()            
               