import sys

from problema02 import Problema02

from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                              QPushButton,
                              QLabel,
                              QVBoxLayout,
                              QHBoxLayout,
                              QWidget,
                              QFormLayout,
                              QLineEdit,
                              QDialog,
                              QComboBox,
                              QTableWidget,
                              QTableWidgetItem)

class ResultadosWindow(QWidget):
    def __init__(self,resultados):
        super().__init__()
        layout = QVBoxLayout()

        self.lbl_titulo = QLabel('Resultados')
        layout.addWidget(self.lbl_titulo)
        self.table_resultado = QTableWidget()
        self.table_resultado.setRowCount(len(resultados))
        self.table_resultado.setColumnCount(2)
        self.table_resultado.setHorizontalHeaderLabels(['Variable', 'Resultado'])
        layout.addWidget(self.table_resultado)

        self.setLayout(layout)

        # Imprimir resultados en Table
        contador = 0
        for key, value in resultados.items():
            self.table_resultado.setItem(contador, 0, QTableWidgetItem(key))
            self.table_resultado.setItem(contador, 1, QTableWidgetItem(value))
            contador += 1
            
            

class LoadsWindow(QWidget):
    def __init__(self,claros,opcion,lab,cant_ab,lbc,cant_bc,lcd=0, cant_cd=0):
        super().__init__()

        self.w = None # No hay ventana secundaria todavia

        self.claros = int(claros[0])
        self.opcion  = opcion # A, B o C
        self.lab = float(lab)
        self.cant_ab = int(cant_ab)
        self.lbc = float(lbc)
        self.cant_bc = int(cant_bc)
        if (lcd != ""):
            self.lcd = float(lcd)
            self.cant_cd = int(cant_cd)


        layout = QVBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()

        self.lbl_titulo = QLabel("Ingresar Cargas Puntuales")
        layout.addWidget(self.lbl_titulo)
        self.lbl_lab = QLabel('Longitud AB')
        layout.addWidget(self.lbl_lab)
        self.table_ab = QTableWidget()
        self.table_ab.setRowCount(self.cant_ab)
        self.table_ab.setColumnCount(3)
        self.table_ab.setHorizontalHeaderLabels(['Carga', 'Dist apoyo izq.', 'Dist. apoyo der.'])
        layout.addWidget(self.table_ab)
        lbl_carga_dist_ab = QLabel('Carga Dist. en AB = ')
        layout2.addWidget(lbl_carga_dist_ab)
        self.txt_carga_dist_ab = QLineEdit()
        layout2.addWidget(self.txt_carga_dist_ab)
        layout.addLayout(layout2)

        self.lbl_lbc = QLabel('Longitud BC')
        layout.addWidget(self.lbl_lbc)
        self.table_bc = QTableWidget()
        self.table_bc.setRowCount(self.cant_bc)
        self.table_bc.setColumnCount(3)
        self.table_bc.setHorizontalHeaderLabels(['Carga', 'Dist apoyo izq.', 'Dist. apoyo der.'])
        layout.addWidget(self.table_bc)
        lbl_carga_dist_bc = QLabel('Carga Dist. en BC = ')
        layout3.addWidget(lbl_carga_dist_bc)
        self.txt_carga_dist_bc = QLineEdit()
        layout3.addWidget(self.txt_carga_dist_bc)
        layout.addLayout(layout3)

        if self.claros == 3:
            self.lbl_lcd = QLabel('Longitud CD')
            layout.addWidget(self.lbl_lcd)
            self.table_cd = QTableWidget()
            self.table_cd.setRowCount(self.cant_cd)
            self.table_cd.setColumnCount(3)
            self.table_cd.setHorizontalHeaderLabels(['Carga', 'Dist apoyo izq.', 'Dist. apoyo der.'])
            layout.addWidget(self.table_cd)
            lbl_carga_dist_cd = QLabel('Carga Dist. en CD = ')
            layout4.addWidget(lbl_carga_dist_cd)
            self.txt_carga_dist_cd = QLineEdit()
            layout4.addWidget(self.txt_carga_dist_cd)
            layout.addLayout(layout4)

        self.btn_calcular = QPushButton('Calcular')
        self.btn_calcular.clicked.connect(self.calcular)
        layout.addWidget(self.btn_calcular)

        self.setLayout(layout)

    def calcular(self,s):
        #print('Boton Calcular')

        # Extraccion de los datos de las tablas
        # Tabla para claro AB
        cargas_ab = []
        for i in range(self.cant_ab): 
            # empieza en cero por default
            
            carga = {
                'indice': i,
                'carga': self.table_ab.item(i,0).text(),
                'dist_apoyo_izq': self.table_ab.item(i,1).text(),
                'dist_apoyo_der': self.table_ab.item(i,2).text()
            }
            cargas_ab.append(carga)
        print('Cargas AB')
        print(cargas_ab)

        cargas_bc = []

        for i in range(self.cant_bc):

            # Lectura de carga distribuida en cada luz
            dist_ab = float(self.txt_carga_dist_ab.text())
            dist_bc = float(self.txt_carga_dist_bc.text())
            if (self.claros == 3):
                dist_cd = float(self.txt_carga_dist_cd.text())

            # empieza en cero por default

            carga = {
                'indice': i,
                'carga': self.table_bc.item(i,0).text(),
                'dist_apoyo_izq': self.table_bc.item(i,1).text(),
                'dist_apoyo_der': self.table_bc.item(i,2).text()
            }
            cargas_bc.append(carga)
        print('Cargas BC')
        print(cargas_bc)

        if (self.claros ==  3):
            cargas_cd = []
            for i in range(self.cant_cd):
                # empieza en cero por default
                carga = {
                     'indice': i,
                     'carga': self.table_cd.item(i,0).text(),
                     'dist_apoyo_izq': self.table_cd.item(i,1).text(),
                     'dist_apoyo_der': self.table_cd.item(i,2).text()
                     }
                cargas_cd.append(carga)
            print('Cargas CD')
            print(cargas_cd)

        if (self.claros == 2):
            solucion = Problema02(self.claros,self.opcion, self.lab, cargas_ab,dist_ab,self.lbc, cargas_bc,dist_bc)
        elif (self.claros == 3):
            solucion = Problema02(self.claros,self.opcion, self.lab, cargas_ab,dist_ab,self.lbc, cargas_bc,dist_bc,self.lcd,cargas_cd, dist_cd)

        resultado = solucion.procedimiento_principal()

        if self.w is None:
            self.w = ResultadosWindow(resultado)
            self.w.show()


class SecondWindow(QWidget):
    def __init__(self, claros):
        super().__init__()

        self.w = None # No hay ventana secundaria todavia

        self.claros = claros
        layout = QVBoxLayout()
        self.lbl_apoyos = QLabel('Ingresar tipo de apoyos')
        layout.addWidget(self.lbl_apoyos)

        if (self.claros == '2 luces'):
            opciones = ["simplemente apoyada", "esquina A empotrada", "esquina C empotrada"]
            self.cbo_caso = QComboBox()
            self.cbo_caso.addItems(opciones)
            layout.addWidget(self.cbo_caso)
        elif (self.claros == '3 luces'):
            opciones = ["simplemente apoyada", "esquina A empotrada", "esquina D empotrada"]
            self.cbo_caso = QComboBox()
            self.cbo_caso.addItems(opciones)
            layout.addWidget(self.cbo_caso)
        self.label = QLabel("Ingresar Luces")
        layout.addWidget(self.label)
        

       

        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        lbl_lab = QLabel('LAB = ')
        layout1.addWidget(lbl_lab)
        self.txt_lab = QLineEdit()
        layout1.addWidget(self.txt_lab)
        lbl_cant_cargas_ab = QLabel('Cantidad Cargas en AB = ')
        layout1.addWidget(lbl_cant_cargas_ab)
        self.txt_cant_cargas_ab = QLineEdit()
        layout1.addWidget(self.txt_cant_cargas_ab)
        layout.addLayout(layout1)

        lbl_lbc = QLabel('LBC = ')
        layout2.addWidget(lbl_lbc)
        self.txt_lbc = QLineEdit()
        layout2.addWidget(self.txt_lbc)
        lbl_cant_cargas_bc = QLabel('Cantidad Cargas en BC = ')
        layout2.addWidget(lbl_cant_cargas_bc)
        self.txt_cant_cargas_bc = QLineEdit()
        layout2.addWidget(self.txt_cant_cargas_bc)
        layout.addLayout(layout2)

        layout3 = QHBoxLayout()
        lbl_lcd = QLabel('LCD = ')
        layout3.addWidget(lbl_lcd)
        self.txt_lcd = QLineEdit()
        layout3.addWidget(self.txt_lcd)
        lbl_cant_cargas_cd = QLabel('Cantidad Cargas en CD = ')
        layout3.addWidget(lbl_cant_cargas_cd)
        self.txt_cant_cargas_cd = QLineEdit()
        layout3.addWidget(self.txt_cant_cargas_cd)
        layout.addLayout(layout3)

        self.btn_cargas = QPushButton('Ingresar Cargas')
        self.btn_cargas.clicked.connect(self.mostrar_loads_window)
        layout.addWidget(self.btn_cargas)


        if self.claros == "2 luces":
            lbl_lcd.setHidden(True)
            self.txt_lcd.setVisible(False)
            lbl_cant_cargas_cd.setHidden(True)
            self.txt_cant_cargas_cd.setVisible(False)
           

      
        self.setLayout(layout)

       # self.setWindowTitle("Datos claros")

    def mostrar_loads_window(self, s):
        # Lectura de la opcion de  los apoyos
        self.opcion = self.cbo_caso.currentText()
        # Lectura de longitud de claros
        lab = self.txt_lab.text()
        lbc = self.txt_lbc.text()
        lcd = self.txt_lcd.text()
        # Lectura la cantidad de cargas en cada claro
        cant_ab = self.txt_cant_cargas_ab.text()
        cant_bc = self.txt_cant_cargas_bc.text()
        cant_cd = self.txt_cant_cargas_cd.text()

        print(self.claros)
        if self.w is None:
            self.w = LoadsWindow(self.claros,self.opcion, lab,cant_ab, lbc,cant_bc, lcd, cant_cd)
            self.w.show()


        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w = None # No hay ventana secundaria todavia

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()

        lbl_titulo = QLabel('Problema 2')
        layout.addWidget(lbl_titulo)

        lbl_caso =QLabel('Seleccione el caso')
        layout1.addWidget(lbl_caso)

        self.cbo_caso = QComboBox()
        self.cbo_caso.addItems(["2 luces", "3 luces"])
        layout1.addWidget(self.cbo_caso)

        layout.addLayout(layout1)

        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_iniciar.clicked.connect(self.mostrar_second_window)
        layout.addWidget(self.btn_iniciar)



        widget = QWidget()
        widget.setLayout(layout)

        self.setWindowTitle("Problema 02")

        self.setCentralWidget(widget)

    def mostrar_second_window(self, s):
        # Lectura de cantidad de claros
        claros = self.cbo_caso.currentText()
        print(claros)
        if self.w is None:
            self.w = SecondWindow(claros)
            self.w.show()

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()





