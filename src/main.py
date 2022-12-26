from random import randrange
import numpy as np
import pygame
import sys



class Main:

	""" Simula el problema del adoquinamiento con interfaz grafica """
	def __init__(self):
		""" Metodo constructor """

		from grid import Grid

		try:
		
			self.size = self.set_size(int(sys.argv[1]))
			#self.size = int(sys.argv[1])
			self.grid = Grid(self.size).get_grid()
			self.screen_size = 650, 650
			self.screen = pygame.display.set_mode(self.screen_size)
			self.colors = self.random_colors(int(np.max(self.grid)))
			self.display()

		except Exception as e:
			raise e

	def display(self):
		""" Permite visualizar la cuadricula """

		pygame.init()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()

			self.draw()
			pygame.display.update()
			self.fill()
			

	def fill(self):
		""" Rellena la cuadricula con adoquines en forma de L """

		border = 8
		dimX = dimY = (620 / self.size) - (border*2)
		max_value = int(np.max(self.grid))

		for i in range(1, max_value + 1):

			for m in range(self.size):
				for n in range(self.size):

					if self.grid[m][n] == i:
						self.draw_square(15 + dimY*m + border + (border*m*2) + 2, 15 + dimX*n + border + (border*n*2) + 2, dimX, dimY, self.colors[i])
			
			pygame.time.wait(200)
			
		

	
	def draw_square(self, x, y, dimX, dimY, color):
		""" Dadas las coordenadas, dimensiones del adoquin y un color, dibuja un cuadrito """

		pygame.draw.rect(self.screen, pygame.Color(color[0], color[1], color[2]), (y, x, dimX, dimY))
		pygame.display.update()

	
	def random_colors(self, max_value):
		""" Genera colores n random """
		return [tuple(np.random.choice(range(256), size = 3)) for i in range(max_value + 1)]


	
	def draw(self):
		""" Dibuja la cuadricula """

		self.screen.fill(pygame.Color('black'))
		pygame.draw.rect(self.screen, pygame.Color('white'), pygame.Rect(15, 15, 620, 620), 4)

		cell_size = 620 / self.size

		for i in range(self.size):
			pygame.draw.line(self.screen, pygame.Color('white'), (15 + (cell_size*i), 15), ((15 + (cell_size*i)), 635), 4)
			pygame.draw.line(self.screen, pygame.Color('white'), (15, 15 + (cell_size*i)), (635, (15 + (cell_size*i))), 4)          

	
	def verify(self, inp):
		""" Verifica si el tamanio es potencia de 2 """

		if inp < 1: return False
		return 0 == (inp & (inp - 1))

	
	def set_size(self, inp):
		""" Establece el tamanio de la cuadricula """
		
		if self.verify(inp): 
			return inp
		else:
			print("Error: No es potencia de 2")


Main()