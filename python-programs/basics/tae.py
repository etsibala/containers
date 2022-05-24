import subprocess
output = subprocess.getoutput("cat /proc/version | grep -i ubuntu")

print ("test " + output.strip() + "tae")
