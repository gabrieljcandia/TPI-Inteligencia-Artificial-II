import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QButtonGroup

import Controladora
from tkinter import filedialog
from tkinter import Tk

from clases.Clases import Cluster
from visual.Figura import Figura

qtCreatorFile = "visual/IGU_Principal.ui" #Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

qtCreatorFile2 = "visual/frame.ui" #Nombre del archivo .ui
Ui_Frame, QtBaseClass2 = uic.loadUiType(qtCreatorFile2)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #variables
        self.miControladora = Controladora.Controladora

        #botones
        self.btnSelectFile.clicked.connect(self.obtenerUbicacionArch)
        self.btnGenerar.clicked.connect(self.generarGraficos)

        #radio buttons
        self.inicializarRbCriterios()
        self.inicializarRbOrigen()
        self.rbCantClusters.clicked.connect(self.radioButtonCriteriosChange)
        self.rbElemPorCluster.clicked.connect(self.radioButtonCriteriosChange)
        self.rbOptimizarCal.clicked.connect(self.radioButtonCriteriosChange)
        self.rbDesdeArch.clicked.connect(self.radioButtonOrigenChange)
        self.rbGeneracionAleatoria.clicked.connect(self.radioButtonOrigenChange)
        self.rb2D.clicked.connect(self.radioButtonDimensionChange)
        self.rb3D.clicked.connect(self.radioButtonDimensionChange)

        #Spins
        self.spinCantElemPorCluster.valueChanged.connect(self.controlSpinCantElemPorCluster)
        self.spinCantPuntos.valueChanged.connect(self.spinCantChanged)
        self.spinCantClusters.valueChanged.connect(self.controlSpinCantClusters)

        #excepciones
        old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions

    def catch_exceptions(self, t, val, tb):
        QtWidgets.QMessageBox.critical(None,
                                   "An exception was raised",
                                   "Exception type: {}".format(t))
        self.old_hook(t, val, tb)

    #funciones radio buttons
    def inicializarRbCriterios(self):
        self.rbCantClusters.setChecked(True)
        self.rbGroupCriterios = QtWidgets.QButtonGroup()
        self.rbGroupCriterios.addButton(self.rbCantClusters)
        self.rbGroupCriterios.addButton(self.rbElemPorCluster)
        self.rbGroupCriterios.addButton(self.rbOptimizarCal)

    def inicializarRbOrigen(self):
        #origenes
        self.rbGroupOrigen = QtWidgets.QButtonGroup()
        self.rbGroupOrigen.addButton(self.rbDesdeArch)
        self.rbGroupOrigen.addButton(self.rbGeneracionAleatoria)
        #dimensiones
        self.rbGroupDim = QtWidgets.QButtonGroup()
        self.rbGroupDim.addButton(self.rb2D)
        self.rbGroupDim.addButton(self.rb3D)
        #por defecto
        self.rbDesdeArch.setChecked(True)
        self.rb2D.setChecked(True)

    def radioButtonCriteriosChange(self):
        if self.rbCantClusters.isChecked():
            self.spinCantClusters.setEnabled(True)
            self.spinCantElemPorCluster.setEnabled(False)
            self.rbMet1.setEnabled(False)
            self.rbMet2.setEnabled(False)
            print("a")
        if self.rbElemPorCluster.isChecked():
            self.spinCantClusters.setEnabled(False)
            self.spinCantElemPorCluster.setEnabled(True)
            self.rbMet1.setEnabled(False)
            self.rbMet2.setEnabled(False)
            print("b")
        if self.rbOptimizarCal.isChecked():
            self.spinCantClusters.setEnabled(False)
            self.spinCantElemPorCluster.setEnabled(False)
            self.rbMet1.setEnabled(True)
            self.rbMet2.setEnabled(True)
            print("c")

    def radioButtonOrigenChange(self):
        if self.rbDesdeArch.isChecked():
            self.frameUbicacion.setEnabled(True)
            self.frameGeneracionAleatoriaRang.setEnabled(False)
            self.rb2D.setEnabled(False)
            self.rb3D.setEnabled(False)
            print("a")
        if self.rbGeneracionAleatoria.isChecked():
            self.frameUbicacion.setEnabled(False)
            self.frameGeneracionAleatoriaRang.setEnabled(True)
            self.rb2D.setEnabled(True)
            self.rb3D.setEnabled(True)
            self.radioButtonDimensionChange()
            self.controlSpinCantElemPorCluster(self.spinCantElemPorCluster.value())
            self.controlSpinCantClusters(self.spinCantClusters.value())
            print("b")

    def radioButtonDimensionChange(self):
        if self.rb2D.isChecked():
            self.spinZmin.setEnabled(False)
            self.spinZmax.setEnabled(False)
        if self.rb3D.isChecked():
            self.spinZmin.setEnabled(True)
            self.spinZmax.setEnabled(True)

    #funciones Spins
    def controlSpinCantElemPorCluster(self, val):
        if val > self.spinCantPuntos.value() and self.spinCantPuntos.isEnabled():
            self.spinCantElemPorCluster.setValue(self.spinCantPuntos.value())

    def controlSpinCantClusters(self, val): #para CantidadClusters
        if val < self.spinCantPuntos.value() and self.spinCantPuntos.isEnabled():
            self.spinCantClusters.setValue(self.spinCantPuntos.value())
        elif (val > self.spinCantPuntos.value() + self.spinCantPuntos.value() - 1) and (self.spinCantPuntos.isEnabled()):
            self.spinCantClusters.setValue(self.spinCantPuntos.value() + self.spinCantPuntos.value() - 1)

    def spinCantChanged(self, val):
        self.controlSpinCantElemPorCluster(self.spinCantElemPorCluster.value())
        self.controlSpinCantClusters(self.spinCantClusters.value())

    #funciones Visual
    def obtenerUbicacionArch(self):
        Tk().withdraw() #crea una ventana root explicitamente para que el popup de select file no muestre una ventana adicional
        ubicacionArch = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT",".txt"), ("DAT","*.dat")))
        self.txtUbicacion.setPlainText(ubicacionArch)

    def extraerDatosArch(self):
        ubicacionArch = self.txtUbicacion.toPlainText()
        clusters = self.miControladora.leerDatosArch(self.miControladora, ubicacionArch)
        return clusters

    def generarGraficos(self):
        '''if self.rbDesdeArch.isChecked():
            clusters = self.extraerDatosArch()
        if self.rbGeneracionAleatoria.isChecked():
            if self.rb2D.isChecked():
                clusters = self.miControladora.generarPuntosAleatorios2D(self.miControladora,
                                                                     self.spinCantPuntos.value(),
                                                                     self.spinXmin.value(),
                                                                     self.spinXmax.value(),
                                                                     self.spinYmin.value(),
                                                                     self.spinYmax.value())
            if self.rb3D.isChecked():
                clusters = self.miControladora.generarPuntosAleatorios3D(self.miControladora,
                                                                     self.spinCantPuntos.value(),
                                                                     self.spinXmin.value(),
                                                                     self.spinXmax.value(),
                                                                     self.spinYmin.value(),
                                                                     self.spinYmax.value(),
                                                                     self.spinZmin.value(),
                                                                     self.spinZmax.value())'''

        self.frame = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.frame)
        self.frame.show()

        self.ui.spinCantClusters.valueChanged.connect(self.editCantClusters)

        #prueba
        Cluster.idProximo = 1
        cluster = self.miControladora.pruebaClustersStaticos(self.miControladora) #para probar el dendograma

        graficoSL = Figura(self.ui, self.ui.VLgraficoSL)
        graficoSL.graficar(cluster)

        self.dendograma = Figura(self.ui, self.ui.VLgraficoDendograma)
        self.dendograma.graficarDendograma(cluster, self.spinCantClusters.value()) #se pasa el cluster de mayor jerarquia
        #figura2 = Figura(self.ui, self.ui.VLgraficoCL)
        #figura2.graficar(clusters)
        #figura3 = Figura(self.ui, self.ui.VLgraficoAL)
        #figura3.graficar(clusters)

    def editCantClusters(self):
        Cluster.idProximo = 1
        cluster = self.miControladora.pruebaClustersStaticos(self.miControladora) #para probar el dendograma
        self.dendograma.graficarDendograma(cluster, self.ui.spinCantClusters.value())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle("IA - Clustering Jerárquico")
    window.show()

    #figura1 = Figura(window, window.VLgraficoArbol)
    #figura2 = Figura(window, window.VLgraficoSL)
    #figura3 = Figura(window, window.VLgraficoCL)
    #figura4 = Figura(window, window.VLgraficoAL)

    #figura2 = Figura(window, window.HLayoutGrafico)
    #figura3 = Figura(window, window.HLayoutGrafico)

    sys.exit(app.exec_())
