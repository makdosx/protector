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


import os
import sys
import time


os.system("python /opt/protector/change_ip.py")

os.system("python /opt/protector/change_mac.py")

#sys.stdout.flush()
#time.sleep(40)

os.system("python /opt/protector/progr.py")

os.system("proxychains python /opt/protector/ProtectorBrowser.py")
