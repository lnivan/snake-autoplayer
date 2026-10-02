#Importacion de librerias 
from tkinter import Grid
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
from PIL import ImageGrab
import random
import time

###Definicion de la clase serpiente
class Serpiente:
    ##Funcion para inicializar la serpiente
    def __init__(self, posicion):
        self.cuerpo = posicion[0 : len(posicion) - 1]
        self.cabeza = posicion[len(posicion) - 1]
        self.posicionManzana = 0
        self.manzana = True
        self.camino = []
        self.tiempoDesdeUltimoPaso = time.time()

    def encontrarManzana(self):
        amplitud = 18
        imagen = ImageGrab.grab()
        for x in range(int(1244 + 500 / 22), int(1743 - 500 / 22 + 2), int(500 / 11)):
            for y in range(int(98 + 500 / 22), int(597 - 500 / 22 + 2), int(500 / 11)):
                if (imagen.getpixel((x + amplitud, y)) == (238, 0, 0) or imagen.getpixel((x - amplitud, y)) == (238, 0, 0)  or imagen.getpixel((x, y + amplitud)) == (238, 0, 0)  or imagen.getpixel((x, y - amplitud)) == (238, 0, 0)) and [int((x - 1244) / 45), int((y - 98) / 45)] != self.posicionManzana:
                    self.manzana = True
                    return([int((x - 1244) / 45), int((y - 98) / 45)])
        grid = [[0 for i in range(11)] for i in range(11)]
        for cuerpo in self.cuerpo:
            grid[cuerpo[0]][cuerpo[1]] = 1
        grid[self.cabeza[0]][self.cabeza[1]] = 2
        candidatos = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    candidatos.append([x, y])
        self.manzana = False
        x, y = candidatos[random.randint(0, len(candidatos) - 1)][0], candidatos[random.randint(0, len(candidatos) - 1)][1]
        return([x, y])


    ##Funcion para encontrar el mejor camino a la manzana
    def encontrarCamino(self, posicionManzana):
        #Definicion de variables para usar en la busqueda
        self.posicionManzana = posicionManzana
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid = [[0 for i in range(11)] for i in range(11)]
        for cuerpo in self.cuerpo:
            grid[cuerpo[0]][cuerpo[1]] = 1
        grid[self.cabeza[0]][self.cabeza[1]] = 2
        grid[posicionManzana[0]][posicionManzana[1]] = 3
        applePosition = posicionManzana
        snakeHeadPosition = self.cabeza
        pathsChecked = [[snakeHeadPosition]]
        pathFound = False
        #Busqueda del mejor camino
        while pathFound == False:
            newPathsChecked = []
            for path in pathsChecked:
                if path[len(path) - 1] == applePosition:
                    path.pop(0)
                    print(path)
                    return(path)
                for direction in directions:
                    if path[len(path) - 1][0] + direction[0] >= 0 and path[len(path) - 1][0] + direction[0] <= len(grid) - 1 and path[len(path) - 1][1] + direction[1] >= 0 and path[len(path) - 1][1] + direction[1] <= len(grid[0]) - 1:
                        if grid[path[len(path) - 1][0] + direction[0]][path[len(path) - 1][1] + direction[1]] not in [1, 2, 4]:
                            newPathsChecked.append(path[:])
                            newPathsChecked[len(newPathsChecked) - 1].append([path[len(path) - 1][0] + direction[0], path[len(path) - 1][1] + direction[1]])
                            grid[path[len(path) - 1][0] + direction[0]][path[len(path) - 1][1] + direction[1]] = 4
            pathsChecked = newPathsChecked





    def encontrarCamino2(self, posicionManzana):
        #Definicion de variables para usar en la busqueda
        tiempo = time.time()
        self.posicionManzana = posicionManzana
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid = [[0 for i in range(11)] for i in range(11)]
        for cuerpo in self.cuerpo:
            grid[cuerpo[0]][cuerpo[1]] = 1
        grid[self.cabeza[0]][self.cabeza[1]] = 2
        grid[posicionManzana[0]][posicionManzana[1]] = 3
        applePosition = posicionManzana
        snakeHeadPosition = self.cabeza
        pathsChecked = [[snakeHeadPosition[:]]]
        pathFound = False
        #Busqueda del mejor camino
        while pathFound == False:
            newPathsChecked = []
            ultimosPasos = []
            for path in pathsChecked:
                if path[len(path) - 1] == applePosition:
                    path.pop(0)
                    print(path)
                    print(time.time() - tiempo)
                    return(path)
                for direction in directions:
                    if path[len(path) - 1][0] + direction[0] >= 0 and path[len(path) - 1][0] + direction[0] <= len(grid) - 1 and path[len(path) - 1][1] + direction[1] >= 0 and path[len(path) - 1][1] + direction[1] <= len(grid[0]) - 1:
                        posicionSerpiente = (self.cuerpo + path)[len(path) - 1:]
                        if [path[len(path) - 1][0] + direction[0], path[len(path) - 1][1] + direction[1]] not in posicionSerpiente:
                            if [path[len(path) - 1][0] + direction[0], path[len(path) - 1][1] + direction[1]] not in ultimosPasos:
                                newPathsChecked.append(path + [[path[len(path) - 1][0] + direction[0], path[len(path) - 1][1] + direction[1]]])
                                ultimosPasos.append([path[len(path) - 1][0] + direction[0], path[len(path) - 1][1] + direction[1]])
            pathsChecked = newPathsChecked



    def encontrarCamino3(self, posicionManzana):
        #Definicion de variables para usar en la busqueda
        self.posicionManzana = posicionManzana
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid = [[0 for i in range(11)] for i in range(11)]
        for cuerpo in self.cuerpo:
            grid[cuerpo[0]][cuerpo[1]] = 1
        grid[self.cabeza[0]][self.cabeza[1]] = 2
        grid[posicionManzana[0]][posicionManzana[1]] = 3
        applePosition = posicionManzana
        snakeHeadPosition = self.cabeza
        snakeBodyPosition = self.cuerpo
        securePath = [[snakeHeadPosition]]
        pathsChecked = [[snakeHeadPosition]]
        pathFound = False
        #Busqueda del mejor camino
        while pathFound == False:
            newPathsChecked = []
            for path in pathsChecked:
                if path[len(path) - 1] == applePosition:
                    path.pop(0)
                    print(path)
                    return(path)
                for direction in directions:
                    if path[len(path) - 1][0] + direction[0] >= 0 and path[len(path) - 1][0] + direction[0] <= len(grid) - 1 and path[len(path) - 1][1] + direction[1] >= 0 and path[len(path) - 1][1] + direction[1] <= len(grid[0]) - 1:
                        if grid[path[len(path) - 1][0] + direction[0]][path[len(path) - 1][1] + direction[1]] != 4:
                            if [path[len(path) - 1][0] + direction[0], path[len(path) - 1][1] + direction[1]] not in snakeBodyPosition and [path[len(path) - 1][0] + direction[0], path[len(path) - 1][1] + direction[1]] not in snakeHeadPosition:
                                newPathsChecked.append(path[:])
                                newPathsChecked[len(newPathsChecked) - 1].append([path[len(path) - 1][0] + direction[0], path[len(path) - 1][1] + direction[1]])
                                grid[path[len(path) - 1][0] + direction[0]][path[len(path) - 1][1] + direction[1]] = 4


            if newPathsChecked == []:
                direcciones = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                direccionElegida = direcciones.pop()
                while [direccionElegida[0] + snakeHeadPosition[0], direccionElegida[1] + snakeHeadPosition[1]] in snakeBodyPosition[1:len(snakeBodyPosition)] or direccionElegida[0] + snakeHeadPosition[0] > 10 or direccionElegida[0] + snakeHeadPosition[0] < 0 or direccionElegida[1] + snakeHeadPosition[1] > 10 or direccionElegida[1] + snakeHeadPosition[1] < 0:
                    direccionElegida = direcciones.pop()
                print(direccionElegida)
                securePath.append([snakeHeadPosition[0] + direccionElegida[0], snakeHeadPosition[1] + direccionElegida[1]])
                grid = [[0 for i in range(11)] for i in range(11)]
                for cuerpo in snakeBodyPosition[1:len(snakeBodyPosition)]:
                    grid[cuerpo[0]][cuerpo[1]] = 1
                grid[snakeHeadPosition[0]][snakeHeadPosition[1]] = 1
                grid[snakeHeadPosition[0] + direccionElegida[0]][snakeHeadPosition[1] + direccionElegida[1]] = 2
                grid[posicionManzana[0]][posicionManzana[1]] = 3
                snakeBodyPosition = snakeBodyPosition[1:len(snakeBodyPosition)]
                snakeBodyPosition.append([snakeHeadPosition[0], snakeHeadPosition[1]])
                snakeHeadPosition = [snakeHeadPosition[0] + direccionElegida[0], snakeHeadPosition[1] + direccionElegida[1]]
                pathsChecked = [securePath[:]] 
            else:
                pathsChecked = newPathsChecked











    def avanzar(self, coordenada):
        direccion = [coordenada[0] - self.cabeza[0], coordenada[1] - self.cabeza[1]]
        amplitud = 10
        imagen = ImageGrab.grab()
        while imagen.getpixel((int(1244 + 500 / 22 + self.cabeza[0] * 500 / 11 + amplitud), int(98 + 500 / 22 + self.cabeza[1] * 500 / 11))) != (109, 255, 24) and imagen.getpixel((int(1244 + 500 / 22 + self.cabeza[0] * 500 / 11 - amplitud), int(98 + 500 / 22 + self.cabeza[1] * 500 / 11))) != (109, 255, 24) and imagen.getpixel((int(1244 + 500 / 22 + self.cabeza[0] * 500 / 11), int(98 + 500 / 22 + self.cabeza[1] * 500 / 11 + amplitud))) != (109, 255, 24) and imagen.getpixel((int(1244 + 500 / 22 + self.cabeza[0] * 500 / 11), int(98 + 500 / 22 + self.cabeza[1] * 500 / 11 - amplitud))) != (109, 255, 24):
            imagen = ImageGrab.grab()
        if direccion == [0, 1]:
            press("s", 0.05)
        elif direccion == [0, -1]:
            press("w", 0.05)        
        elif direccion == [1, 0]:
            press("d", 0.05)        
        else:
            press("a", 0.05)
        self.cuerpo.append(self.cabeza)
        self.cabeza = [self.cabeza[0] + direccion[0], self.cabeza[1] + direccion[1]]
        amplitud = 1
        if imagen.getpixel((int(1244 + 500 / 22 + coordenada[0] * 500 / 11 + amplitud), int(98 + 500 / 22 + coordenada[1] * 500 / 11))) == (238, 0, 0) or imagen.getpixel((int(1244 + 500 / 22 + coordenada[0] * 500 / 11 - amplitud), int(98 + 500 / 22 + coordenada[1] * 500 / 11))) == (238, 0, 0) or imagen.getpixel((int(1244 + 500 / 22 + coordenada[0] * 500 / 11), int(98 + 500 / 22 + coordenada[1] * 500 / 11 + amplitud))) == (238, 0, 0) or imagen.getpixel((int(1244 + 500 / 22 + coordenada[0] * 500 / 11), int(98 + 500 / 22 + coordenada[1] * 500 / 11 - amplitud))) == (238, 0, 0):
            print("manzana")
        else:
            self.cuerpo.pop(0)
        self.camino.pop(0)
        #print(self.camino)
        print(len(self.cuerpo)-2)


'''
time.sleep(5)
serpi = Serpiente([[2, 5], [3, 5], [4, 5]])
while True:
    if serpi.camino == []:
        #print("hola")
        for paso in serpi.encontrarCamino3(serpi.encontrarManzana()):
            #print(paso)
            serpi.camino.append(paso)
    tiempo = time.time()
    serpi.avanzar(serpi.camino[0])
    print(time.time() - tiempo)
'''


serpi = Serpiente([[2, 5], [3, 5], [4, 5]])
serpi.camino = serpi.camino + [[4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
while True:
    if len(serpi.camino) == 0:
        serpi.camino = serpi.camino + [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10],
                                       [1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1],
                                       [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10],
                                       [3, 10], [3, 9], [3, 8], [3, 7], [3, 6], [3, 5], [3, 4], [3, 3], [3, 2], [3, 1],
                                       [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10],
                                       [5, 10], [5, 9], [5, 8], [5, 7], [5, 6], [5, 5], [5, 4], [5, 3], [5, 2], [5, 1],
                                       [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10],
                                       [7, 10], [7, 9], [7, 8], [7, 7], [7, 6], [7, 5], [7, 4], [7, 3], [7, 2],
                                       [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [8, 10],
                                       [9, 10], [9, 9], [10, 9], [10, 8], [9, 8], [9, 7], [10, 7], [10, 6], [9, 6], [9, 5],
                                       [10, 5], [10, 4], [9, 4], [9, 3], [10, 3], [10, 2], [9, 2], [9, 1], [10, 1], [10, 0],
                                       [9, 0], [8, 0], [8, 1], [7, 1], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0],]


        serpi.camino = serpi.camino + [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10],
                                       [1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1],
                                       [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10],
                                       [3, 10], [3, 9], [3, 8], [3, 7], [3, 6], [3, 5], [3, 4], [3, 3], [3, 2], [3, 1],
                                       [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10],
                                       [5, 10], [5, 9], [5, 8], [5, 7], [5, 6], [5, 5], [5, 4], [5, 3], [5, 2], [5, 1],
                                       [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10],
                                       [7, 10], [7, 9], [7, 8], [7, 7], [7, 6], [7, 5], [7, 4], [7, 3], [7, 2],
                                       [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [8, 10],
                                       [9, 10], [10, 10], [10, 9], [9, 9], [9, 8], [10, 8], [10, 7], [9, 7], [9, 6], [10, 6],
                                       [10, 5], [9, 5], [9, 4], [10, 4], [10, 3], [9, 3], [9, 2], [10, 2], [10, 1], [9, 1],
                                       [9, 0], [8, 0], [8, 1], [7, 1], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0],]
    serpi.avanzar(serpi.camino[0])




'''
serpi = Serpiente([[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [6, 10], [7, 10], [8, 10], [8, 9]])
serpi.encontrarCamino2([0, 0])
'''



###################
##    PRUEBAS    ##
###################

'''
#/Encontrar camino funciona
tiempo = time.time()
print("")
serpi = Serpiente([[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [3, 0]])
serpi.encontrarCamino3([10, 10])
print(time.time() - tiempo)
print("")
'''

'''
#/Comprovar avanzar
serpi = Serpiente([[2, 5], [3, 5], [4, 5], [5, 5]])
serpi.avanzar(0)
'''

'''
#/Comprobar avanzar 2
time.sleep(3)
pasos = [[5, 5], [5, 4], [5, 3], [4, 3], [3, 3], [3, 4], [3, 5], [4, 5]]
serpi = Serpiente([[2, 5], [3, 5], [4, 5]])
while True:
    for i in pasos:
        serpi.avanzar(i)
'''