#!/usr/bin/python
#It's supposed to overwrite the wireless options with the data it recieves.
#It might be better if it could change just the SSID instead of having to overwrite the whole file.
#I can't get it to read the data that is being sent

import cgi, datetime, os, re

values = cgi.FieldStorage()
if values.has_key("ssid"):
	ssid = values["ssid"].value
print "Content-type:text/html\n\r\n\r"
print "TEST<br><h2>"
print ssid
print "</h2>"
print cgi.FieldStorage()
print values["ssid"].value
