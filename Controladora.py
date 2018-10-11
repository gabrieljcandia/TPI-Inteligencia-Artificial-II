from clases.Clases import Cluster

class Controladora:
    clusters = []   #Contiene los ids de todos los clusters existentes.

    def __init__(self):
        self.a = "3" #borrar esta liena

    def leerDatos(self, dir):
        x = []
        y = []
        z = []

        with open(dir, "r") as file:
            lines = []
            for line in file:
                line.strip()  # quita espacios si hubieran
                lines.append(line) #agrega linea en lineas

        #si son 2 dimensiones
        try:
            for line in lines:
                a, b, c = line.split("\t")
                b.rstrip() #quita el \n del final
                x.append(float(a))
                y.append(float(b))
                z.append(float(c))
            datos = (x, y, z)

        #si son 3 dimensiones
        except Exception as inst:
            #x, y, z = []
            for line in lines:
                a, b = line.split("\t")
                b.rstrip() #quita el \n del final
                x.append(float(a))
                y.append(float(b))
            #datos = (x, y)

            clusters = []
            for i in range(x.__len__()):
                print(i)
                miCluster = Cluster(x[i], y[i], 0)
                clusters.append(miCluster)
            print(clusters)

            #prueba relacionar clusters
            nuevoCluster1 = Cluster(1, 2, 0)
            nuevoCluster2 = Cluster(1, 3, 0)
            nuevoCluster3 = Cluster(1, 4, 0)
            nuevoCluster4 = Cluster(1, 5, 0)
            nuevoCluster1.clusters = nuevoCluster2
            nuevoCluster2.clusters = nuevoCluster3
            nuevoCluster3.clusters = nuevoCluster4
            clusters[0].clusters = nuevoCluster1

            #otra prueba similar
            nuevoCluster1 = Cluster(4, 5, 0)
            nuevoCluster2 = Cluster(4, 4, 0)
            nuevoCluster3 = Cluster(3, 3, 0)
            nuevoCluster4 = Cluster(3, 4, 0)
            nuevoCluster1.clusters = nuevoCluster2
            nuevoCluster2.clusters = nuevoCluster3
            nuevoCluster3.clusters = nuevoCluster4
            clusters[1].clusters = nuevoCluster1
        return clusters

    def getClusters(self):
        return self.clusters

    def setClusters(self, clustersAgregar):
        self.clusters = clustersAgregar

    #Agrega el nuevo clúster a la lista de clústers del dominio
    def agregarClusterSuperior(self, nc):
        self.setClusters(self.clusters + nc)

    def simple(self):
        min = 1000000000000000000000000
        clustersUnirse = [] #va a tener los ids de los clusters a fusionarse
        nuevoCluster = Cluster(0, 0, 0) #es el nuevo cluster superior que se creará con el algoritmo
        cn1 = None
        cn2 = None
        dist = 0
        i = 0
        j = 1
        while i < len(self.getClusters()):
            while j < len(self.getClusters()):
                #Verificación de que los clusters evaluados no pertenecen al mismo cluster superior
                if (not self.perteneceAlMismoCluster(self.getClusters()[i], self.getClusters()[j])):
                    #dist = self.getClusters()[i].distanciaEuclidea(self.getClusters()[j].getX(), self.getClusters()[j].getY())
                    dist = self.distanciaClusters(self.getClusters()[i], self.getClusters()[j])
                    if (dist < min):
                        print ("Nueva distancia mínima: ", dist)
                        print ("Entre los clústers: ", self.getClusters()[i].getCoordenadasR2(),", y " ,self.getClusters()[j].getCoordenadasR2())
                        min = dist
                        cn1 = self.getClusters()[i]
                        cn2 = self.getClusters()[j]
                j = j + 1
            i = i + 1
            j = i + 1
        if ((cn1 is not None) & (cn2 is not None)):
            print("El valor del cluster a unir, en la posición 0 es: ", cn1.getCoordenadasR2())
            print("El valor del cluster a unir, en la posición 1 es: ", cn2.getCoordenadasR2())
            cs1 = self.devolverSuperior(cn1)
            print("El valor de cs1, 1, es: ", cs1)
            #nuevoCluster.agregarCluster(cs)
            #nuevoCluster.setClusters(cs1)
            cs2 = self.devolverSuperior(cn2)
            #nuevoCluster.agregarCluster(cs1)
            nuevoCluster.setClusters([cs1, cs2])

            self.agregarClusterSuperior(nuevoCluster)

    def devolverSuperior(self, c):
        retornar = c
        longitud = 0
        for x in self.getClusters():
            cluster = x.getClustersContenidos()
            if ((c in cluster) & (len(cluster) > longitud)):
                min = len(cluster)
                retornar = x
        return retornar

    def perteneceAlMismoCluster(self, c1, c2):
        retorno = False
        for x in self.getClusters(): #Recorro los clusters que contiene el dominio
            if x.hasClusters():
                cAux = x.getClustersContenidos() #Traigo todos los elementos que posee x

                if ((c1 in cAux) & (c2 in cAux)):
                    return True
        #end for
        return retorno

    def distanciaClusters(self, cluster1, cluster2):
        #dist = cluster1.distanciaEuclidea(cluster2.getX(), cluster2.getY())
        retorno = 10000000
        c1 = cluster1.getClustersContenidos()
        c2 = cluster2.getClustersContenidos()

        for x in c1:
            for y in c2:
                dist = x.distanciaEuclidea(y.getX(), y.getY())
                if dist < retorno:
                    retorno = dist

        return retorno







#miControladora = Controladora()
#miControladora.Visual.iniciarVentana()
#miControladora.leerDatos("C:/Users/mejor/Desktop/Libro1.txt")
