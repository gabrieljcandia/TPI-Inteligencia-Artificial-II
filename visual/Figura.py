import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import math


class Figura(QDialog):
    #def __init__(self, parent=None):
    def __init__(self, parent, layout):
        super(QDialog, self).__init__(parent)

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

    def graficar(self, clusters):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        for cluster in clusters: #obtiene x,y,z de cada cluster
            x, y = cluster.getPuntosR2()
            ax.scatter(x, y, s=None, color=[cluster.getRGB()])
            if cluster.clusters is not None:
                self.graficarCirculo(cluster)
        plt.autoscale(enable=True, axis='both', tight=None) #habilita autoscale
        self.canvas.draw()

    def graficarCirculo(self, cluster):
        centroide = cluster.obtenerCentroide()
        ptoDistante = cluster.obtenerMayorDistante(centroide)
        radio = cluster.distanciaEuclidea([ptoDistante[0], centroide[0]], [ptoDistante[1], centroide[1]])
        circle = plt.Circle(centroide, radio, color=cluster.getRGB(), fill=False, lw=3)
        plt.gcf().gca().add_artist(circle)
