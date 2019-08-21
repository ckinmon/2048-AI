import random
import sys
import math
import time
from BaseAI_3 import BaseAI

class PlayerAI(BaseAI):
	def __init__(self):
		self.maxDepth = 6
		self.exponent = 1

	def getMove(self, grid):
		move = self.expectiminimax(grid)
		if move is None:
			return random.choice(grid.getAvailableMoves())[0]
		return move 

	def expectiminimax(self, grid):
		best_move = self.maximize(grid, 0, -sys.maxsize - 1, sys.maxsize )
		return best_move[0]

	def maximize(self, grid, depth, alpha, beta):

		if self.cutoffTest(grid, depth):
			return ( None, self.evaluate(grid) )
		
		direction, maxUtility = None, (-sys.maxsize - 1)
		for move in grid.getAvailableMoves():
			utility = self.chance(move[1], depth + 1, alpha, beta)
			if utility > maxUtility:
				direction, maxUtility = move[0], utility
			
			if maxUtility >= beta:
				break

			alpha = max(alpha, maxUtility)
		
		return ( direction, maxUtility )

	def chance(self, grid, depth, alpha, beta):

		if self.cutoffTest(grid, depth):
			return self.evaluate(grid)

		left = 0.9 * self.minimize(grid, depth + 1, 2, alpha, beta)
		right = 0.1 * self.minimize(grid, depth + 1, 4, alpha, beta)
		return (left + right) / 2

	def minimize(self, grid, depth, number, alpha, beta):
	
		if self.cutoffTest(grid, depth):
			return self.evaluate(grid)
		
		minUtility = sys.maxsize

		child_limit = 3
		count = 0
		for pos in grid.getAvailableCells():
			new_grid = grid.clone()
			new_grid.insertTile(pos, number)
			utility = self.maximize( new_grid, depth + 1, alpha, beta )
			minUtility = min(utility[1], minUtility)

			if minUtility <= beta or count >= child_limit:
				break
			
			#count += 1
			beta = min(minUtility, beta)
		
		return minUtility
	
	def evaluate(self, grid):
		self.exponent = math.ceil(grid.getMaxTile() / 2048)
		possible_merges = self.countPossibleMerges(grid)
		grid_value = self.calculateGridValue(grid)
		monotonicity = self.monotonicity(grid) 
		open_tiles = math.pow(len(grid.getAvailableCells()), self.exponent)
		weights = [40, 200, 270, 500]
		score = weights[0]*grid_value + weights[1]*monotonicity + weights[2]*possible_merges + weights[3]*open_tiles
		return score

	def countPossibleMerges(self, grid):
		open_cells = len(grid.getAvailableCells())
		most_merges = 0
		for move in grid.getAvailableMoves():
			next_grid = move[1]
			next_open_cells = len(next_grid.getAvailableCells())
			most_merges += open_cells - next_open_cells
		return math.pow(most_merges, self.exponent)

	def monotonicity(self, grid):
		monotonicity = 0	
		for row in range(3):
			for col in range(3):
				if grid.map[row][col] >= grid.map[row][col+1]:
					monotonicity += 1
				if grid.map[col][row] >= grid.map[col][row+1]:
					monotonicity += 1
					
		return math.pow(monotonicity, self.exponent)

	def calculateGridValue(self, grid):
		topLeft = [[128, 64, 16, 8], [32, 16, 8, 4], [16, 8, 4, 2], [8, 4, 2, 2]]
		count = 0
		for row in range(len(grid.map)):
			for col in range(len(grid.map[row])):
				count += topLeft[row][col] * grid.map[row][col]
		return math.pow(count, 2)

	def cutoffTest(self, grid, depth):
		if depth > self.maxDepth:
			return True
		return False 

	