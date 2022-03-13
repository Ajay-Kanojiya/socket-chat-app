import socket

skt = socket.socket()
host = input("Please enter host name of server: ")
port = 5000
skt.connect((host, port))
print("Connected to host server")
while True:
    incoming_message = skt.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server says: ", incoming_message)
    message = input(">> ")
    message = message.encode()
    skt.send(message)
    print("Message has been sent")
