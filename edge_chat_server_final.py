import socket, threading

class ClientThread(threading.Thread):

    def __init__(self,ip,port,csocket,user):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = csocket
        self.user = user
        print( "[+] New thread started for "+ip+":"+str(port))

    def run(self):
        print( "Connection from : "+ip+":"+str(port))
        data = "default"
        while len(data):
            data = self.csocket.recv(2048)
            broadcast(clients, self.user + ">".encode() +data)
            # self.csocket.sendall(data)
            print( "Client(%s:%s) sent : %s"%(self.ip, str(self.port), data))

        print( "Client at "+self.ip+" disconnected...")

host = "0.0.0.0"
port = 9055

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,9055))
# tcpsock.listen(10)
# (clientsock, (ip, port)) = tcpsock.accept()

clients = []
# message = clientsock.recv(2048)

def broadcast(clients,message):
    for client in clients:
        client[0].send(message)


while True:
    tcpsock.listen(10)
    (clientsock, (ip, port)) = tcpsock.accept()

    clientsock.send( "Welcome to the chat room!\nWhat is your name?\n".encode())
    username = clientsock.recv(2048)
    broadcast(clients, "\n".encode() + username +"has just joined the chat".encode())

    clients.append([clientsock, username])

    #pass clientsock to the ClientThread thread object being created
    newthread = ClientThread(ip, port, clientsock, username)
    newthread.start()

