import socket

ip = "127.0.0.1"  # loopback address
port = 5000
#ip2 = socket.gethostname()
#print(ip2)



# Step1: Create a scoket
socket = socket.socket(socket.SOCK_STREAM, socket.IF_INET)

# Step2: Bind the server address + port = 0 to 65535  ==> (0 to 1024) reserved ports
socket.bind((ip, port))

# Step3: Listen to the cleint connection
socket.listen(5)

print("Server is waiting....")

# Step4: accept the conection
while True:

     cleint_id , clinet_addr = socket.accept()
     print("Request accepted from the client : {}".format(clinet_addr))
     cleint_id.send(b"Hi I am a server how can I help you")

     data = cleint_id.recv(1024)
     print("Data from the clint: {}".format(data))
     cleint_id.close()


# Step5: Send or Receive the data 

# Step6: Cloase the connection
