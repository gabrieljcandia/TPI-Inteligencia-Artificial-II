import math
import random


class Cluster:
    idProximo = 1
    R = []
    G = []
    B = []

    def __init__(self, x, y, z):
        self.id = self.obtenerNuevaId()
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
        nuevaId = Cluster.idProximo
        Cluster.idProximo = self.idProximo + 1
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

    def addCluster(self, cluster):
        if self.clusters is None:
            self.clusters = []
        self.clusters.append(cluster)

    def cantPuntos(self): #devuelve el numero de puntos de nivel 0, ingresado por usuario (o autogenerado)
        cant = 0
        if self.clusters is not None:
            for cluster in self.clusters:
                cant = cant + cluster.cantPuntos()
        else:
            cant = cant + 1
        return cant

    def getPuntosR2(self): #modificar para que contemple que clusters sea un array de dos clusters (terminado)
        x, y = [], []
        x.append(self.getX())
        y.append(self.getY())

        if self.clusters is not None:
            for cluster in self.clusters:
                xClusters, yClusters = cluster.getPuntosR2()
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

    def getClusters(self):
        return self.clusters

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

    ########### metodos graficar dendograma #####################

    def getNivel(self, cantPuntos): #devuelve el nivel jerarquico del cluster
        if self.getId() <= cantPuntos:
            nivel = 0
        else:
            nivel = self.getId() - cantPuntos
        return nivel

    def getClusterIzq(self): #devuelve el cluster de nivel inmediatamente inferior que posea, de entre todos sus clusters hijos, la menor ID
        ClIzq = None
        if self.clusters is not None:
            for cl in self.clusters:
                if ClIzq is None or cl.getMenorId() < ClIzq.getMenorId():
                    ClIzq = cl
        else:
            ClIzq = self
        return ClIzq

    def getClusterDer(self): #devuelve el cluster de nivel inmediatamente inferior que posea, de entre todos sus clusters hijos, la mayor ID
        ClDer = None
        if self.clusters is not None:
            for cl in self.clusters:
                if ClDer is None or cl.getMayorId() > ClDer.getMayorId():
                    ClDer = cl
        else:
            ClDer = self
        return ClDer

    def getMenorId(self): #devuelve la menor ID, de entre las IDs de todos los clusters inferiores
        menor = 999999999
        if self.clusters is not None:
            for cl in self.clusters:
                if cl.getMenorId() < menor:
                    menor = cl.getMenorId()
        else:
            menor = self.getId()
        return menor

    def getMayorId(self): #devuelve la mayor ID, de entre las IDs de todos los clusters inferiores
        mayor = 0
        if self.clusters is not None:
            for cl in self.clusters:
                if cl.getMayorId() > mayor:
                    mayor = cl.getMayorId()
        else:
            mayor = self.getId()
        return mayor

    def getLink(self): #devuelve la consecucion de medias entre los puntos de nivel 0 de cada cluster (devuelve la posicion en X, interseccion horizontal-vertical entre nuevo cluster y uno anterior)
        if self.clusters is not None:
            clIzq = self.getClusterIzq()
            clDer = self.getClusterDer()

            linkIzq = clIzq.getLink()
            linkDer = clDer.getLink()

            link = (linkIzq + linkDer) / 2
        else:
            link = self.id
        return link



    #############################################################













