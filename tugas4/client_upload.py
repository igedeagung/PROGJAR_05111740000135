import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

Filename = "PLAINS.png "

print("Sending: " + Filename)
myfile = open("File Client/"+Filename, "rb")
Fil8=Filename.encode("utf-8")
datasend=Fil8+myfile.read()
sock.send(datasend)
print("File sent")
sock.close()