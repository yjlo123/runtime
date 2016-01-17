from sense_hat import SenseHat
import time
import os
from evdev import InputDevice, list_devices, ecodes

sh = SenseHat()

colors = [[0,0,0],[255,255,255],[255,0,0],[255,128,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[102,0,204],[255,0,255]]

cursor = 0
apps = []
app_icons = []

def draw_icon(icon_data):
	img = []
	for code in icon_data:
		img.append(colors[int(code)])
	return img

def transit_right(img):
	global sh
	cur = sh.get_pixels()
	for i in range(1,9):
		tran = []
		for row in range(8):
			for m in range(i,8):
				tran.append(cur[row*8+m])
			for n in range(i):
				tran.append(img[row*8+n])
		sh.set_pixels(tran)
		time.sleep(0.05)

def transit_left(img):
	global sh
	cur = sh.get_pixels()
	for i in range(1,9):
		tran = []
		for row in range(8):
			for n in range(i):
				tran.append(img[row*8+8-i+n])
			for m in range(8-i):
				tran.append(cur[row*8+m])
		sh.set_pixels(tran)
		time.sleep(0.05)

def handle_key(code):
	global cursor
	'''
	if code == ecodes.KEY_DOWN:
		set_pixels(DOWN_PIXELS, colour)
	elif code == ecodes.KEY_UP:
		set_pixels(UP_PIXELS, colour)
	'''
	if code == ecodes.KEY_LEFT:
		if cursor < len(apps)-1:
			cursor += 1
			transit_right(app_icons[cursor])
	elif code == ecodes.KEY_RIGHT:
		if cursor > 0:
			cursor -= 1
			transit_left(app_icons[cursor])
	'''
	elif code == ecodes.KEY_ENTER:
		set_pixels(CENTRE_PIXELS, colour)
	'''

def init():
	global sh
	global apps
	global app_icons
	init_joystick()
	# low light mode
	sh.low_light = True
	# load apps
	current_path = os.path.join(os.path.dirname(__file__), '')
	apps = [d for d in os.listdir(current_path+'app') if os.path.isdir(os.path.join(current_path+'app', d))]
	#print apps
	# load app icons
	for app in apps:
		f = open(current_path+'app/'+app+'/icon', 'r')
		icon_data = f.read()
		app_icons.append(draw_icon(icon_data))
	if len(apps) > 0:
		sh.set_pixels(app_icons[cursor])

def init_joystick():
	global dev
	found = False;
	devices = [InputDevice(fn) for fn in list_devices()]
	for dev in devices:
	  if dev.name == 'Raspberry Pi Sense HAT Joystick':
		found = True;
		break
	if not(found):
		print('Raspberry Pi Sense HAT Joystick not found. Aborting ...')
		exit()

def main_loop():
	global dev
	try:
		for event in dev.read_loop():
			if event.type == ecodes.EV_KEY:
				if event.value == 1:  # key down
					#print "key down"
					handle_key(event.code)
					#sh.set_pixels(app_icons[cursor])
				'''
				if event.value == 0:  # key up
					print "key up"
					#handle_key(event.code)
				'''
	except KeyboardInterrupt:
		sys.exit()

init()
print "Runtime started."
main_loop()