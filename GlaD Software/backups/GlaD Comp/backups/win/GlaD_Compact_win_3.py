import hashlib
import qrcode
import cryptography
import uuid
from PIL import Image
import stepic
import pyaes, pbkdf2, binascii, os, secrets
import secrets
import scrypt
import scapy.all as scapy
from pytube import YouTube
import re
import socket
import os


#############################
							#
com = False                 #
                 			#
entered_text = ('') 		#  
      						#
result =('')				#
							#
end = ('')					#
							#####################################################################
tab = ('                                                                                                             ')#
							#####################################################################				
#############################

GlaD_Editor_text = ('') 

# ----------------- Enigma Settings -----------------
rotors = ("I","II","III")
reflector = "UKW-B"
ringSettings ="ABC"
ringPositions = "DEF" 
plugboard = ""
# ---------------------------------------------------

file_name_qr = ''
input_data_qr = ""

rv_file = ''

no_colored = ""
white_bold = ""
blue_bold = ""
green_bold = ""
red_bold = ""
yellow_bold = ""


text_c=''
s_c=0


text_to_decrypt = ('')
sa = 0

output_d = ('')
entered_text_d = ("")



a = 'jjbjjfjbfjefjebjkerhferr                           	    '
b = 'efeeededeededed											'
c = "'2222eeeeesswdddwdwdw'										"
d = "'wdddwwdwwwdwwdwdd'										"
e = "'wbwejjhßßßßßßßßß°°°°°°°°n'                                " 
f = "'§whjwbflebbllllllllllllllllllll'                          "
g =	'gggggggrrffrfrfff											'
h = '448gg78g222g5g422gg5g11gkdkgnkj							'
i = 'rrrrrrrrrrrrrrkjtrßßß030338457358eztee						'
j = '2007														'
k = '22222222222x2x2228ss8s										'
l = '646533883555655											'
m = '646533883555655646533883555655eweeeweee°°°°				'
n = '°°°°DDwedwdwwdWAAAAAAAAAAAAJ54641122555					'
o = 'asdcjddbejjb555949422228782$$$$$$$44jebfjebjbelj			'
p = "$_aint_good_;)												"
q = 'qwertzuiopadfghjüüäöööäöäööä								'
r = "2222^^^^°°°°°°°°°°°d23228dw								"	
s = '革面洗心王福云马蒂电视台умереть#								'
t = 'офицер云马蒂电视台ть马蒂电		     						'
u = 'умереть马蒂电вместомировойнаучныйуметьдетскийкорабdddkkdjk  '
v = 'омироветь马蒂电клиентофицерzrhhr°°°°°°°°°°°°°°°°°°rh(89)))	'
w = 'ть马蒂电^^^^^^^^^°°°°°°°°°°°ть马蒂电							'
x = '串口串口串口串口串口串口曹书记°°°°%§§$§$$mmoneyyyyyyyyyyyyyyyyyy'
y = '杭州丝绸市场检查率检查率检查率检查率%§§§???ßßßhalloichbinhadinon?' 
z = '曹书记曹书记曹书记曹书记杭州丝绸市场$$%?********+*~~soddontstopme'
sp = "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"


ar = 'jjbjjfjbfjefjebjkerhferr'
br = 'efeeededeededed'
cr = "'2222eeeeesswdddwdwdw'"
dr = "'wdddwwdwwwdwwdwdd'"
er = "'wbwejjhßßßßßßßßß°°°°°°°°n'" 
fr = "'§whjwbflebbllllllllllllllllllll'"
gr =	'gggggggrrffrfrfff'
hr = '448gg78g222g5g422gg5g11gkdkgnkj'
ir = 'rrrrrrrrrrrrrrkjtrßßß030338457358eztee'
jr = '2007'
kr = '22222222222x2x2228ss8s'
lr = '646533883555655'
mr = '646533883555655646533883555655eweeeweee°°°°'
nr = '°°°°DDwedwdwwdWAAAAAAAAAAAAJ54641122555'
op = 'asdcjddbejjb555949422228782$$$$$$$44jebfjebjbelj'
pr = "$_aint_good_;)"
qr = 'qwertzuiopadfghjüüäöööäöäööä'
rr = "2222^^^^°°°°°°°°°°°d23228dw"	
sr = '革面洗心王福云马蒂电视台умереть#'
tr = 'офицер云马蒂电视台ть马蒂电'
ur = 'умереть马蒂电вместомировойнаучныйуметьдетскийкорабdddkkdjk'
vr = 'омироветь马蒂电клиентофицерzrhhr°°°°°°°°°°°°°°°°°°rh(89)))'
wr = 'ть马蒂电^^^^^^^^^°°°°°°°°°°°ть马蒂电'
xr = '串口串口串口串口串口串口曹书记°°°°%§§$§$$mmoneyyyyyyyyyyyyyyyyyy'
yr = '杭州丝绸市场检查率检查率检查率检查率%§§§???ßßßhalloichbinhadinon?' 
zr = '曹书记曹书记曹书记曹书记杭州丝绸市场$$%?********+*~~soddontstopme'
spr = "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

a0 = 'mmudtsirettumenied_:):):):):):):):):):):):):):):):):):):):)'
a1 = 'jibberish_jibberish_jibberish_jibberish_jibberish_jibberish_'
a2 = 'and_ayny_time_you_fell_i_laughft_:):):):):):):):):):):):):)'
a3 = 'jshadjahbdhsdbjkshbwsbsjhfbsjkhbwsjhb62626626266262626266626#'
a4 = '##a#a#a###a#a#########aaadfshduuezueuezzheuzezuzzjzussjzhahah'
a5 = 'aassoottiiaall___________xjfmsefkjsdkjsdfjb wsjdfsjdjh jssdjhh'
a6 = 'deine mutter ist hallo ____________________________--adjh xdks'
a7 = 'my brain_is f*cked hahazhahahahahhahahahahahahahahahahahahahah'
a8 = 'muhahahahahahahahahahahahahahahahqahhahahahahahahhahahahahahah'
a9 = 'its meme_time uiakjh sefjkhb djkfg ailrehiaerjhjsdhfju dhhhhhh'

#bin

ba = "01000001"
bb = "01000010"
bc = "01000011"
bd = "01000100"
be = "01000101"
bf = "01000110"
bg = "01000111"
bh = "01001000"
bi = "01001001"
bj = "01001010"
bk = "01001011"
bl = "01001100"
bm = "01001101"
bn = "01001110"
bo = "01001111"
bp = "01010000"
bq = "01010001"
br = "01010010"
bs = "01010011"
bt = "01010100"
bu = "01010101"
bv = "01010110"
bw = "01010111"
bx = "01011000"
by = "01011001"
bz = "01011010"

b1 = "00110001"
b2 = "00110010"
b3 = "00110011"
b4 = "00110100"
b5 = "00110101"
b6 = "00110110"
b7 = "00110111"
b8 = "00111000"
b9 = "00111001"
b0 = "00111010"

bsp = "00000000"





def end_d():
	global output_d	
	print("")
	file = input(green_bold+'filename> '+no_colored)

	fh = open(file,'w')
	fh.write(output_d) #####################
	fh.close
	on_start()



def end_rv():

	global rv_file	
	print("")
	file = input(green_bold+'filename> '+no_colored)

	fh = open(file,'w')
	fh.write(rv_file) #####################
	fh.close
	on_start()



def write_rv():
	while True:
		global output_d, com
		print('')
		print('write...')
		print(output_d)
		print('')

		question= input (yellow_bold+"do you want to save to file? "+green_bold+"(yes/y) "+red_bold+"(no/n)"+yellow_bold+"> "+no_colored)

		if question == ('y'):
			end_rv()
			
			break

		elif question == ('Y'):
			end_rv()

		if question == ('yes'):
			end_rv()
			
			break

		elif question == ('Yes'):
			end_rv()
			
			
			break

		elif question == ('n'):
			on_start()
	
		elif question == ('N'):
			on_start()

		else:
			on_start()




def write():
	while True:
		global output_d, com
		print('')
		print('write...')
		print(output_d)
		print('')

		question= input (yellow_bold+"do you want to save to file? "+green_bold+"(yes/y) "+red_bold+"(no/n)"+yellow_bold+"> "+no_colored)

		if question == ('y'):
			end_d()
			
			break

		elif question == ('Y'):
			end_d()

		if question == ('yes'):
			end_d()
			
			break

		elif question == ('Yes'):
			end_d()
			
			
			break

		elif question == ('n'):
			on_start()
	
		elif question == ('N'):
			on_start()

		else:
			on_start()



def save():
	global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, ba, bb, bc, bd, be, bf, bg, bh, bi, bj, bk, bl, bm, bn, bo, bp, bq, br, bs, bt, bu, bv, bw, bx, by, bz, b1, b2, b3, b4, b5, b6, b7, b8, b9, b0 , bsp,entered_text, end, tab, com

	for index, letter in enumerate(entered_text):

		updater = (index, letter)

		if updater == (index, 'a'):
			end = end + a 
			print(a)


		elif updater == (index, 'b'):
			end = end + b 
			print(b)

		elif updater == (index, 'c'):
			end = end + c 
			print(c)

		elif updater == (index, 'd'):
			end = end + d 
			print(d)

		elif updater == (index, 'e'):
			end = end + e  
			print(e)

		elif updater == (index, 'f'):
			end = end + f 
			print(f)

		elif updater == (index, 'g'):
			end = end + g 
			print(g)

		elif updater == (index, 'h'):
			end = end + h 
			print(h)

		elif updater == (index, 'i'):
			end = end + i 
			print(i)

		elif updater == (index, 'j'):
			end = end + j 
			print(j)

		elif updater == (index, 'k'):
			end = end + k 
			print(k)

		elif updater == (index, 'l'):
			end = end + l 
			print(l)

		elif updater == (index, 'm'):
			end = end + m 
			print(m)

		elif updater == (index, 'n'):
			end = end + n 
			print(n)

		elif updater == (index, 'o'):
			end = end + o 
			print(o)

		elif updater == (index, 'p'):
			end = end + p 
			print(p)

		elif updater == (index, 'q'):
			end = end + q 
			print(q)

		elif updater == (index, 'r'):
			end = end + r 
			print(r)

		elif updater == (index, 's'):
			end = end + s 
			print(s)

		elif updater == (index, 't'):
			end = end + t 
			print(t)

		elif updater == (index, 'u'):
			end = end + u  
			print(u)

		elif updater == (index, 'v'):
			end = end + v  
			print(v)

		elif updater == (index, 'w'):
			end = end + w 
			print(w)

		elif updater == (index, 'x'):
			end = end + x  
			print(x)

		elif updater == (index, 'y'):
			end = end + y 
			print(y)

		elif updater == (index, 'z'):
			end = end + z 
			print(z)
#
		elif updater == (index, '0'):
			end = end + a0 
			print(a0)

		elif updater == (index, '1'):
			end = end + a1 
			print(a1)

		elif updater == (index, '2'):
			end = end + a2 
			print(a2)

		elif updater == (index, '3'):
			end = end + a3
			print(a3)

		elif updater == (index, '4'):
			end = end + a4 
			print(a4)

		elif updater == (index, '5'):
			end = end + a5
			print(a5)

		elif updater == (index, '6'):
			end = end + a6 
			print(a6)

		elif updater == (index, '7'):
			end = end + a7 
			print(a7)

		elif updater == (index, '8'):
			end = end + a8 
			print(a8)

		elif updater == (index, '9'):
			end = end + a9 
			print(a9)

		elif updater == (index, ' '):
			end = end + sp 
			print(sp)


		else:
			print("")

	on_start()


def decrypt():

	while True:

		global ar, br, cr, dr, er, fr, gr, hr, ir, jr, kr, lr, mr, nr, op, pr, qr, rr, sr, tr, ur, vr, wr, xr, yr, zr, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, entered_text_d, output_d

		starter = input ('')

		if starter == (ar):

			output_d = output_d + 'a'
			print('a')	

		elif starter == (br):
			output_d = output_d + 'b'
			print ('b')

		elif starter == (cr):
			output_d = output_d + 'c'
			print ('c')

		elif starter == (dr):
			output_d = output_d + 'd'
			print ('d')

		elif starter == (er):
			output_d = output_d + 'e'
			print ('e')

		elif starter == (fr):
			output_d = output_d + 'f'
			print ('f')

		elif starter == (gr):
			output_d = output_d + 'g'
			print ('g')

		elif starter == (hr):
			output_d = output_d + 'h'
			print ('h')

		elif starter == (ir):
			output_d = output_d + 'i'
			print ('i')

		elif starter == (jr):
			output_d = output_d + 'j'
			print ('j')

		elif starter == (kr):
			output_d = output_d + 'k'
			print ('k')

		elif starter == (lr):
			output_d = output_d + 'l'
			print ('l')

		elif starter == (mr):
			output_d = output_d + 'm'
			print ('m')

		elif starter == (nr):
			output_d = output_d + 'n'
			print ('n')

		elif starter == (op):
			output_d = output_d + 'o'
			print ('o')

		elif starter == (pr):
			output_d = output_d + 'p'
			print ('p')

		elif starter == (qr):
			output_d = output_d + 'q'
			print ('q')

		elif starter == (rr):
			output_d = output_d + 'r'
			print ('r')

		elif starter == (sr):
			output_d = output_d + 's'
			print ('s')

		elif starter == (tr):
			output_d = output_d + 't'
			print ('t')

		elif starter == (ur):
			output_d = output_d + 'u'
			print ('u')

		elif starter == (vr):
			output_d = output_d + 'v'
			print ('v')

		elif starter == (wr):
			output_d = output_d + 'w'
			print ('w')

		elif starter == (xr):
			output_d = output_d + 'x'
			print ('x')

		elif starter == (yr):
			output_d = output_d + 'y'
			print ('y')

		elif starter == (zr):
			output_d = output_d + 'z'
			print ('z')

		elif starter == (a0):
			output_d = output_d + '0'
			print ('0')

		elif starter == (a1):
			output_d = output_d + '1'
			print ('1')

		elif starter == (a2):
			output_d = output_d + '2'
			print ('2')

		elif starter == (a3):
			output_d = output_d + '3'
			print ('3')

		elif starter == (a4):
			output_d = output_d + '4'
			print ('4')

		elif starter == (a5):
			output_d = output_d + '5'
			print ('5')

		elif starter == (a6):
			output_d = output_d + '6'
			print ('6')

		elif starter == (a7):
			output_d = output_d + '7'
			print ('7')

		elif starter == (a8):
			output_d = output_d + '8'
			print ('8')

		elif starter == (a9):
			output_d = output_d + '9'
			print ('9')

		elif starter == (spr):
			output_d = output_d + ' '
			print (' ')

###################################################################################################


		elif starter == (ba):
			output_d = output_d + 'a'
			print ('a')

		elif starter == (bb):
			output_d = output_d + 'b'
			print ('b')

		elif starter == (bc):
			output_d = output_d + 'c'
			print ('c')

		elif starter == (bd):
			output_d = output_d + 'd'
			print ('d')

		elif starter == (be):
			output_d = output_d + 'e'
			print ('e')

		elif starter == (bf):
			output_d = output_d + 'f'
			print ('f')

		elif starter == (bg):
			output_d = output_d + 'g'
			print ('g')

		elif starter == (bh):
			output_d = output_d + 'h'
			print ('h')

		elif starter == (bi):
			output_d = output_d + 'i'
			print ('i')

		elif starter == (bj):
			output_d = output_d + 'j'
			print ('j')

		elif starter == (bk):
			output_d = output_d + 'k'
			print ('k')		

		elif starter == (bl):
			output_d = output_d + 'l'
			print ('l')

		elif starter == (bm):
			output_d = output_d + 'm'
			print ('m')

		elif starter == (bn):
			output_d = output_d + 'n'
			print ('n')

		elif starter == (bo):
			output_d = output_d + 'o'
			print ('o')

		elif starter == (bp):
			output_d = output_d + 'p'
			print ('p')

		elif starter == (bq):
			output_d = output_d + 'q'
			print ('q')

		elif starter == (br):
			output_d = output_d + 'r'
			print ('r')

		elif starter == (bs):
			output_d = output_d + 's'
			print ('s')

		elif starter == (bt):
			output_d = output_d + 't'
			print ('t')

		elif starter == (bu):
			output_d = output_d + 'u'
			print ('u')

		elif starter == (bv):
			output_d = output_d + 'v'
			print ('v')

		elif starter == (bw):
			output_d = output_d + 'w'
			print ('w')

		elif starter == (bx):
			output_d = output_d + 'x'
			print ('x')

		elif starter == (by):
			output_d = output_d + 'y'
			print ('y')

		elif starter == (bz):
			output_d = output_d + 'z'
			print ('z')

		elif starter == (bsp):
			output_d = output_d + ' '
			print (' ')

		elif starter == ('write'):
			write()

		elif starter == (starter):

			entered_text_d = entered_text_d + starter

		

		

def binary_enc():
	global ba, bb, bc, bd, be, bf, bg, bh, bi, bj, bk, bl, bm, bn, bo, bp, bq, br, bs, bt, bu, bv, bw, bx, by, bz, b1, b2, b3, b4, b5, b6, b7, b8, b9, b0 , bsp, entered_text, end, tab, com

	for index, letter in enumerate(entered_text):

		updater = (index, letter)

		if updater == (index, 'a'):
			end = end + ba 
			print(ba)

		elif updater == (index, 'b'):
			end = end + bb
			print(bb)

		elif updater == (index, 'c'):
			end = end + bc
			print(bc)

		elif updater == (index, 'd'):
			end = end + bd
			print(bd)

		elif updater == (index, 'e'):
			end = end + be
			print(be)

		elif updater == (index, 'f'):
			end = end + bf
			print(bf)

		elif updater == (index, 'g'):
			end = end + bg
			print(bg)

		elif updater == (index, 'h'):
			end = end + bh
			print(bh)

		elif updater == (index, 'i'):
			end = end + bi
			print(bi)

		elif updater == (index, 'j'):
			end = end + bj
			print(bj)

		elif updater == (index, 'k'):
			end = end + bk
			print(bk)

		elif updater == (index, 'l'):
			end = end + bl
			print(bl)

		elif updater == (index, 'm'):
			end = end + bm
			print(bm)

		elif updater == (index, 'n'):
			end = end + bn
			print(bn)

		elif updater == (index, 'o'):
			end = end + bo
			print(bo)

		elif updater == (index, 'p'):
			end = end + bp
			print(bp)

		elif updater == (index, 'q'):
			end = end + bq
			print(bq)

		elif updater == (index, 'r'):
			end = end + br
			print(br)

		elif updater == (index, 's'):
			end = end + bs
			print(bs)

		elif updater == (index, 't'):
			end = end + bt
			print(bt)

		elif updater == (index, 'u'):
			end = end + bu
			print(bu)

		elif updater == (index, 'v'):
			end = end + bv
			print(bv)

		elif updater == (index, 'w'):
			end = end + bw
			print(bw)

		elif updater == (index, 'x'):
			end = end + bx
			print(bx)

		elif updater == (index, 'y'):
			end = end + by
			print(by)

		elif updater == (index, 'z'):
			end = end + bz
			print(bz)

#####################################################################################################################################################

		elif updater == (index, '1'):
			end = end + b1
			print(b1)

		elif updater == (index, '2'):
			end = end + b2
			print(b2)

		elif updater == (index, '3'):
			end = end + b3
			print(b3)

		elif updater == (index, '4'):
			end = end + b4
			print(b4)

		elif updater == (index, '5'):
			end = end + b5
			print(b5)

		elif updater == (index, '6'):
			end = end + b6
			print(b6)

		elif updater == (index, '7'):
			end = end + b7
			print(b7)

		elif updater == (index, '8'):
			end = end + b8
			print(b8)

		elif updater == (index, '9'):
			end = end + b9
			print(b9)

		elif updater == (index, '0'):
			end = end + b0
			print(b0)

		elif updater == (index, ' '):
			end = end + bsp 
			print(bsp)


		else:
			print("")

	on_start()


def encrypt():

	while True:

		global entered_text

		starter = input ("")

		if starter == ("#ch"):

			save()
			break

		elif starter == (starter):

			entered_text=entered_text+starter

def bin():

	while True:

		global entered_text

		starter = input ("")

		if starter == ("#ch"):

			binary_enc()
			break

		elif starter == (starter):

			entered_text=entered_text+starter

def create_qr():

        global input_data_qr, file_name_qr, entered_text

        qr = qrcode.QRCode(
             version=1,
             box_size=10,
               border=5)

        qr.add_data(input_data_qr)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(file_name_qr)
        on_start()


def qr_image_name():

	global input_data_qr, file_name_qr, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, entered_text
	print("")
	filename = input(green_bold+'imagename> '+white_bold,)
	file_name_qr = file_name_qr + filename

	text_qr()



def text_qr():


	global input_data_qr, file_name_qr, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold, entered_text

	print('')

	print(green_bold+'enter text> '+no_colored)

	while True:

		qr_text = input(red_bold+'')

		if qr_text == ("#ch"):
			create_qr()

		elif qr_text == (qr_text):

			input_data_qr=input_data_qr+qr_text


def reverse():

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	global rv_file

	print('')

	rev_inp = input(green_bold+'reverse_text> '+no_colored)

	translated = '' #cipher text is stored in this variable
	i = len(rev_inp) - 1

	while i >= 0:
   		translated = translated + rev_inp[i]
   		i = i - 1
	print(red_bold+translated)
	rv_file = rv_file + translated
	write_rv()



def encrypt_caeser():

    global text_c, s_c, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


    result = ""
 
    print('')

    c_enc_inp = input(green_bold + 'caeser_input> ' + no_colored)

    print('')

    alg_c = int(input(green_bold + 'shifter> ' + no_colored))

    text_c = text_c + c_enc_inp
    s_c = s_c + alg_c



    # traverse text
    for i in range(len(text_c)):
        char = text_c[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s_c-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s_c - 97) % 26 + 97)

    print(red_bold + result)

    on_start()

############################################################################################################################################################################################



def md5():

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	while True:

		print('')

		md5_string = input(yellow_bold+'md5_hash> '+no_colored)

		if md5_string == ('#cd'):

			hashing_menu()
			break


		hash_object = hashlib.md5(md5_string.encode())
		print(green_bold+hash_object.hexdigest())




def double_h():

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	while True:

		print('')

		md5_string = input(yellow_bold+'md5 + sha1_hash> '+no_colored)

		if md5_string == ('#cd'):

			hashing_menu()
			break


		hash_object = hashlib.md5(md5_string.encode())

		md5_out = hash_object.hexdigest()

		print(green_bold+md5_out)

		data = md5_out.encode()

		hash_object = hashlib.sha1(data)
		hex_dig = hash_object.hexdigest()
		print(green_bold+hex_dig)
		print('')






def sha1():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		sha1_string = input(yellow_bold+'sha1_hash> '+no_colored)

		data = sha1_string.encode()

		if sha1_string == ('#cd'):
			hashing_menu()
			break


		hash_object = hashlib.sha1(data)
		hex_dig = hash_object.hexdigest()
		print(green_bold+hex_dig)
		print('')


def sha224():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		sha224_string = input(yellow_bold+'sha224_hash> '+no_colored)

		data = sha224_string.encode()

		if sha224_string == ('#cd'):
			hashing_menu()
			break


		hash_object = hashlib.sha224(data)
		hex_dig = hash_object.hexdigest()
		print(green_bold+hex_dig)
		print('')

def sha256():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		sha256_string = input(yellow_bold+'sha256_hash> '+no_colored)

		data = sha256_string.encode()

		if sha256_string == ('#cd'):
			hashing_menu()
			break


		hash_object = hashlib.sha256(data)
		hex_dig = hash_object.hexdigest()
		print(green_bold+hex_dig)
		print('')

def sha384():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		sha384_string = input(yellow_bold+'sha384_hash> '+no_colored)

		data = sha384_string.encode()

		if sha384_string == ('#cd'):
			hashing_menu()
			break


		hash_object = hashlib.sha384(data)
		hex_dig = hash_object.hexdigest()
		print(green_bold+hex_dig)
		print('')

def sha512():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		sha512_string = input(yellow_bold+'sha512_hash> '+no_colored)

		data = sha512_string.encode()

		if sha512_string == ('#cd'):
			hashing_menu()
			break


		hash_object = hashlib.sha512(data)
		hex_dig = hash_object.hexdigest()
		print(green_bold+hex_dig)
		print('')


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + '' + salt


def OpenSSL():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		print('')

		new_pass = input(yellow_bold+'OpenSSL> '+no_colored)
		if new_pass == ('#cd'):
			hashing_menu()
			break
		hashed_password = hash_password(new_pass)
		print(green_bold+hashed_password)

def blake2s():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		blake2s_string = input(yellow_bold+'blake2s_hash> '+no_colored)

		data = blake2s_string.encode()

		if blake2s_string == ('#cd'):
			hashing_menu()
			break


		hash_object = hashlib.blake2s(data)
		hex_dig = hash_object.hexdigest()
		print(green_bold+hex_dig)
		print('')


def shake_256():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		shake_256_string = input(yellow_bold+'shake_256_hash> '+no_colored)

		data = shake_256_string.encode()

		if shake_256_string == ('#cd'):
			hashing_menu()
			break


		gfg = hashlib.shake_256()
		gfg.update(data)

		print(green_bold)
  
		print(gfg.digest(10))

		print('')

def python_hashing():

	print('')
	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	while True:

		python_hashing_inp = input(yellow_bold+'enter text> '+no_colored)

		if python_hashing_inp == ('#cd'):
			hashing_menu()
			break

		print(green_bold)

		print((hash(python_hashing_inp)))
	

def shake_128():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		shake_128_string = input(yellow_bold+'shake_128_hash> '+no_colored)

		data = shake_128_string.encode()

		if shake_128_string == ('#cd'):
			hashing_menu()
			break


		gfg = hashlib.shake_128()
		gfg.update(data)

		print(green_bold)
  
		print(gfg.digest(10))

		print('')

def AES():
  print('')

  global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

  while True:
    # Derive a 256-bit AES encryption key from the password
    password = input(yellow_bold+'enter AES key> '+no_colored)
    passwordSalt = os.urandom(16)

    key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    print('' + green_bold)
    print(binascii.hexlify(key))
    hashing_menu()
    break


def symmetric_block_cipher():

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	while True:

		password = input(yellow_bold+'SBC_input> '+no_colored)
		salt = secrets.token_bytes(32)
		key = scrypt.hash(password, salt, N=2048, r=8, p=1, buflen=32)
		print('')
		print(green_bold,key)
		hashing_menu()
		break

def ripemd():

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	print('')

	while True:

		x = hashlib.new('ripemd160')

		ripemd_input = input(yellow_bold+'ripemd160> '+no_colored)


		data = ripemd_input.encode()
		x.update(data)

		print(green_bold)

		print(x.hexdigest())

		hashing_menu()
		break

def hashing_menu():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold


	while True:

		hashing_option = input(red_bold+'hash-menu> '+no_colored)

		if hashing_option == ('md5'):
			md5()

		elif hashing_option == ('sha1'):
			sha1()

		elif hashing_option == ('sha224'):
			sha224()

		elif hashing_option == ('sha256'):
			sha256()

		elif hashing_option == ('sha384'):
			sha384()

		elif hashing_option == ('sha512'):
			sha512()

		elif hashing_option == ('OSSL'):
			OpenSSL()

		elif hashing_option == ('cd'):
			on_start()
			break

		elif hashing_option == ('b2s'):
			blake2s()
			break

		elif hashing_option == ('s256'):
			shake_256()
			break

		elif hashing_option == ('ph'):
			python_hashing()
			break

		elif hashing_option == ('s128'):
			shake_128()
			break

		elif hashing_option == ('AES'):
			AES()
			break

		elif hashing_option == ('SBC'):
			symmetric_block_cipher()
			break

		elif hashing_option == ('rip'):
			ripemd()
			break

		elif hashing_option == ('dh'):
			double_h()
			break


		elif hashing_option == ('exit'):
			break


		elif hashing_option == ("help"):
			print(green_bold+"exit    ----------------------->  exit GlaD_Hash")
			print(green_bold+"cd      ----------------------->  sets you back to start")
			print(green_bold+"ph      ----------------------->  python hashing, enter '#cd' to leave python hashing")			
			print(green_bold+"md5     ----------------------->  md5 hashing, enter '#cd' to leave md5")
			print(green_bold+"sha1    ----------------------->  sha1 hashing, enter '#cd' to leave sha1")
			print(green_bold+"sha224  ----------------------->  sha224 hashing, enter '#cd' to leave sha224")
			print(green_bold+"sha256  ----------------------->  sha256 hashing, enter '#cd' to leave sha256")
			print(green_bold+"sha384  ----------------------->  sha384 hashing, enter '#cd' to leave sha384")
			print(green_bold+"sha512  ----------------------->  sha512 hashing, enter '#cd' to leave sha512")
			print(green_bold+"OSSL    ----------------------->  OpenSSL hashing, enter '#cd' to leave OpenSSL")
			print(green_bold+"b2s     ----------------------->  blake2s hashing ,enter '#cd' to leave blake2s")
			print(green_bold+"s256    ----------------------->  shake_256 hashing, enter '#cd' to leave shake_256")
			print(green_bold+"s128    ----------------------->  shake_128 hashing, enter '#cd' to leave shake_128")
			print(green_bold+"rip     ----------------------->  ripemd160 hashing")
			print(green_bold+"AES     ----------------------->  AES hashing")
			print(green_bold+"SBC     ----------------------->  symmetric block cipher hashing")
			print(green_bold+"dh      ----------------------->  double hash including md5 and then sha1")
			print("")

		else:

			print(yellow_bold, "'", hashing_option, "'", "isn't a command try again")


################################################################################################################################################################################################################################################

def steg_enc():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	while True:

		steg_enc = input(yellow_bold+'open file> '+no_colored)

		print()

		text_steg = input(green_bold+'enter text> '+no_colored)


		im = Image.open(steg_enc)

		
		#Encode some text into your Image file and save it in another file
		data = text_steg.encode()

		im1 = stepic.encode(im, data)

		steg_enc_res = input(green_bold+'save file> '+no_colored)

    
		im1.save(steg_enc_res, 'PNG')
		print('')

		steganography()
		break

	#Now is the time to check both images and see if there is any visible changes


def steg_dec():

	print('')

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	while True:

		steg_dec_inp = input(yellow_bold+'filename> '+no_colored)

		im2 = Image.open(steg_dec_inp)
		stegoImage = stepic.decode(im2)
		print('')
		print(green_bold+stegoImage)

		steganography()
		break


def steganography():
	print('')

	while True:


		global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

		steg_input = input(yellow_bold+'steganography_menu> '+no_colored)

		if steg_input == ('senc'):
			steg_enc()
			break

		elif steg_input == ('sdec'):
			steg_dec()
			break

		elif steg_input == ('help'):

			print(green_bold+"senc    ----------------------->  encryption mode")
			print(green_bold+'sdec    ----------------------->  decryption mode')

		elif steg_input == ('cd'):
			on_start()
			break

		else:
			print(red_bold+steg_input, "isnt a command try again")


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
  global rotors, reflector,ringSettings,ringPositions,plugboard
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

  global plugboard, no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

  print("")

  plaintext = input(yellow_bold+"enigma_text> "+no_colored)

  print('')

  pl_board_input = input(red_bold+'plugboard> '+no_colored)
  plugboard = plugboard + pl_board_input

  ciphertext = encode(plaintext)

  print('')

  print(green_bold+ciphertext)
  on_start()


def save_Gl_file():

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	print("")
	print("save...")

	name = input(yellow_bold+"create_filename> "+green_bold)
	
	fh = open(name,'w')
	fh.write(GlaD_Editor_text)
	fh.close
	GlaD_Editor()



def create_Gl_file():

    global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

    while True:

        global GlaD_Editor_text

        file = input (green_bold+"")


        if file == ("#save"):
        	save_Gl_file()
        	break

        elif file == (file):

        	GlaD_Editor_text = GlaD_Editor_text +file
        


def GlaD_Editor():

	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	print('')

	while True:


		command = input(yellow_bold+"GlaD_Editor> "+no_colored)


		if command == ("create"):
			print("")
			create_Gl_file()
			break
		


		elif command ==("cd"):
			on_start()
			break
	

		elif command == ("help"):
			print(green_bold+"cd    -----------------------> back to GlaD Hash menu")
			print(green_bold+"create  -----------------------> creates file")
			print(green_bold+"#save    -----------------------> enter #save to save")
			print('')





		else:
			print(red_bold+command, "isnt a command try again"+no_colored)
			print('')
			
		
def GlaD_Scanner():

  print('')

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
    on_start()




def GlaD_Tube():

    global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

    print('')

    video_name = input(yellow_bold+'video_url> '+no_colored)

    print(yellow_bold+'')

    folder_name = input('folder_name> '+no_colored)
    print('')

    video_list = [video_name]

    #Looping through the list
    for i in video_list:

        try:

            yt = YouTube(i)
            print(green_bold+'Downloading Link: ' + i)
            print(green_bold+'Downloading video: ' + yt.streams[0].title)
        except:
            print(red_bold+"Connection Error")

         #filters out all the files with "mp4" extension
        stream = yt.streams.filter(res="360p").first()
        stream.download(folder_name)
    print(blue_bold+'[*] download finished')
    on_start()

def  on_start():


	global no_colored, white_bold, blue_bold, green_bold, red_bold, yellow_bold

	while True:

		print("")
		
		command = input(yellow_bold+"GlaD_Hash> "+no_colored)


		if command ==("exit"):
			break

	
		elif command ==("enc"):
			encrypt()
			break
	

		elif command ==("dec"):
			decrypt()
			break

		elif command ==("bin"):
			bin()
			break

		elif command == ('qr'):
			qr_image_name()
			break

		elif command == ('rv'):
			reverse()
			break

		elif command == ('ce'):
			encrypt_caeser()
			break

		elif command == ('hs'):
			hashing_menu()
			break

		elif command == ('steg'):
			steganography()
			break

		elif command == ('eni'):
			enigma()
			break

		elif command == ('gle'):
			GlaD_Editor()
			break

		elif command == ('gls'):
			GlaD_Scanner()
			break

		elif command == ('glt'):
			GlaD_Tube()
			break


		elif command == ("help"):
			print(green_bold+"enc     ----------------------->  encryption mode")
			print('dec     ----------------------->  decryption mode + if you want to write everything to a file then just enter "write"')
			print("exit    ----------------------->  exit GlaD_Hash")
			print("bin     ----------------------->  binary encryption")
			print('qr      ----------------------->  converts text to a qr code')
			print('rv      ----------------------->  reverses text')
			print('hs      ----------------------->  hashing menu enter help after entering to find more')
			print('ce      ----------------------->  caesar encryption')
			print('steg    ----------------------->  steganography menu')
			print('eni     ----------------------->  enigma encryption')
			print('gle     ----------------------->  starts implemented GlaD_Editor')
			print('gls     ----------------------->  starts implemented GlaD_Scanner')
			print('glt     ----------------------->  starts implemented GlaD_Tube')
			print('to start a encryption process just type "#ch"')
			print("btw. you can use dec for binary decryption")
			print("")


		else:
			print(red_bold+command, "isnt a command try again")

def slogan():

	print(yellow_bold)

	os.system("figlet GlaD")
	print("")
	print(blue_bold+"******************************************************")
	print(blue_bold+"* Made by Hadinon                                    *")
	print(blue_bold+"* find more tools on https://hadinon.itch.io         *")
	print(blue_bold+"* https://gladnews.000webhostapp.com                 *")
	print(blue_bold+"******************************************************")
	print("")

	on_start()


slogan()

