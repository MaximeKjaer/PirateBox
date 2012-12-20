#!/usr/bin/python

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