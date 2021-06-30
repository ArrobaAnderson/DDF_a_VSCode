# En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
# cuánto deberá pagar finalmente por su compra.

'''Ejercicio 2'''

class Compra:
    def __init__(self):
        pass
def Pag_Fnl():
    TC = float(input("Digite el total de la compra: "))
    D = TC*0.15
    CP = TC - D
    print("Su cantidad a pagar es: ")
    print (CP,"$")

Pag_Fnl()
     
    