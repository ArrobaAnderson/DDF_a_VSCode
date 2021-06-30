# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber 
# cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total 
# que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.

"""Ejercicio 3"""

class Sueldo_Comisiones:
    def sueldo():
        SB=float(input("Ingrese salario base: "))
        V1=float(input("Ingrese valor venta_1: "))
        V2=float(input("Ingrese valor venta_2: "))
        V3=float(input("Ingrese valor venta_3: "))
        TV=V1+V2+V3
        C=TV*0.10
        TR=SB+C
        print()
        print("Su total de salario a percibir es: $", TR)
        
    sueldo()
        
    
            
        