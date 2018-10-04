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

    def distanciaClusters (self, c1, c2):
        min = 1000000 #el valor que representa a la mínima distancia entre los clusters

        if c1.hasClusters:
            dist = self.distanciaClusters(c1.getClusters, c2)
        else:
            if c2.hasClusters:
                dist = self.distanciaClusters(c1, c2.getClusters)
            else:
                dist = self.distanciaClusters(c1, c2)
        if dist < min:
                min = dist
                dist = 1000000


        dist = c1.distanciaEuclidea(c2.getX(), c2.getY())






#miControladora = Controladora()
#miControladora.Visual.iniciarVentana()
#miControladora.leerDatos("C:/Users/mejor/Desktop/Libro1.txt")
