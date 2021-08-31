import sys

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
	
	start_state = readInput(sys.argv[1])
	final_state = readInput(sys.argv[2])
