import socket

ip = "127.0.0.1"  # loopback address
port = 5000
#Step1: create a socket
socket = socket.socket()

# Step2: Connect
socket.connect((ip, port))


# Step3: Send or revceive the data

data = socket.recv(1024)
print(data)

socket.send(b"Thanks for sending")



socket.close()
