import socket

skt = socket.socket()
host = 'localhost'
print("Server started on host: ", host)
port = 5000
skt.bind(('localhost', port))
print("Server binding successfull between host and port")
print("Server is waiting for incoming connection")
skt.listen(1)
connection, address = skt.accept()
print(address, "has connected to the server and is now online...")
while True:
    message = input(">> ")
    message = message.encode()
    connection.send(message)
    print("Message has been sent")
    incoming_message = connection.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client says: ", incoming_message)
