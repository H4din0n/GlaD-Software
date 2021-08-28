import socket
import re

no_colored = "\033[0m"
white_bold = "\033[1;37m"
blue_bold = "\033[1;96m"
green_bold = "\033[1;92m"
red_bold = "\033[1;91m"
yellow_bold = "\033[1;33m"

def sc():

  ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

  port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

  port_min = 0
  port_max = 65535



  open_ports = []

  while True:
      ip_add_entered = input(yellow_bold + "Please enter the ip address that you want to scan> "+no_colored)
      print('')
      if ip_add_pattern.search(ip_add_entered):

        print(f"{ip_add_entered} is a valid ip address")
        break

  while True:

    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    print('')
    port_range = input(yellow_bold+"Enter port range> " + no_colored)
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

  for port in range(port_min, port_max + 1):

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:


          s.settimeout(0.5)
          open_ports.append(port)

    except:

        pass

  for port in open_ports:

    print(f"Port {port} is open on {ip_add_entered}.")



def slogan():



    print(yellow_bold+r"""                  ________   __            __        ______
             /  ______|  | |          /  \      |  ___ \            
            /  /   ____  | |         / /\ \     | |   | | 
            | |   |__ |  | |        / /__\ \    | |   | |
            | \_____| |  | |____   / /____\ \   | |___| |
             \________/  |______| / /      \ \  |______/         """)
    print("")
    print(blue_bold+"           ******************************************************")
    print(blue_bold+"           * Made by Hadinon                                    *")
    print(blue_bold+"           * find more tools on https://hadinon.itch.io         *")
    print(blue_bold+"           * https://gladnews.000webhostapp.com                 *")
    print(blue_bold+"           ******************************************************")
    print("")

    sc()


slogan()
