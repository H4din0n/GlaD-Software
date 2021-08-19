import socket
import threading



no_colored =  "\033[0m"   
white_bold =  "\033[1;37m"
blue_bold =   "\033[1;96m"
green_bold =  "\033[1;92m"
red_bold =    "\033[1;91m"
yellow_bold = "\033[1;33m"



host = '127.0.0.1'
port = 55555


clients = []
nicknames = []


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def GlaD_Chat_host():

    server.bind((host, port))
    server.listen()
    receive()



def broadcast(message):

    global host, port, server, clients, nicknames

    for client in clients:
        client.send(message)

def handle(client):

    global host, port, server, clients, nicknames


    while True:
        try:

            message = client.recv(1024)
            broadcast(message)
        except:

            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():

    global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold
    global host, port, server, clients, nicknames


    while True:

        print(yellow_bold)

        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))


        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

GlaD_Chat_host()