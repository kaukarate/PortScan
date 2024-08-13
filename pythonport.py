import socket
import subprocess 
import sys
from datetime import datetime

#blank your screen
subprocess.call('clear', shell=True)

#ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#print a banner with information on the host we are about to scan 
print ("_" * 80)
print ("Please wait, scanning remote host", remoteServerIP)
print ("_" * 80)

#Check the date and time the scan was started 
t1 = datetime.now()

#Use range function to specify ports

try:
    for port in range (1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port)) 
        if result == 0:
            print ("Port {}:    Open".format(port)) 
        sock.close()

#Perform error handling 

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#Checking time again 
t2 = datetime.now()

#Calculate the differences in time to know how long the scan took
total = t2 - t1

# Printing the information on the screen
print ('Scanning Completed in: ', total)
