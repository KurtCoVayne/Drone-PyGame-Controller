import argparse
import configparser
import math
from concurrent.futures.thread import ThreadPoolExecutor
from sys import exit
from threading import Thread
from time import sleep

from database import DatabaseHandler
from drone import DroneHandler, Goal
from models import *


class ClientThread(Thread):
	"""
	
	"""
	def __init__(self, drone_conf, db_conf):
		super(MainThread,self).__init__()

			
		self.droneconn = DroneHandler(drone_conf)
		
		self.dbconn = DatabaseHandler(db_conf)

		if not (self.droneconn.check() or self.dbconn.check):
			raise "Drone Connection nor Database Connection didnt work"

class ServerThread(Thread):
	
	"""
	
	"""
	
	def __init__(self, drone_conf, db_conf):

		super(MainThread,self).__init__()
		self.dbconn = DatabaseHandler(drone_conf['ID'],db_conf)
		self.drone_conf = drone_conf
		if not self.dbconn.check():
			raise "Drone Connection nor Database Connection didnt work"	
		#Get drone status here... initial position and set it
		self.drone = self.dbconn.getDrone()
		if not drone:
			raise "Drone not found"
		
	def run(self):
		import pygame
		WHITE = (255, 255, 255)
		RED   = (255,   0,   0)
		GREEN = (0  , 255,   0)
		BLUE  = (0  ,   0, 255)
		pygame.init()
		W=500
		H=500
		assert W==H,"El canvas debe ser cuadrado"
		def getOffsets(initialCoordinates,x,y,z):
			"""
			W = a metros
			pixel = x
			x= pixel*a/W
			"""
			pixelEquivalent = lambda pix: pix*self.drone_conf['CanvasMetric']/W
			
			return (pixelEquivalent(x),pixelEquivalent(y),z)

		screen = pygame.display.set_mode((W, H))
		done = False
		paused = False
		keep_state = False
		pointer = (W//2,H//2)
		myFont = pygame.font.SysFont("Times New Roman", 14)
		z = self.drone_conf['Altitude']
		while not done:
				for event in pygame.event.get():
						if not self.drone.ready:
							screen.fill([255,255,255])
							readylabel = myFont.render("DRONE NOT READY", 1, RED)
							offset = (len("DRONE NOT READY") // 2) * 14
							screen.blit(readylabel,((W//2) - offset,H//2))
							sleep(1)
							self.drone = self.dbconn.getDrone()
							continue
						keys = pygame.key.get_pressed()
						if not paused:
							screen.fill([0,0,0])
							pointer = pygame.mouse.get_pos() if pygame.mouse.get_focused() else pointer	
							pygame.draw.line(screen,GREEN,(pointer[0], 0),(pointer[0], pointer[1] -3))
							pygame.draw.line(screen,GREEN,(pointer[0], H),(pointer[0], pointer[1] +3))

							pygame.draw.line(screen,RED,(0, pointer[1]),(pointer[0]-3,pointer[1]))
							pygame.draw.line(screen,RED,(W, pointer[1]),(pointer[0]+3,pointer[1]))
							rectangle = pygame.rect.Rect(pointer[0]-2, pointer[1]-2, 6, 6)
							pygame.draw.rect(screen, BLUE, rectangle)

							xLabel = myFont.render(f"X: {pointer[0]-W//2}", 1, WHITE)
							yLabel = myFont.render(f"Y: {pointer[1]-H//2}", 1, WHITE)
							zLabel = myFont.render(f"Z: {z}", 1, WHITE)
							lockedLabel = myFont.render(f"Locked", 1, WHITE)

							screen.blit(xLabel,(4,14))
							screen.blit(yLabel,(4,30))
							screen.blit(zLabel,(4,46))
						if event.type == pygame.QUIT:
								done = True
						if keys[pygame.K_SPACE] and not keep_state:
							paused = not paused
							if paused: 
								screen.blit(lockedLabel,(4,62))
								with ThreadPoolExecutor(max_workers=1) as executor:
									x,y,z = pointer[0],pointer[1],z
									xi,yi,zi = self.drone.initialpos
									goal = GeoCoords(xi,yi,zi)+getOffsets(x,y,0)
									
									future = executor.submit(self.dbconn.setDroneGoal, goal)
									print(future.result())
				pygame.display.flip()

"""
TODO:
Se debe ejecutar el thread principal que se encarga del control del resto de clases
"""
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Ignito DroneLinker CLI entry point')
	parser.add_argument('cfg',help='Config File entry point, read README.md to know how it should look like.',type=str)
	args = parser.parse_args()
	
	config = configparser.ConfigParser()
	config.read(args.cfg)
	envConfig = config['defaults']['envConfig'].lower()

	if envConfig == 'prod' or envConfig == 'production':
		print("STARTING ENVIRONMENT AS PRODUCTION")
		mainThread = MainThread(drone_conf=['drone'],db_conf=config['mongo_database'])
		mainThread.start()
	elif envConfig == 'dev' or envConfig == 'development':
		print("STARTING ENVIRONMENT AS DEVELOPMENT")
		mainThread = MainThread(drone_conf=config['drone'],db_conf=config['mongo_database'])
		mainThread.start()
	else:
		print("Invalid environment in config")
		exit(1)
