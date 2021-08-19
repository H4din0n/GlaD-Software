import socket
import threading



no_colored =  "\033[0m"   
white_bold =  "\033[1;37m"
blue_bold =   "\033[1;96m"
green_bold =  "\033[1;92m"
red_bold =    "\033[1;91m"
yellow_bold = "\033[1;33m"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

global_nickname = ""

global_message = ""

def GlaD_Chat_connect():

    global global_nickname, client, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, global_message


    print('')
    nickname = input(yellow_bold+"enter nickname> "+no_colored)

    global_nickname = global_nickname + nickname

    # Connecting To Server

    client.connect(('127.0.0.1', 55555))

    receive()

# Listening to Server and Sending Nickname
def receive():

    global global_nickname, client, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, global_message

    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname

            global_message = global_message + client.recv(1024).decode('ascii')

            if global_message == 'NICK':
                client.send(nickname.encode('ascii'))
                write()
            else:
                print(green_bold)
                print(global_message)
        except:
            # Close Connection When Error
            print(red_bold+"An error occured!")
            client.close()
            break

        


# Sending Messages To Server
def write():

    global global_nickname, client, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, global_message

    while True:
        global_message = '{}: {}'.format(global_nickname, input(''))
        client.send(message.encode('ascii'))

        threads()




def threads():

    global global_nickname, client, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, global_message

    # Starting Threads For Listening And Writing
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()



GlaD_Chat_connect()

