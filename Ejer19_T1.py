# Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y 
# a continuación escribir en un vector A todos los números negativos y en un vector B todos los positivos 
# o iguales a cero. Imprimir dichos vectores.

"""Ejercicio 19"""

class Vec_Arreglos:
    def __init__(self):
        pass

    def arreglo1(self):            
        nuevo_vector = []
        A = []
        B = []
        for j in range(0,20):
            numero = int(input('Ingrese numero: '))
            nuevo_vector.append(numero)
        for j in nuevo_vector:
            if j >= 0:
                B.append(j)
            else:
                A.append(j)
        print('Vector A con números negativos: {}'.format(A))
        print('Vector B con números positivos: {}'.format(B))

vector = Vec_Arreglos()
vector.arreglo1()        
