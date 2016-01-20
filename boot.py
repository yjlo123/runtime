from sense_hat import SenseHat
import time

sense = SenseHat()

colors = [[0,0,0],[255,255,255],[255,0,0],[255,128,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[102,0,204],[255,0,255]]

def cal_color(color, alpha):
	if alpha <= 0:
		return [0,0,0]
	elif alpha >= 1:
		return color
	else:
		return [int(round(float(c)*alpha)) for c in color]

def show_logo():
	blue = [11,19]
	red = [20,21]
	purple = [28,36]
	green = [26,27]
	status = [0, -0.5, -1, -1.5]
	img = []
	for i in range(64):
		img.append([0,0,0])
	for i in range(40):
		status = [x+0.1 for x in status]
		img[red[0]] = cal_color(colors[2], status[0])
		img[red[1]] = cal_color(colors[2], status[0])
		img[purple[0]] = cal_color(colors[9], status[1])
		img[purple[1]] = cal_color(colors[9], status[1])
		img[green[0]] = cal_color(colors[5], status[2])
		img[green[1]] = cal_color(colors[5], status[2])
		img[blue[0]] = cal_color(colors[7], status[3])
		img[blue[1]] = cal_color(colors[7], status[3])
		sense.set_pixels(img)
		time.sleep(0.02)

def refresh_logo_alpha(logo_img, alpha):
	points = [11, 19, 20, 21, 26, 27, 28, 36]
	cur = sense.get_pixels()
	for p in points:
		cur[p] = cal_color(logo_img[p], alpha)
	sense.set_pixels(cur)

def refresh():
	logo_img = sense.get_pixels()
	for n in range(5):
		time.sleep(0.4)
		for i in range(20):
			refresh_logo_alpha(logo_img, (30-i)/30.0)
			time.sleep(0.02)
		for i in range(21):
			refresh_logo_alpha(logo_img, (10+i)/30.0)
			time.sleep(0.02)


show_logo()
refresh()