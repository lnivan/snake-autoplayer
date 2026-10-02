import random
from ctypes import windll
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
from PIL import ImageGrab
import time
def pathFinder2DGrid(grid):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    #applePosition = [random.randint(0, 10), random.randint(0, 10)]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 3:
                applePosition = [x, y]
            if grid[x][y] == 2:
                snakeHeadPosition = [x, y]
    pathsChecked = [[snakeHeadPosition]]
    pathFound = False
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
    
'''grid = [[0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,2,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,3,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]]'''
#print(pathFinder2DGrid(grid)) 

'''def posicionManzana():
    image = ImageGrab.grab()
    for x in range(int(1286 + 46 / 2), int(1286 + 506 - 46 / 2), 46):
        for y in range(int(87 + 46 / 2), int(87 + 506 - 46 / 2), 46):
            if image.getpixel((x, y)) == (255, 0, 0):
                return([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)])
            elif image.getpixel((x, y)) == (0, 255, 0):
                print("blanco")


time.sleep(5)
print("ya")
snakePos = [[2,5], [3,5], [4,5]]

def makeGrid():
    grid = [[0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]]
    time.sleep(0.1)
    for i in snakePos:
        if i == snakePos[len(snakePos) - 1]:
            grid[i[0]][i[1]] = 2
        else:
            grid[i[0]][i[1]] = 1
    applePos = posicionManzana()

    grid[applePos[0]][applePos[1]] = 3
    return(grid)



grid = makeGrid()

caminoSeguido = pathFinder2DGrid(grid)

direccion = [caminoSeguido[0][0] - snakePos[len(snakePos) - 1][0], caminoSeguido[0][1] - snakePos[len(snakePos) - 1][1]]   
if direccion == [1, 0]:
    press("d", 0.1)
    print("h")
elif direccion == [-1, 0]:
    press('a', 0.1)
    print("h")
elif direccion == [0, 1]:
    press('w', 0.1)
    print("h")
elif direccion == [0, -1]:
    press('s', 0.1)
    print("h")
caminoSeguido.pop(0)
snakePos.append([direccion[0] + snakePos[len(snakePos) - 1][0], direccion[1] + snakePos[len(snakePos) - 1][1]])
if len(caminoSeguido) != 0:
    snakePos.pop(0)

    

while True:
    time.sleep(0.1)
    #print("ya")
    #press("d")
    print(caminoSeguido)
    image = ImageGrab.grab()
    if len(caminoSeguido) == 0:
        grid = makeGrid()
        caminoSeguido = pathFinder2DGrid(grid)
    #if image.getpixel((int(snakePos[len(snakePos) - 1][0] * 46 + 1286 + 46 / 2), int(snakePos[len(snakePos) - 1][1] * 46 + 87 + 46 / 2))) == (50, 255, 50):
    if 1 == 1:
        direccion = [caminoSeguido[0][0] - snakePos[len(snakePos) - 1][0], caminoSeguido[0][1] - snakePos[len(snakePos) - 1][1]]   
        if direccion == [1, 0]:
            press('d', 0.1)
            print("h")
        elif direccion == [-1, 0]:
            press('a', 0.1)
            print("h")
        elif direccion == [0, 1]:
            press('w', 0.1)
            print("h")
        elif direccion == [0, -1]:
            press('s', 0.1)
            print("h")
        caminoSeguido.pop(0)
        snakePos.append([direccion[0] + snakePos[len(snakePos) - 1][0], direccion[1] + snakePos[len(snakePos) - 1][1]])
        if len(caminoSeguido) != 0:
            snakePos.pop(0)'''





'''

snakePosition = [[2, 5], [3, 5], [4, 5]]
def posicionManzana():
    image = ImageGrab.grab()
    for x in range(int(1286 + 46 / 2), int(1286 + 506 - 46 / 2 + 1), 46):
        #print("caca")
        for y in range(int(87 + 46 / 2), int(87 + 506 - 46 / 2 + 1), 46):
            if image.getpixel((x, y)) == (238, 0, 0):
                return([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)])
    return([0, 0])

def crearCuadricula(snakePos):
    grid = [[0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]]
    for i in snakePos:
        if i == snakePos[len(snakePos) - 1]:
            grid[i[0]][i[1]] = 2
        else:
            grid[i[0]][i[1]] = 1
    manzanaPosicion = posicionManzana()
    grid[manzanaPosicion[0]][manzanaPosicion[1]] = 3
    return(grid)

def siguientesPasos(cuadricula):
    pasos = pathFinder2DGrid(cuadricula)
    return(pasos)



pasosSiguientes = []

def avanzar():
    global pasosSiguientes
    if len(pasosSiguientes) == 0:
        pasosSiguientes = siguientesPasos(crearCuadricula(snakePosition))
    pasoSiguiente = pasosSiguientes[0]
    direccion = [pasoSiguiente[0] - snakePosition[len(snakePosition) - 1][0], pasoSiguiente[1] - snakePosition[len(snakePosition) - 1][1]]
    if direccion == [1, 0]:
        press("d", 0.1)
        print("h")
    elif direccion == [-1, 0]:
        press('a', 0.1)
        print("h")
    elif direccion == [0, -1]:
        press('w', 0.1)
        print("h")
    elif direccion == [0, 1]:
        press('s', 0.1)
        print("h")
    snakePosition.append([direccion[0] + snakePosition[len(snakePosition) - 1][0], direccion[1] + snakePosition[len(snakePosition) - 1][1]])
    snakePosition.pop(0)
    pasosSiguientes.pop(0)

time.sleep(5)
running = True
''''''while running == True:
    #image = ImageGrab.grab()
    #if image.getpixel((snakePosition[len(snakePosition) - 1][0] * 46 + 1286 + 46 / 2, snakePosition[len(snakePosition) - 1][1] * 46 + 87 + 46 / 2)) == (109, 255, 24):
    if 1 == 1:
        tiempo = time.time()
        avanzar()
        print(tiempo)
        time.sleep(0.05)


def posicionManzanasertgpfodisujherdfngtre():
    tiempo = time.time()
    grid = [[0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]]
    image = ImageGrab.grab()
    for x in range(int(1286 + 46 / 2) + 10, int(1286 + 506 - 46 / 2 + 1) + 10, 46):
        #print("caca")
        for y in range(int(87 + 46 / 2), int(87 + 506 - 46 / 2 + 1), 46):
            if image.getpixel((x, y)) == (238, 0, 0):
                print([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)], "manzana")
            if image.getpixel((x, y)) == (109, 255, 24):
                print([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)], "serpi")
            if image.getpixel((x, y)) == (255, 255, 255):
                print([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)], "serpiC")
    
    print(time.time() - tiempo)
i = 0
while True:
    print(i)
    posicionManzanasertgpfodisujherdfngtre()
    i = i + 1'''
'''
#Solo la primara vez
snakePosition = [[2, 5], [3, 5], [4, 5]]
applePosition = [0, 0]
direccion = [[0, 0]]
caminoPorSeguir = []
ejecutandose = True
caminoDeTransicion = False

#Funcion que devuelve la posición de la manzana
def encontrarPosicionManzana():
    imagen = ImageGrab.grab()
    for x in range(int(1284 + 46 / 2), int(1284 + 496 - 46 / 2 + 1), 45):
        for y in range(int(98 + 46 / 2), int(98 + 496 - 46 / 2 + 1), 45):
            if imagen.getpixel((x, y)) == (238, 0, 0):
                return([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)])

#Funcion para hacer la cuadricula y poder encontrar el camino
def crearCuadricula(posicionSerpiente, posicionManzana):
    cuadricula = [[0 for i in range(11)] for i in range(11)]
    #if posicionManzana == None:
     #   posicionManzana = [random.randint(0, 10), random.randint(0, 10)]
    cuadricula[posicionManzana[0]][posicionManzana[1]] = 3
    for i in posicionSerpiente:
        if i == posicionSerpiente[len(posicionSerpiente) - 1]:
            cuadricula[i[0]][i[1]] = 2  
        else:
            cuadricula[i[0]][i[1]] = 1
    return(cuadricula)

#Funcion para sacar posicion de pixel en pantalla de coordenada en juego
def coordenadaAPixel(coordenada):
    return((coordenada[0] * 45 + 1307, coordenada[1] * 45 + 121))

#Funcion para repetir en cada paso(avanzar por el camino)
def avanzar():
    time.sleep(0)
    direccion = [caminoPorSeguir[0][0] - snakePosition[len(snakePosition) - 1][0], caminoPorSeguir[0][1] - snakePosition[len(snakePosition) - 1][1]]
    if direccion == [1, 0]:
        press("d", 0.1)
        print("h")
    elif direccion == [-1, 0]:
        press('a', 0.1)
        print("h")
    elif direccion == [0, -1]:
        press('w', 0.1)
        print("h")
    elif direccion == [0, 1]:
        press('s', 0.1)
        print("h")
    caminoPorSeguir.pop(0)
    snakePosition.append([direccion[0] + snakePosition[len(snakePosition) - 1][0], direccion[1] + snakePosition[len(snakePosition) - 1][1]])
    if len(caminoPorSeguir) != 0:
        snakePosition.pop(0)

#Funcion para hacer un nuevo camino
def nuevoCamino():
    global caminoDeTransicion
    if caminoDeTransicion:
        nuevoObjetivo = [random.randint(0, 10), random.randint(0, 10)]
        caminoNuevo = pathFinder2DGrid(crearCuadricula(snakePosition, nuevoObjetivo))
        while caminoNuevo in snakePosition:
            caminoNuevo = pathFinder2DGrid(crearCuadricula(snakePosition, nuevoObjetivo))
        caminoDeTransicion = False
    else:
        applePosition = encontrarPosicionManzana()
        caminoNuevo = pathFinder2DGrid(crearCuadricula(snakePosition, applePosition))
        caminoDeTransicion = True
    return(caminoNuevo)

#Como la primera vez esta parada y es diferente, el primer movimineto es diferente y se hace fuera del bucle
time.sleep(5)
caminoPorSeguir = nuevoCamino()
tiempo = time.time()
avanzar()

#Todo el rato
while ejecutandose == True:
    tiempo = time.time()
    if len(caminoPorSeguir) == 0:
        caminoPorSeguir = nuevoCamino()
    imagen = ImageGrab.grab()
    if imagen.getpixel(coordenadaAPixel(snakePosition[len(snakePosition) - 1])) != (0, 0, 0):
        avanzar()
    print(time.time() - tiempo)
    print(snakePosition[len(snakePosition) - 1])
'''
'''
tiempoExcedido = 0
while ejecutandose == True:
    if len(caminoPorSeguir) == 0:
        caminoPorSeguir = nuevoCamino()
    if time.time() - tiempo >= 1/7 - tiempoExcedido:
        tiempoExcedido = (time.time() - tiempo) - (1/7 - tiempoExcedido)
        tiempo = time.time()
        avanzar()
    print(time.time() - tiempo)
    print(snakePosition[len(snakePosition) - 1])
    #print(snakePosition)
    '''



class Pila:
    def __init__(self):
        self.pila = []
    
    def meter(self, objeto):
        self.pila += objeto

    def sacar(self):
        return(self.pila.pop(0))
'''
caca = Pila()
caca.meter(8)
caca.meter(9)
caca.meter(10)
print(caca.sacar())
print(caca.sacar())'''


def rgba(colorref):
    mask = 0xff
    devolvicion =  [(colorref & (mask << (i * 8))) >> (i * 8) for i in range(4)]
    devolvicion.pop()
    return(devolvicion)

'''

tiempo = time.time()
image = ImageGrab.grab().load()
if image[1632, 773] == (54,113,44):
    print("lol")
print(time.time() - tiempo)


tiempo = time.time()
image = ImageGrab.grab()
if image.getpixel((1632, 773)) == (54,113,44):
    print("lol")
print(time.time() - tiempo)


tiempo = time.time()
hdc = windll.user32.GetDC(0)
#print(rgba(windll.gdi32.GetPixel(hdc,1632,773)))
if rgba(windll.gdi32.GetPixel(hdc,1632,773)) == (54,113,44):
    print("lol")
print(time.time() - tiempo)


'''

hdc = windll.user32.GetDC(0)
'''
def encontrarPosicionManzana():
    imagen = ImageGrab.grab()
    for x in range(1270, 1270 + 45 * 10 + 1, 45):
        for y in range(112, 112 + 45* 10 + 1, 45):
            if rgba(windll.gdi32.GetPixel(hdc, x, y)) == [238, 0, 0]:
                return([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)])



def caminoAManzana(posicionSerpiente, posicionManzana):
    cuadricula = [[0 for i in range(11)] for i in range(11)]
    for i in posicionSerpiente:
        if i == posicionSerpiente[len(posicionSerpiente) - 1]:
            cuadricula[i[0]][i[1]] = 2
        else:
            cuadricula[i[0]][i[1]] = 1
    cuadricula[posicionManzana[0]][posicionManzana[1]]
    return(pathFinder2DGrid(cuadricula))

'''

'''

time.sleep(3)
serpiCabezaPos = [4,4]
recorrido=["w","w","a","a","a","s","s","s","d","d","d","w"]
print("ya")
pixelesExtra = 10
press("w", 0.01)
time.sleep(random.uniform(0.01, 0.07))
while True:
    for paso in recorrido:
        tiempo = time.time()
        while rgba(windll.gdi32.GetPixel(hdc, serpiCabezaPos[0] * 45 + 1270 + pixelesExtra, serpiCabezaPos[1] * 45 + 112)) != [109, 255, 24] and rgba(windll.gdi32.GetPixel(hdc, serpiCabezaPos[0] * 45 + 1270 - pixelesExtra, serpiCabezaPos[1] * 45 + 112)) != [109, 255, 24] and rgba(windll.gdi32.GetPixel(hdc, serpiCabezaPos[0] * 45 + 1270, serpiCabezaPos[1] * 45 + 112 + pixelesExtra)) != [109, 255, 24] and rgba(windll.gdi32.GetPixel(hdc, serpiCabezaPos[0] * 45 + 1270, serpiCabezaPos[1] * 45 + 112 - pixelesExtra)) != [109, 255, 24]:
            True
        tiempo2 = time.time()
        press(paso, 0.01)
        if paso == "w":
            serpiCabezaPos[1] = serpiCabezaPos[1] - 1
        elif paso == "s":
            serpiCabezaPos[1] = serpiCabezaPos[1] + 1
        elif paso == "a":
            serpiCabezaPos[0] = serpiCabezaPos[0] - 1
        else:
            serpiCabezaPos[0] = serpiCabezaPos[0] + 1
        #print(time.time() - tiempo, time.time() - tiempo2)
'''
'''
time.sleep(3)
serpiCabezaPos = [4,5]
recorrido=["w","w","w","a","a","a","s","s","s","d","d","d",]
print("ya")
tiempoExtra = 0
vez1 = True
while True:
    tiempoTranscurrido = time.time()
    for paso in recorrido:
        press(paso, 0.01)
        if paso == "w":
            serpiCabezaPos[1] = serpiCabezaPos[1] - 1
        elif paso == "s":
            serpiCabezaPos[1] = serpiCabezaPos[1] + 1
        elif paso == "a":
            serpiCabezaPos[0] = serpiCabezaPos[0] - 1
        else:
            serpiCabezaPos[0] = serpiCabezaPos[0] + 1
        if vez1 == True:
            vez1 = False
            while time.time() - tiempoTranscurrido <= 1/14:
                True
            tiempoExtra = (time.time() - tiempoTranscurrido) - 1/14
        else:
            while time.time() - tiempoTranscurrido <= 1/7 - tiempoExtra:
                True
            tiempoExtra = (time.time() - tiempoTranscurrido) - (1/7 - tiempoExtra)
        print(time.time() - tiempoTranscurrido)
        tiempoTranscurrido = time.time()
'''




image = ImageGrab.grab()
while True:
    serpiente = []
    xx = 0
    tiempo = time.time()
    for x in range(int(1244 + (500 / 11) / 2), int(1743 - (500 / 11) / 2 + 2), int(500 / 11)):
        #print("caca")
        serpiente.append([])
        for y in range(int(98 + (500 / 11) / 2), int(597 - (500 / 11) / 2 + 2), int(500 / 11)):
            if image.getpixel((x, y)) == (238, 0, 0):
                #print([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)], "manzana")
                serpiente[xx].append("M")
            elif image.getpixel((x, y)) == (109, 255, 24):
                #print([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)], "serpi")
                serpiente[xx].append("S")
            else:
                serpiente[xx].append("N")
        xx = xx + 1
    print("")
    print(serpiente)
    print(time.time() - tiempo)
            #if image.getpixel((x, y)) == (255, 255, 255):
             #   print([int((x - (1286 + 46 / 2)) / 46), int((y - (87 + 46 / 2)) / 46)], "serpiC")