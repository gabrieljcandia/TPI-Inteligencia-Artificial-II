import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import math


class Figura(QDialog):
    def __init__(self, parent, layout):
        super(Figura, self).__init__(parent=None)


        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        #self.button.clicked.connect(self.plot)

        # set the layout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        #layout.addWidget(self.button)
        self.setLayout(layout)

    def graficar(self, clusters): #recibe como parametro un grupo de clusters; ver si no conviene pasar solo el cluster de mayor nivel, y recorrer los demas desde ese
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        for cluster in clusters.getClusters():
            x, y = cluster.getPuntosR2()
            ax.scatter(x, y, s=None, color=[cluster.getRGB()])
            if cluster.clusters is not None:
                self.graficarCirculo(cluster)
        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()

    def graficarDendograma(self, cluster, maxClusters=None, maxElemPorCluster=None): #recibe como parametro inicial el cluster de mayor nivel
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        cantPuntos = cluster.cantPuntos() #devuelve cantidad de puntos original
        cantClusters = cluster.getId() #devuelve cantidad de clusters total
        if cantPuntos < cluster.getId() and cantPuntos >= 2: #control de errores
            self.graficarDendogramaCluster(cluster, cantPuntos, cantClusters, maxClusters, maxElemPorCluster)

        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()

    def graficarDendogramaCluster(self, cluster, cantPuntos, cantClusters, maxClusters=None, maxElemPorCluster=None):
        if cluster.clusters is not None:
            if (maxClusters is None) or (cluster.getId() <= cantClusters - (cantClusters - maxClusters)):
                nivel = cluster.getNivel(cantPuntos)
                clIzq = cluster.getClusterIzq()
                clDer = cluster.getClusterDer()
                hIzq = clIzq.getNivel(cantPuntos)
                hDer = clDer.getNivel(cantPuntos)
                xIzq = clIzq.getLink()
                xDer = clDer.getLink()

                self.ax.plot([xIzq, xIzq, xDer, xDer],[hIzq, nivel, nivel, hDer], color=cluster.getRGB())

            for cl in cluster.clusters:
                self.graficarDendogramaCluster(cl, cantPuntos, cantClusters, maxClusters, maxElemPorCluster)

    def graficarCirculo(self, cluster):
        centroide = cluster.obtenerCentroide()
        ptoDistante = cluster.obtenerMayorDistante(centroide)
        radio = cluster.distanciaEuclidea([ptoDistante[0], centroide[0]], [ptoDistante[1], centroide[1]])
        circle = plt.Circle(centroide, radio, color=cluster.getRGB(), fill=False, lw=3)
        plt.gcf().gca().add_artist(circle)




