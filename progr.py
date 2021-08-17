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
                  Wait for the appropriate actions to be taken <br>
                  for enable anti-forensics tool, Protector Browser  <br>
                  The duration is from 20 to 30 seconds. <br>
                  Immediately after the browser will be ready for use. <br> 
            </font>
                 </div>

             <div align=center style=background:blue> 
              <font color=white size=5> 
                  Full coverage of digital fingerprints. <br>
                  from the 2nd to the 7th level of OSI. <br>
                  Change of physical address, change of local address (IP), <br>
                  connection to a Proxy server, connection to neural networks, <br>
                  neural networks control and browser function. <br> 
            </div>""")

    # SplashScreen - Indicates that the window is a splash screen. This is the default type for .QSplashScreen
    # FramelessWindowHint - Creates a borderless window. The user cannot move or resize the borderless window through the window system.
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.showMaximized()

    # Automatically exit after  40 seconds
    QTimer.singleShot(30000, app.quit) 
    sys.exit(app.exec_())
