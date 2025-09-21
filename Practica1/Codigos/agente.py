import mapa
import numpy as np

class agente:
    def __init__(self, tipo, mapa, pos_x=0, pos_y=0):
        self.__tipo = tipo
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__matrizVision = self.__definirPatronVision(tipo)
        self.__matrizVista = self.asignarMapa(mapa)

    def __definirPatronVision(self, tipo):
        if tipo == "Agente P":
            return np.array([[1,0,1],
                            [0,1,0],
                            [1,0,1]])
        if tipo == "SuperSayayin":
            return np.array([[1,1,1],
                            [1,1,1],
                            [1,1,1]])
        if tipo == "robotBasico":
            return np.array([[0,1,0],
                            [1,1,1],
                            [0,1,0]])
        if tipo == "robotMinimo":
            return np.array([[0,1,0],
                            [0,1,0],
                            [0,0,0]])

    def asignarMapa(self, mapa):
        matrizMapaAuxiliar = mapa
        self.__matrizVista = [[False for _ in range(matrizMapaAuxiliar.ancho)] for _ in range(matrizMapaAuxiliar.alto)]
        self.actualizarVision()

    def actualizarVision(self):
        if self.__matrizVista is None:
            return

        patron_alto = len(self.__matrizVision)
        patron_ancho = len(self.__matrizVision[0])
        centro_patron_y = patron_alto // 2
        centro_patron_x = patron_ancho // 2

if "__name__" == "__main__":
    print("Agente")