import os
import subprocess

adminuser = "root\n"
user = subprocess.check_output('id -un', shell=True, universal_newlines=True)
print "User is: ", user
if user != adminuser:
    print "This script must be run as root user"
    exit (1)
else: 
    print "Welcome root user"
    
if os.path.isdir("/tmp"):
    gpfs_dir = "/tmp/operations"
else:
    gpfs_dir = "/root/operations"

print (gpfs_dir)

