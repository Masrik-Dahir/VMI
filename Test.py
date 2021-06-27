import os

a = "~/Downloads/memory/evilprofessor.vmem"
location = 'python2.7 volatility/vol.py imageinfo -f /run/user/1000/doc/e49783ea/zeusbot.mem'
p = os.popen(location).read()