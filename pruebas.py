import math
import random
#3

class Cluster:
    idProximo = 1
    R = []
    G = []
    B = []

    def __init__(self, x, y, z):
        #self.id = self.obtenerNuevaId()
        self.x = x
        self.y = y
        self.z = z
        self.clusters = None #cluster de menor jerarquia
        self.R = self.obtenerColor(self.R)
        self.G = self.obtenerColor(self.G)
        self.B = self.obtenerColor(self.B)

    def obtenerColor(self, col):
        salir = False
        #random.seed(1234124) #para repetir misma secuencia de colores en cada ejecucion, no funciona en Python 3
        while not salir:
            nuevoCol = random.random()
            if nuevoCol not in col:
                salir = True
                col.append(nuevoCol)
        return nuevoCol

    def obtenerNuevaId(self):
        nuevaId = self.idProximo
        self.idProximo = self.idProximo + 1
        return nuevaId

    def setX (self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setZ(self, z):
        self.z = z

    def getZ(self):
        return self.z

    def getId(self):
        return self.id

    def getR(self):
        return self.R

    def getG(self):
        return self.G

    def getB(self):
        return self.B

    def getRGB(self):
        rgb = [self.getR(), self.getG(), self.getB()]
        return rgb

    def getPuntosR2(self):
        x, y = [], []
        x.append(self.getX())
        y.append(self.getY())

        if self.clusters is not None:
            xClusters, yClusters = self.clusters.getPuntosR2()
            for xi in xClusters:
                x.append(xi)
            for yi in yClusters:
                y.append(yi)
            #x.append(xClusters)
            #y.append(yClusters)

        return x, y

    def getCoordenadasR2(self):
        retornar = [self.x, self.y]
        return retornar

    def getCoordenadasR3(self):
        retornar = [self.x, self.y, self.z]
        return retornar

    def hasClusters(self): #devuelve True si el cluster agrupa a otros
        if self.clusters is not None:
            retornar = True
        else:
            retornar = False
        return retornar

    def obtenerCentroide(self):
        x, y = self.getPuntosR2()
        sumX, sumY = 0, 0
        for xi in x: sumX = sumX + xi
        for yi in y: sumY = sumY + yi
        cX = sumX/x.__len__()
        cY = sumY/x.__len__()
        return cX, cY

    def obtenerMayorDistante(self, punto): #devuelve el punto mas distante entre uno dado y los del cluster
        maxDistancia = 0
        ptoDistante = [0, 0]
        puntosClX, puntosClY = self.getPuntosR2()
        pX, pY = punto[0], punto[1]
        for i in range(puntosClX.__len__()):
                dist = self.distanciaEuclidea([pX, puntosClX[i]], [pY, puntosClY[i]])
                if dist > maxDistancia:
                    maxDistancia = dist
                    ptoDistante = [puntosClX[i], puntosClY[i]]
        return ptoDistante

    def distanciaEuclidea(self, x, y): #distancia entre 2 puntos
        dist = math.sqrt( (x[0]-x[1])**2 + (y[0]-y[1])**2 )
        return dist

    def generarClustersAleatorios(self):
        #cantidad
        #desde X, hasta X
        #desde Y, hasta Y
        #desde Z, hasta Z




