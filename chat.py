import socket
import sys
import time

## end of imports ###
###init###

s = socket__socket()
host = socket.gethostname()
print("server will start on host:",host)
port = 8080
s.bind(host .port)
print("")
print("Server done binding to host and port successfully")
print()
s.listen(1)
conn,addr = s.accept()
print(addr,"Has connected to the server and is now online...")
print("")
