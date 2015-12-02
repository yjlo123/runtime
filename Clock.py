from BaseApp import BaseApp

class Clock(BaseApp):
	def __init__(self):
		BaseApp.__init__(self)
		self.icon = []
		self.set_icon()

	def set_icon(self):
		e = [0,0,0]
		y = [255,255,0]
		b = [0,0,255]
		self.icon = [[e,y,y,y,y,e],
				[y,e,b,e,e,y],
				[y,e,b,e,e,y],
				[y,e,e,b,e,y],
				[y,e,e,e,b,y],
				[e,y,y,y,y,e]]
	def get_icon(self):
		return self.icon
