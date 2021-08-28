import hashlib
import os







no_colored =  "\033[0m"   
white_bold =  "\033[1;37m"
blue_bold =   "\033[1;96m"
green_bold =  "\033[1;92m"
red_bold =    "\033[1;91m"
yellow_bold = "\033[1;33m"

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


    md5_string = input(yellow_bold+'fingerprint_text> '+no_colored)


    hash_object = hashlib.md5(md5_string.encode())

    md5_out = hash_object.hexdigest()



    data = md5_out.encode()

    hash_object = hashlib.sha1(data)

    hex_dig = hash_object.hexdigest()

#############################################

    data_sha224 = hex_dig.encode()

    hash_object_sha224 = hashlib.sha224(data_sha224)

    hex_dig_sha224 = hash_object_sha224.hexdigest()

###################################

    data_sha256 = hex_dig_sha224.encode()

    hash_object_sha224 = hashlib.sha256(data_sha256)

    hex_dig_256 = hash_object_sha224.hexdigest()

######################################################


    sha384_string = hex_dig_256

    data_sha384 = sha384_string.encode()

    hash_object_sha384 = hashlib.sha384(data_sha384)

    hex_dig_sha384 = hash_object_sha384.hexdigest()


#######################################################


    sha512_string = hex_dig_sha384

    data_sha512 = sha512_string.encode()


    hash_object_sha512 = hashlib.sha512(data_sha512)

    hex_dig_sha512 = hash_object_sha512.hexdigest()

######################################################



    blake2s_string = hex_dig_sha512

    blake2s_data = blake2s_string.encode()

    blake2s_hash_object = hashlib.blake2s(blake2s_data)
    blake2s_hex_dig = blake2s_hash_object.hexdigest()

######################################################

    #python_hash = (hash(blake2s_hex_dig))
  
######################################################

    print('')
    print(yellow_bold+'This is your secure fingerprint : '+green_bold+blake2s_hex_dig)#str(python_hash))
    print('')







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