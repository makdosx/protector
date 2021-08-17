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
import random
import subprocess


status1, lan = subprocess.getstatusoutput("ls /sys/class/net | grep enp")

status2, wlan = subprocess.getstatusoutput("ls /sys/class/net | grep wl")


mac_lan = ':'.join(("%012x" % random.randint(0, 0xFFFFFFFFFFFF))[i:i+2] for i in range(0, 12, 2))
mac_wlan = ':'.join(("%012x" % random.randint(0, 0xFFFFFFFFFFFF))[i:i+2] for i in range(0, 12, 2))


os.system('sudo ifconfig ' + lan + ' down')
os.system("sudo ifconfig  '"+ lan +"'  hw ether '"+ mac_lan +"'")
os.system('sudo ifconfig ' + lan + ' up')


os.system('sudo ifconfig ' + wlan + ' down')
os.system("sudo ifconfig  '"+ wlan +"'  hw ether '"+ mac_wlan +"'")
os.system('sudo ifconfig ' + wlan + ' up')

os.system("sudo service network-manager restart")