from random import randrange
import numpy as np



class Grid:

	""" Simula el problema de adoquinamiento """
	def __init__(self, size):

		""" Crea un nuevo adoquin """
		self.size = size
		self.grid = np.zeros((size, size))
		self.val = 1
		self.pave()

	
	def pave(self):
		""" Adoquina la cuadricula con adoquines en forma de L"""

		self.grid[randrange(self.size)][randrange(self.size)] = 1
		self.ppave(self.size, 0, 0)


	def ppave(self, cur_size, posX, posY):
		""" Adoquina o llena la cuadricula """

		i = 0
		j = 0

		if cur_size == 1:
			self.grid[i][j] = 1
			return


		self.val += 1

		if cur_size == 2:

			for m in range(cur_size):
				for n in range(cur_size):

					y = n + posY
					x = m + posX

					if self.grid[x][y] == 0:
						self.grid[x][y] = self.val
			return

						
		for m in range(posX, cur_size + posX):
			for n in range(posY, cur_size + posY):
				
				if self.grid[m][n] != 0:
					i = m
					j = n

		half1 = posX + cur_size/2 # col
		half2 = posY + cur_size/2 # row

		pos1 = half1 - 1
		pos2 = half2 - 1

		if i < half1 and j >= half2:
			self.set_value((half1, pos2), (half1, half2), (pos1, pos2))


		elif i >= half1 and j >= half2:
			self.set_value((pos1, half2), (half1, pos2), (pos1, pos2))

		elif i >= half1 and j < half2:
			self.set_value((pos1, half2), (half1, half2), (pos1, pos2))


		elif i < half1 and j < half2:
			self.set_value((half1, pos2), (half1, half2), (pos1, half2))

		self.ppave(cur_size/2, half1, posY)
		self.ppave(cur_size/2, posX, half2)
		self.ppave(cur_size/2, posX, posY)
		self.ppave(cur_size/2, half1, half2)


	def set_value(self, (a1, a2), (b1, b2), (c1, c2)):
		""" Dadas tres coordenadas, les asigna un valor """

		self.val += 1

		self.grid[a1][a2] = self.val
		self.grid[b1][b2] = self.val
		self.grid[c1][c2] = self.val

		

	def get_grid(self):
		return self.grid
      
