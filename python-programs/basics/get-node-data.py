import os
import subprocess
import sys

if len(sys.argv) == 2:
    FlowCategory = sys.argv[1]
else:
    print ("Invalid argument")
    exit ()

# Standard Querys
OS_DISTRO = "Unknown"
OS_RHEL = subprocess.getoutput("cat /proc/version | grep -i redhat")
if OS_RHEL != "":
    OS_DISTRO = "RHEL"

OS_CENTOS = subprocess.getoutput("cat /proc/version | grep -i centos")
if OS_CENTOS != "":
    OS_DISTRO = "CENTOS"

OS_UBUNTU = subprocess.getoutput("cat /proc/version | grep -i ubuntu")
if OS_UBUNTU != "":
    OS_DISTRO = "UBUNTU"
    
server_uptime = subprocess.getoutput("date -d @$(( $(date +%s) - $(cut -f1 -d. /proc/uptime) )) 2> /dev/null")
server_kernel = subprocess.getoutput("uname -r")

print ("first arg is " + FlowCategory);
print ("distro is " + OS_DISTRO);
print ("uptime is " + server_uptime);
print ("kernel is " + server_kernel);
