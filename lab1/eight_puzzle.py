import sys
import utils
import numpy as np

ROW_SIZE = 3
COL_SIZE = 3

def readInput(input_path):
	mat = np.arange(ROW_SIZE*COL_SIZE).reshape(ROW_SIZE, COL_SIZE)
	with open(input_path) as f:
		row, col = (0, 0)
		for line in f:
			for i in range(0, len(line)):
				if line[i] == 'T':
					mat[row][col] = int(line[i + 1])
					col = col + 1
				if line[i] == 'B':
					mat[row][col] = -1
					col = col + 1
			row = row + 1
			col = 0
	return mat

if __name__ == '__main__':
	# Handling incorrect command line arguments
	if len(sys.argv) != 3:
		print('Error: Incorrect command line arguments.')
		print('Run: eight_puzzle.py <path_to_initial_state> <path_to_final_state>')
		exit(0)
	
	# Ask for Hueristic type
	print('Enter Hueristic type:')
	print('1. h1(n) = number of tiles displaced from their destined position.')
	print('2. h2(n) = sum of Manhattan distance of each tile from the goal')
	print('3. h(n) = g(n) Best First Search')
	hueristic_type = int(input())

	start_state = utils.Matrix(readInput(sys.argv[1]))
	final_state = utils.Matrix(readInput(sys.argv[2]))
