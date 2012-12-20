#!/usr/bin/python
# Should be placed at /opt/piratebox/www/cgi-bin/admin.py

import json

cpustats = open("/proc/cpuinfo", 'r')
cpustat = cpustats.read()
cpustats.close()

uptime = open("/proc/uptime", 'r')
up = uptime.read()
uptime.close()

wireless = open("/etc/config/wireless", 'r')
wifi = wireless.read()
wireless.close()


data = [ { 'uptime': up, 'cpustats': cpustat, 'wireless': wifi } ]
data_string = json.dumps(data)

print "Content-type:application/json\r\n\r\n"
print data_string
