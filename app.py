import sys
from PyQt5 import QtTest
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyembedded.rfid_module.rfid import RFID
from ui.app_ui import Ui_MainWindow


class APP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.rfid = RFID(port='COM3', baud_rate=9600)

        self.timer = QTimer()
        self.timer.timeout.connect(self.get_rfid_id)
        self.timer.start(1000)

    def get_rfid_id(self):
        rfid_id = self.rfid.get_id()
        self.ui.lineEdit.setText(str(rfid_id))
        self.ui.left_circle.setStyleSheet("border-radius: 10px; background-color: rgb(0, 255, 0); min-height: 20px; min-width: 20px;")
        self.ui.right_circle.setStyleSheet("border-radius: 10px; background-color: rgb(0, 255, 0); min-height: 20px; min-width: 20px;")
        self.ui.label_2.setText("Thank You")
        QtTest.QTest.qWait(3000)
        self.ui.lineEdit.setText(" ")
        self.ui.left_circle.setStyleSheet("border-radius: 10px; background-color: rgb(255, 0, 0); min-height: 20px; min-width: 20px;")
        self.ui.right_circle.setStyleSheet("border-radius: 10px; background-color: rgb(255, 0, 0); min-height: 20px; min-width: 20px;")
        self.ui.label_2.setText(" ")


app = QApplication(sys.argv)
main_window = APP()
main_window.show()
sys.exit(app.exec_())
