import hashlib
import os






no_colored =  ""
white_bold =  ""
blue_bold =   ""
green_bold =  ""
red_bold =    ""
yellow_bold = ""


global_ciphertext = ''

# ----------------- Enigma Settings -----------------
rotors = ("I","II","III")
reflector = "UKW-B"
ringSettings ="ABC"
ringPositions = "DEF" 
plugboard = ""
# ---------------------------------------------------


text_c=''
s_c=0

c_result = ''





def fingerprint(): 

  global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, global_ciphertext

  while True:




    print('')

    md5_string = input(yellow_bold+'fingerprint_text> '+no_colored)


    hash_object = hashlib.md5(md5_string.encode())

    md5_out = hash_object.hexdigest()



    data = md5_out.encode()

    hash_object = hashlib.sha1(data)
    hex_dig = hash_object.hexdigest()


    data_sha224 = hex_dig.encode()

    hash_object_sha224 = hashlib.sha224(data_sha224)
    hex_dig_sha224 = hash_object_sha224.hexdigest()

    print('')
    print(yellow_bold+'This is your secure fingerprint : '+green_bold+hex_dig_sha224)




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

  fingerprint()


slogan()