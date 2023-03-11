from PyQt6 import QtCore, QtGui, QtWidgets,QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QImage,QPixmap
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtCore import Qt
import sys
import cv2

from PIL import Image as im


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setFixedSize(QtCore.QSize(600, 600))
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setGeometry(QtCore.QRect(80, 30, 431, 411))
        self.graphicsView.setStyleSheet("background:rgb(255, 255, 255)")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 470, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        # self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.UpArrowCursor))
        self.pushButton_3.setStyleSheet("background:rgb(96, 255, 109);\n"
"color:black;")
        self.pushButton_3.setObjectName("Select Image")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 470, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        # self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.UpArrowCursor))
        self.pushButton_4.setStyleSheet("background:rgb(96, 255, 109);\n"
"color:black;")
        self.pushButton_4.setObjectName("Convert Image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Picture Converter"))
        self.pushButton_3.setText(_translate("MainWindow", "Select Image"))
        self.pushButton_4.setText(_translate("MainWindow", "Convert Image"))

        self.pushButton_3.clicked.connect(self.SelectPhotofun)
        self.pushButton_4.clicked.connect(self.PhotoConvert)

    def SelectPhotofun(self):
        
        self.file_path, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Open image file', '', 'Images (*.png *.xpm *.jpg *.bmp)')
        image = QImage(self.file_path)

        pixmap = QPixmap.fromImage(image)
        self.item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.item)

        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.item, Qt.AspectRatioMode.KeepAspectRatio)
        self.graphicsView.show()
    
    def PhotoConvert(self):
        # plt.style.use('seaborn')
        img = cv2.imread(self.file_path)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)        
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(img_gray)
        img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
        final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)

        data = im.fromarray(final)

        data.save('image.jpg')
        image = QImage('image.jpg')
        pixmap = QPixmap.fromImage(image)
        self.item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.item, Qt.AspectRatioMode.KeepAspectRatio)
        self.graphicsView.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
