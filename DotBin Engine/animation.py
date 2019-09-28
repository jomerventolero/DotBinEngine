''' Sprite Animation '''
import pygame as pg
from constant import FPS

class Animation:
	def __init__(self, sprite_sheet, frame_rate=24, end_frame=0):
		self.clock = pg.time.Clock()
		self.deltaTime = self.clock.tick(1000) / FPS
		self.currentFrame = 0
		self.frameRate = frame_rate
		self.endFrame = end_frame
