#!/usr/bin/python

#
#  Copyright (c) 2021 Barchampas Gerasimos <makindosxx@gmail.com>.
#  protector is anonymous browser using gateways of the onion router.
#
#  protector is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  protector is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import sys
from PyQt5 import QtCore, QtGui, QtWidgets     # + QtWidgets


import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore    import QTimer, Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel("""
            <div align=center style=background:purple>
                  <br>  
                 <img src=/opt/protector/prot.png height=200 width=200> <br>
             <font color=white size=5>
                 Περιμένετε ώστε να γίνουν οι κατάλληλες ενέργειες <br>
                 για να ενεργοποιηθεί ο Protector Browser. <br>
                 Η διάρκεια είναι από 20 έως 30 δευτερόλεπτα. <br>
                 Αμέσως μετά το πρόγραμμα περιήγησης θα είναι έτοιμο προς χρήση. <br> 
            </font>
                 </div>

             <div align=center style=background:blue> 
              <font color=white size=5> 
                 Πλήρης κάλυψη ηλεκτρονικών αποτυπωμάτων. <br>
                 απο το 2ο έως το 7ο επίπεδο του OSI. <br>
                 Αλλαγή Φυσικής διευθυνσιοδότησης, αλλαγή τοπικής διευθύνσης (IP), <br>
                 σύνδεση σε Διακομιστή μεσολάβησης, σύνδεση σε νευρωνικά δίκτυα, <br>
                 έλεγχος νευρωνικών δικτύων και λειτουργία φυλλομετρητή. <br>
            </div>""")

    # SplashScreen - Indicates that the window is a splash screen. This is the default type for .QSplashScreen
    # FramelessWindowHint - Creates a borderless window. The user cannot move or resize the borderless window through the window system.
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.showMaximized()

    # Automatically exit after  40 seconds
    QTimer.singleShot(30000, app.quit) 
    sys.exit(app.exec_())
