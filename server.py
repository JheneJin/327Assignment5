import socket
#initalize TCPSocket
myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#input host and port
hostIP = input("Enter host IP here: ")
hostPort = input("Enter host port here: ")

#bind TCPSocket to hostIp and hostPort
myTCPSocket.bind((str(hostIP), int(hostPort)))
#listening for client port
myTCPSocket.listen(10)
print("Server running and listening for clients on port", hostPort)
#accepts client port
incomingSocket, incomingAddress = myTCPSocket.accept()
print("Server connected to client address")
while True:
    #gets client data from incoming socket
    clientData = incomingSocket.recv(1024).decode("utf-8")
    #if recieves nothin from the client incomingSocket turns off
    if clientData == "":
        incomingSocket.close()
        break
    print("Recived client's message:", clientData)
    #makes the client Data upper case
    serverMessage = clientData.upper()
    #sends the server msg back to the client
    incomingSocket.send(bytes(serverMessage, encoding = "utf-8"))
    print("Message sent back to client:", serverMessage)
print("Server stopped")
