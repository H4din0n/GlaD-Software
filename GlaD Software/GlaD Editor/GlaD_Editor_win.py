  
#import sockets

import os
import time as t

#############################
no_colored =  "" 
white_bold =  ""
blue_bold =   ""
green_bold =  ""
red_bold =    ""
yellow_bold = ""
							#
com = False                 #
                 			#
entered_text = ('') 		#  
a=1							#
b=12      					#
#############################

def test():
	
	global entered_text
	print (entered_text)

def save():

	print("")
	print("save...")

	name = input(yellow_bold+"create_filename>"+no_colored)
	
	fh = open(name,'w')
	fh.write(entered_text)
	fh.close



def create():

    while True:
        global entered_text

        file = input ("")


        if file == ("#save"):
        	save()
        	break

        elif file == (file):

        	entered_text=entered_text+file
        


def start():
	global com

	while not com:



		command = input(yellow_bold+"GlaD_Editor>"+no_colored)


		if command == ("create"):
			print(green_bold+"    ############################### create ###############################"+no_colored)
			print("")
			com = True
			create()
		


		elif command ==("exit"):
			com = True
	

		elif command == ("help"):
			print("exit    -----------------------> exit GlaD_Editor")
			print("create  -----------------------> creates file")
			print("save    -----------------------> enter save to save")

			com = False



		else:
			print(red_bold+command, "isnt a command try again"+no_colored)
			com = False
		


def slogan():
	global com
	
	print(yellow_bold)

	os.system("figlet G l a D")
	print("")
	print(blue_bold+"******************************************************")
	print(blue_bold+"* Made by Hadinon                                    *")
	print(blue_bold+"* find more tools on https://github.com/H4din0n      *")
	print(blue_bold+"*                                                    *")
	print(blue_bold+"******************************************************")
	print("")
	#GD586b44f67445532219fee6479274e926fb82b30c9915f79bc179d1b1e263fb6bID
	start()



slogan()