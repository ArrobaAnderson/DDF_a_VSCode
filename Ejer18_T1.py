#Sea un vector “Calificaciones” de 100 componentes: En forma de columna se representaría así.

"""Ejercicio 18"""

class Calf_100:
    def __init__(self):
        pass

    def arrg1(self):
        calificaciones = []
        for i in range(10):
            nuevoDato = int(input("diga el dato numero {}: ".format(i)))
            calificaciones.append(nuevoDato)
        print("Las calificaciones son: {}".format(calificaciones))   

resultado=Calf_100()
resultado.arrg1()
