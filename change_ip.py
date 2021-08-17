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
import subprocess
import ipaddress
import random
import sys


status1, gateway = subprocess.getstatusoutput('route -n|grep "UG"|grep -v "UGH"|cut -f 10 -d " "')

status2, lan = subprocess.getstatusoutput("ls /sys/class/net | grep enp")

status3, wlan = subprocess.getstatusoutput("ls /sys/class/net | grep wl")


default_gateway = gateway[:-1]

for i in range(1):        
        host_id_l = random.choice(range(10,200))
        lan_ip_gen = f'{default_gateway}{host_id_l}'
        

for i in range(1):        
        host_id_w = random.choice(range(10,200))
        wlan_ip_gen = f'{default_gateway}{host_id_w}'


lan_ip = lan_ip_gen 
wlan_ip = wlan_ip_gen  


lan_change_ip = lan +' ' + lan_ip
wlan_change_ip = wlan +' ' + wlan_ip

gateway_beg = default_gateway + '0'
gateway_end = default_gateway + '254'
gateway_all = gateway_beg + ' via ' + gateway_end 


os.system('sudo ifconfig ' + lan_change_ip  + ' netmask 255.255.255.0 up')

os.system('sudo ifconfig ' + wlan_change_ip  + ' netmask 255.255.255.0 up')

os.system('sudo ip route add default via ' + gateway)

os.system("sudo service network-manager restart")


