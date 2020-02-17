import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

Filename = input("Enter namefile ")
filename, file_extension = os.path.splitext(Filename)

sock.send(Filename.encode('utf-8'))
sock.shutdown(socket.SHUT_WR)

data = sock.recv(1024)
if data == b'File not exist':
    print("File not exist")
else:
    f = open(filename + "_client" + file_extension, 'wb')  # open in binary
    while (data):
        f.write(data)
        data = sock.recv(1024)
    print("File received with namefile "+filename+"_client"+file_extension)
    f.close()

print("closing")
sock.close()