from sense_hat import SenseHat
from Clock import Clock
import time
import pygame
from pygame.locals import *

class RunTime():
	def __init__(self):
		self.apps = []
		self.apps.append(Clock())
		self.sense = SenseHat()

	def start(self):
		pygame.init()
		pygame.display.set_mode((640,480))
		running = True
		icon = self.apps[0].get_icon()
		self.display_icon(icon)
		'''
		while running:
			for event in pygame.event.get():
				if event.type == QUIT:
					running = False
				else:
					if event.key == K_RIGHT:
						self.sense.clear()
					elif event.key == K_LEFT:
						self.display_icon(icon)
					else:
						running = False
		'''

	def display_icon(self, icon):
		e = [0,0,0]
		padded_icon = []
		for i in range(0, len(icon)):
			padded_icon.append(e)
			padded_icon.extend(icon[i])
			padded_icon.append(e)
		padded_icon.extend([e,e,e,e,e,e,e,e,
							e,e,e,e,e,e,e,e])
		self.sense.set_pixels(padded_icon)
		#time.sleep(4)
		#self.sense.clear()


if __name__ == "__main__":
	rt = RunTime()
	rt.start()
