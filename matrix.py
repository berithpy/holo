
import re
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

"""
Como conectar
VCC negro 5V
GND blanco gnd
DIN gris 10 mosi 
cs lila 8 ceo
clk azul 11 sclk
"""


def staticText(device,msg):
	with canvas(device) as draw:
		text(draw, (0, 0), msg, fill="white")
	time.sleep(2)

def scrolling_text(device,msg,speed=0.04,font=TINY_FONT):
	show_message(device, msg, fill="white", font=font,scroll_delay=speed)	

def main():
	serial = spi(port=0, device=0, gpio=noop())
	device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
	
	
def ascii_char(device,pic):
	with canvas(device) as draw:
		text(draw, (0, 0), chr(pic), fill="white")
	time.sleep(2)


# def keyboard_2(device):
# 	if keyboard.is_pressed('up'):#if key 'q' is pressed 
# 		ascii_char(device,24)
# 		pass
# 	elif keyboard.is_pressed('down'):
# 		ascii_char(device,25)
# 		pass
# 	elif keyboard.is_pressed('left'):
# 		ascii_char(device,27)
# 		pass
# 	elif keyboard.is_pressed('right'):
# 		ascii_char(device,26)
# 		pass
# 	else:
# 		pass
		
def scrolling_text_flask(msg,speed,font_index=1):
	"""
	This is the code that gets called by the flask app
	msg: String message to scroll(Not UTF-8 compilant)
	speed: speed delay. The higher, the slower.
	font_index: it was easier for us to use numbers 
	instead of the actual font names.
	"""
	serial = spi(port=0, device=0, gpio=noop())
	device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
	fonts=[CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT]
	scrolling_text(device,msg,speed,fonts[font_index])
			

if __name__ == "__main__":
	"""
	Testing code!
	You shouldn't worry about it unless you want to test your led matrix beforehand.
	"""
	serial = spi(port=0, device=0, gpio=noop())
	device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
	fonts=[CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT]
	while True:
		#fi=input("Fuente: 0 CP437_FONT, 1 TINY_FONT,  2 SINCLAIR_FONT, 3 LCD_FONT")
		#keyboard_2(device)
		#speed = input("velocidad")
		#mensaje = str(input("mensaje"))
		#scrolling_text(device,mensaje,speed,fonts[fi])
		#scrolling_text(device,mensaje)
		x=input()
		ascii_char(device,x)
		#with canvas(device) as draw:
		#	text(draw, (0, 0), "R", fill="white")
