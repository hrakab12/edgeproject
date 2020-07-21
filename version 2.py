import socket, threading

class ClientThread(threading.Thread):

    def __init__(self,ip,port,csocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = csocket
        print( "[+] New thread started for "+ip+":"+str(port))

    def run(self):
        print( "Connection from : "+ip+":"+str(port))
        data = "default"
        while len(data):
            data = self.csocket.recv(2048)
            self.csocket.sendall(data)
            print( "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data))

        print( "Client at "+self.ip+" disconnected...")

host = "0.0.0.0"
port = 9999

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,9999))

clients = []

while True:
    tcpsock.listen(10)
    clients.append(csocket)
    csocket.send( "Welcome to the chat room!...".encode())
    (clientsock, (ip, port)) = tcpsock.accept()

    #pass clientsock to the ClientThread thread object being created
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()

for client in clients:
    client.sendall("a new client has just joined the chat".encode())
