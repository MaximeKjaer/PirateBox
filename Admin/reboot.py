#!/usr/bin/python
##When called by the Admin-panel, reboots the PirateBox
## Doesn't work yet.

import subprocess, sys

shell = subprocess.Popen(["sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
script = open("./testing.sh", "r").read()
shell.stdin.write(script + "\n")
shell.stdin.write("env\n")
shell.stdin.close
print script
for line in shell.stdout:
	print line
	name, value = line.strip().split("=", 1)
	os.environ[name] = value

