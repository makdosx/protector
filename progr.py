import sys
from PyQt5 import QtCore, QtGui, QtWidgets     # + QtWidgets


import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore    import QTimer, Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel("""
            <div align=center> 
              <font color=red size=6>
               <b>  
                Παρακαλώ περιμένετε να γίνουν οι κατάλληλες συνδέσεις <br>
                 για να ενεργοποιηθεί ο Protector Browser. <br>
                 Η διάρκεια είναι από 20 έως 30 δευτερόλεπτα. <br>
                 Αμέσως μετά το πρόγραμμα περιήγησης θα είναι έτοιμο προς χρήση. <br> 
                 Πλήρης κάλυψη ηλεκτρονικών αποτυπωμάτων. <br>
                 fake mac address -> router -> proxy -> neural networks (Tor etc)
               </b>
            </font>
                 </div>""")

    # SplashScreen - Indicates that the window is a splash screen. This is the default type for .QSplashScreen
    # FramelessWindowHint - Creates a borderless window. The user cannot move or resize the borderless window through the window system.
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.showMaximized()

    # Automatically exit after  40 seconds
    QTimer.singleShot(30000, app.quit) 
    sys.exit(app.exec_())
