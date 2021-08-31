import sys
import numpy as np
from utils import ROW_SIZE, COL_SIZE, BLANK_KEY, Matrix, printMat, string_to_mat, mat_to_string
from search	import a_star
import time

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
					mat[row][col] = BLANK_KEY
					col = col + 1
			row = row + 1
			col = 0
	return mat

def printOptimalPath(parent_list: dict, current_state: str, start_state: str):
	if current_state == start_state:
		printMat(string_to_mat(current_state))
		return
	printOptimalPath(parent_list, parent_list[current_state], start_state)
	print('\n   |		')
	print('   |		')
	print('   v		')
	print('				')
	printMat(string_to_mat(current_state))
	return

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

	start_state = Matrix(np.array(readInput(sys.argv[1])))
	final_state = Matrix(np.array(readInput(sys.argv[2])))

	start_time = time.time()
	closed_list, parent_list, optimal_path_cost, string_to_matrix_mapping = a_star(start_state, final_state, hueristic_type)
	end_time = time.time()

	if optimal_path_cost != -1:
		print("Voila ! Found a solution to the puzzle ! Gretings from MnMnM !")
		print("Start State:")
		printMat(start_state.mat)
		print("Goal State:")
		printMat(final_state.mat)
		print(f"Total number of states explored: {len(closed_list)}")
		print(f"Total number of states to Optimal Path: {optimal_path_cost + 1}")
		print(f"Optimal Path Cost: {optimal_path_cost}")
		print(f"Time taken: {end_time - start_time}")
		print("")
		printOptimalPath(parent_list, mat_to_string(final_state.mat), mat_to_string(start_state.mat))
	else:
		print("Boo ! Unable to find a solution !")
		print("Start State:")
		printMat(start_state.mat)
		print("Goal State:")
		printMat(final_state.mat)
		print(f"Total number of states explored before termination: {len(closed_list)}")
