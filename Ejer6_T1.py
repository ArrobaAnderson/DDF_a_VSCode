# Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10%  si su sueldo es 
# inferior a $600, en caso contrario no tendrá aumento.

"""Ejercicio 6"""

class Sueldo_Aumento:
    def __init__(self):
        pass
    def sueldo():
        sueldo = float(input("sueldo del empleado: "))
        if sueldo <=600:
            ns=sueldo+sueldo*0.10
            print()
        else:
            ns=sueldo
            print()
        print(ns,"$")
        
    sueldo()       
    
        
