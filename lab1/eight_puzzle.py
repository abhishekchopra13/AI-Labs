import sys
import utils

def readInput(input_path):
	with open(input_path) as f:
	    for line in f:
	        print(line)
	return input_path

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

	start_state = readInput(sys.argv[1])
	final_state = readInput(sys.argv[2])
