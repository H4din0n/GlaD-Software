import hashlib
import os
import time






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

gl_hash = ''

gl_cipher_text = ''

count = 0

eni_ch_inp = ''

gl_eni_text = ''

def caesarShift(str, amount):
    output = ""

    for i in range(0,len(str)):
        c = str[i]
        code = ord(c)
        if ((code >= 65) and (code <= 90)):
            c = chr(((code - 65 + amount) % 26) + 65)
        output = output + c
    
    return output

def encode(plaintext):
  global rotors, reflector,ringSettings,ringPositions,plugboard,no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold
  #Enigma Rotors and reflectors
  rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  rotor1Notch = "Q"
  rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  rotor2Notch = "E"
  rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  rotor3Notch = "V"
  rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  rotor4Notch = "J"
  rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
  rotor5Notch = "Z" 
  
  rotorDict = {"I":rotor1,"II":rotor2,"III":rotor3,"IV":rotor4,"V":rotor5}
  rotorNotchDict = {"I":rotor1Notch,"II":rotor2Notch,"III":rotor3Notch,"IV":rotor4Notch,"V":rotor5Notch}  
  
  reflectorB = {"A":"Y","Y":"A","B":"R","R":"B","C":"U","U":"C","D":"H","H":"D","E":"Q","Q":"E","F":"S","S":"F","G":"L","L":"G","I":"P","P":"I","J":"X","X":"J","K":"N","N":"K","M":"O","O":"M","T":"Z","Z":"T","V":"W","W":"V"}
  reflectorC = {"A":"F","F":"A","B":"V","V":"B","C":"P","P":"C","D":"J","J":"D","E":"I","I":"E","G":"O","O":"G","H":"Y","Y":"H","K":"R","R":"K","L":"Z","Z":"L","M":"X","X":"M","N":"W","W":"N","Q":"T","T":"Q","S":"U","U":"S"}
  
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  rotorANotch = False
  rotorBNotch = False
  rotorCNotch = False
  
  if reflector=="UKW-B":
    reflectorDict = reflectorB
  else:
    reflectorDict = reflectorC
  
  #A = Left,  B = Mid,  C=Right 
  rotorA = rotorDict[rotors[0]]
  rotorB = rotorDict[rotors[1]]
  rotorC = rotorDict[rotors[2]]
  rotorANotch = rotorNotchDict[rotors[0]]
  rotorBNotch = rotorNotchDict[rotors[1]]
  rotorCNotch = rotorNotchDict[rotors[2]]
  
  rotorALetter = ringPositions[0]
  rotorBLetter = ringPositions[1]
  rotorCLetter = ringPositions[2]
  
  rotorASetting = ringSettings[0]
  offsetASetting = alphabet.index(rotorASetting)
  rotorBSetting = ringSettings[1]
  offsetBSetting = alphabet.index(rotorBSetting)
  rotorCSetting = ringSettings[2]
  offsetCSetting = alphabet.index(rotorCSetting)
  
  rotorA = caesarShift(rotorA,offsetASetting)
  rotorB = caesarShift(rotorB,offsetBSetting)
  rotorC = caesarShift(rotorC,offsetCSetting)
  
  if offsetASetting>0:
    rotorA = rotorA[26-offsetASetting:] + rotorA[0:26-offsetASetting]
  if offsetBSetting>0:
    rotorB = rotorB[26-offsetBSetting:] + rotorB[0:26-offsetBSetting]
  if offsetCSetting>0:
    rotorC = rotorC[26-offsetCSetting:] + rotorC[0:26-offsetCSetting]

  ciphertext = ""
  
  #Converplugboard settings into a dictionary
  plugboardConnections = plugboard.upper().split(" ")
  plugboardDict = {}
  for pair in plugboardConnections:
    if len(pair)==2:
      plugboardDict[pair[0]] = pair[1]
      plugboardDict[pair[1]] = pair[0]
  
  plaintext = plaintext.upper()  
  for letter in plaintext:
    encryptedLetter = letter  
    
    if letter in alphabet:
      #Rotate Rotors - This happens as soon as a key is pressed, before encrypting the letter!
      rotorTrigger = False
      #Third rotor rotates by 1 for every key being pressed
      if rotorCLetter == rotorCNotch:
        rotorTrigger = True 
      rotorCLetter = alphabet[(alphabet.index(rotorCLetter) + 1) % 26]
      #Check if rotorB needs to rotate
      if rotorTrigger:
        rotorTrigger = False
        if rotorBLetter == rotorBNotch:
          rotorTrigger = True 
        rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
  
        #Check if rotorA needs to rotate
        if (rotorTrigger):
          rotorTrigger = False
          rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]
             
      else:
          #Check for double step sequence!
        if rotorBLetter == rotorBNotch:
          rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
          rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]
        
      #Implement plugboard encryption!
      if letter in plugboardDict.keys():
        if plugboardDict[letter]!="":
          encryptedLetter = plugboardDict[letter]
    
      #Rotors & Reflector Encryption
      offsetA = alphabet.index(rotorALetter)
      offsetB = alphabet.index(rotorBLetter)
      offsetC = alphabet.index(rotorCLetter)

      # Wheel 3 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorC[(pos + offsetC)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetC +26)%26]
      
      # Wheel 2 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorB[(pos + offsetB)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetB +26)%26]
      
      # Wheel 1 Encryption
      pos = alphabet.index(encryptedLetter)
      let = rotorA[(pos + offsetA)%26]
      pos = alphabet.index(let)
      encryptedLetter = alphabet[(pos - offsetA +26)%26]
      
      # Reflector encryption!
      if encryptedLetter in reflectorDict.keys():
        if reflectorDict[encryptedLetter]!="":
          encryptedLetter = reflectorDict[encryptedLetter]
      
      #Back through the rotors 
      # Wheel 1 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetA)%26]
      pos = rotorA.index(let)
      encryptedLetter = alphabet[(pos - offsetA +26)%26] 
      
      # Wheel 2 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetB)%26]
      pos = rotorB.index(let)
      encryptedLetter = alphabet[(pos - offsetB +26)%26]
      
      # Wheel 3 Encryption
      pos = alphabet.index(encryptedLetter)
      let = alphabet[(pos + offsetC)%26]
      pos = rotorC.index(let)
      encryptedLetter = alphabet[(pos - offsetC +26)%26]
      
      #Implement plugboard encryption!
      if encryptedLetter in plugboardDict.keys():
        if plugboardDict[encryptedLetter]!="":
          encryptedLetter = plugboardDict[encryptedLetter]

    ciphertext = ciphertext + encryptedLetter
  
  return ciphertext

#Main Program Starts Here
def enigma():

    global plugboard, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, eni_ch_inp, gl_cipher_text, gl_eni_text

    print("")

    plaintext = eni_ch_inp

    print('')

    pl_board_input = input(red_bold+'plugboard> '+no_colored)

    plugboard = plugboard + pl_board_input

    ciphertext = encode(plaintext)

    gl_eni_text = gl_eni_text + ciphertext

    write()


def write():

    global plugboard, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, eni_ch_inp, gl_cipher_text, gl_eni_text


    gl_cipher_text = gl_cipher_text + gl_eni_text
    print('')
    fingerprint()




def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                    len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
    
# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
            ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
    
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
            ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))





    
# Driver code
def veg():

    global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, global_ciphertext, gl_hash, gl_cipher_text, count, eni_ch_inp



    string = input(yellow_bold+'fingerprint_text> '+no_colored)
    print('')
    keyword = input(yellow_bold+'keyword> '+no_colored)


    key = generateKey(string, keyword)
    cipher_text = cipherText(string,key)

    eni_ch_inp = eni_ch_inp + cipher_text

    #print(cipher_text)



    enigma()
#cipher_text


def fingerprint(): 

    global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, global_ciphertext, gl_hash, gl_cipher_text, count



    md5_string = gl_cipher_text #input(yellow_bold+'fingerprint_text> '+no_colored)



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
    time.sleep(1)
    print(yellow_bold+'This is your secure fingerprint : '+green_bold+blake2s_hex_dig)
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
    #2e7dbc2ad6ffd4647b7435b5912126f415b365ab4372758a9eed4e82a3f0d63f
    veg()

