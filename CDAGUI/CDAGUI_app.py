import sys
import serial
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from CDAGUI import Ui_MainWindow

class Test(QMainWindow):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.FIREbutton.pressed.connect(self.fire)
        self.ui.sendsirial_1.pressed.connect(self.submit1)
        self.ui.sendsirial_2.pressed.connect(self.submit2)
        self.ui.sendsirial_3.pressed.connect(self.submit3)
        self.ui.sendsirial_4.pressed.connect(self.submit4)
        self.ui.sendsirial_5.pressed.connect(self.submit5)
        self.ui.sendsirial_6.pressed.connect(self.submit6)
        self.ui.sendsirial_7.pressed.connect(self.submit7)
        self.ui.sendsirial_8.pressed.connect(self.submit8)
        self.ui.sendsirial_9.pressed.connect(self.submit9)
        self.ui.sendsirial_10.pressed.connect(self.submit10)

        #self.ui.DebugLabel.setText("aaaaa")

    def fire(self):
        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes('f', 'UTF-8'))
        ser.close()

    def submit1(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_1.value())
        time2 = str(self.ui.endtime_1.value())

        senddata ='00'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit2(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_2.value())
        time2 = str(self.ui.endtime_2.value())

        senddata ='01'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit3(self):
            # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_3.value())
        time2 = str(self.ui.endtime_3.value())

        senddata ='02'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit4(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_4.value())
        time2 = str(self.ui.endtime_4.value())

        senddata ='03'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit5(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_5.value())
        time2 = str(self.ui.endtime_5.value())

        senddata ='04'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit6(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_6.value())
        time2 = str(self.ui.endtime_6.value())

        senddata ='05'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit7(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_7.value())
        time2 = str(self.ui.endtime_7.value())

        senddata ='06'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit8(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_8.value())
        time2 = str(self.ui.endtime_8.value())

        senddata ='07'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit9(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_9.value())
        time2 = str(self.ui.endtime_9.value())

        senddata ='08'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

    def submit10(self):
        # self.ui.starttime_1.value()

        time1 = str(self.ui.starttime_10.value())
        time2 = str(self.ui.endtime_10.value())

        senddata ='09'+time1.zfill(3)+time2.zfill(3)

        ser = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=None)
        ser.write(bytes(senddata, 'UTF-8'))
        ser.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
