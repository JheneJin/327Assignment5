import socket
import ipaddress

#initalize TCPSocket
myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
        try:
            #enter the serverIP
            serverIP = str(input("Enter server ip here: "))
            #validates the ip
            ipaddress.ip_address(serverIP)
            break
        except ValueError:
            #displays if user inputs wrong 
            print("Invalid ip address. Please re-enter")
while True:
        try:
            #enter server port
            serverPort = int(input("Enter server port here: "))
            break
        except ValueError:
            #displays if user inputs wrong 
            print("Invalid server port. Please re-enter") 
try:
    #connects the tcp socket to server socket
    myTCPSocket.connect((serverIP, serverPort))
    while True:
        #enter client msg for the user
        clientMessage = str(input("Enter message here: "))
        #entering exit will turn off the client connection to server
        if clientMessage.lower() == 'exit':
            #turns off the socket
            myTCPSocket.close()
            break
        #sneds the client msg to the server
        myTCPSocket.send(bytes(clientMessage, encoding= "utf-8"))
        #echos client msg from the server and displays back to client
        serverResponse = myTCPSocket.recv(1024).decode("utf-8")
        print("Server response:", serverResponse)
except:
    #displays failed connection if serverIP or serverPort are invalid
    print(f"Failed connection of serverIP {serverIP} of port {serverPort}")
print("Client stopped")
