import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QButtonGroup

import Controladora
from tkinter import filedialog
from tkinter import Tk
from visual.Figura import Figura

qtCreatorFile = "visual/IGU_Principal.ui" #Nombre del archivo .ui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

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
        self.rbCantClusters.clicked.connect(self.radioButtonCriteriosChange)
        self.rbElemPorCluster.clicked.connect(self.radioButtonCriteriosChange)
        self.rbOptimizarCal.clicked.connect(self.radioButtonCriteriosChange)

        #excepciones
        old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions

    def catch_exceptions(self, t, val, tb):
        QtWidgets.QMessageBox.critical(None,
                                   "An exception was raised",
                                   "Exception type: {}".format(t))
        self.old_hook(t, val, tb)

    def inicializarRbCriterios(self):
        self.rbCantClusters.setChecked(True)
        self.rbGroupCriterios = QtWidgets.QButtonGroup()
        self.rbGroupCriterios.addButton(self.rbCantClusters)
        self.rbGroupCriterios.addButton(self.rbElemPorCluster)
        self.rbGroupCriterios.addButton(self.rbOptimizarCal)

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

    #funciones Visual
    def obtenerUbicacionArch(self):
        Tk().withdraw() #crea una ventana root explicitamente para que el popup de select file no muestre una ventana adicional
        ubicacionArch = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT",".txt"), ("DAT","*.dat")))
        self.txtUbicacion.setPlainText(ubicacionArch)

    def extraerDatosArch(self):
        ubicacionArch = self.txtUbicacion.toPlainText()
        clusters = self.miControladora.leerDatos(self.miControladora, ubicacionArch)
        return clusters

    def generarGraficos(self):
        clusters = self.extraerDatosArch()
        figura1.graficar(clusters)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle("IA - Clustering Jerárquico")
    window.show()

    figura1 = Figura(window, window.VLayoutGrafico)
    #figura2 = Figura(window, window.HLayoutGrafico)
    #figura3 = Figura(window, window.HLayoutGrafico)

    sys.exit(app.exec_())
