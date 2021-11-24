from queue import PriorityQueue
from utils import Matrix, up, down, left, right, printMat
import heuristics
from state import Puzzle_State, Puzzle_State_HC
import math
import random
import numpy as np

def h_n(current_matrix, goal, heuristic_used: int, blank_as_tile: bool):
    if heuristic_used == 1:
        return heuristics.displaced_tiles_heuristic_with_blank_tile(current_matrix, goal, blank_as_tile)
    elif heuristic_used == 2:
        return heuristics.manhattan_heuristic_with_blank_tile(current_matrix, goal, blank_as_tile)
    elif heuristic_used == 3:
        return heuristics.sum_heuristic(current_matrix, goal, blank_as_tile)
    elif heuristic_used == 4:
        return heuristics.zero_heuristic()

def find_neighbours(puzzle_state: Puzzle_State):
    neighbours = [
        up(puzzle_state.puzzle_configuration),
        down(puzzle_state.puzzle_configuration),
        left(puzzle_state.puzzle_configuration),
        right(puzzle_state.puzzle_configuration)
    ]
    return neighbours


def hill_climbing(initial_matrix: Matrix, goal: Matrix, heuristic_used: int, blank_as_tile: bool):
    puzzle_start = Puzzle_State_HC(initial_matrix, 0, h_n(initial_matrix, goal, heuristic_used, blank_as_tile))
    open_list = PriorityQueue()
    open_list.put(puzzle_start)
    open_list_len = 1
    closed_list = {}
    parent_list = {}
    string_to_matrix_mapping = {}
    optimal_path_cost = -1
    puzzle_configuration_string = ''.join(str(val) for row in puzzle_start.puzzle_configuration.mat for val in row)
    closed_list[puzzle_configuration_string] = 0
    while open_list_len > 0:
        puzzle_state: Puzzle_State_HC = open_list.get()
        open_list_len -= 1
        puzzle_configuration_string = ''.join(str(val) for row in puzzle_state.puzzle_configuration.mat for val in row)
        if puzzle_configuration_string not in closed_list:
            closed_list[puzzle_configuration_string] = puzzle_state.g_n
        else:
            closed_list[puzzle_configuration_string] = min(closed_list[puzzle_configuration_string], puzzle_state.g_n)
        string_to_matrix_mapping[puzzle_configuration_string] = puzzle_state.puzzle_configuration.mat
        if (puzzle_state.puzzle_configuration.mat == goal.mat).all():
            optimal_path_cost = puzzle_state.g_n
            break
        neighbours = find_neighbours(puzzle_state)
        for neighbour in neighbours:
            if neighbour is None:
                continue
            neighbour_string = ''.join(str(val) for row in neighbour.mat for val in row)

            neighbour_queue = PriorityQueue()

            if neighbour_string not in closed_list:
                parent_list[neighbour_string] = puzzle_configuration_string
                closed_list[neighbour_string] = puzzle_state.g_n + 1
                neighbour_queue.put(Puzzle_State_HC(neighbour, puzzle_state.g_n + 1, h_n(neighbour, goal, heuristic_used, blank_as_tile)))
            elif puzzle_state.g_n + 1 < closed_list[neighbour_string]:
                parent_list[neighbour_string] = puzzle_configuration_string
                closed_list[neighbour_string] = puzzle_state.g_n + 1
                neighbour_queue.put(Puzzle_State_HC(neighbour, puzzle_state.g_n + 1, h_n(neighbour, goal, heuristic_used, blank_as_tile)))
            
            if neighbour_queue.empty():
                break
            best_neighbour = neighbour_queue.get()
            if best_neighbour <= puzzle_state:
                open_list.put(best_neighbour)
                open_list_len += 1
    return closed_list, parent_list, optimal_path_cost, string_to_matrix_mapping


def get_temperature(max_temperature, iteration, choice):
    if choice == 1:
        return max_temperature*(0.95**iteration)
    elif choice == 2:
        return max_temperature/iteration
    elif choice == 3:
        if iteration == 1:
            return max_temperature
        return max_temperature / math.log(iteration)


def simulated_annealing(initial_matrix: Matrix, goal, heuristic_used, max_temperature, cooling_function):
    puzzle_start = Puzzle_State(initial_matrix, 0, h_n(initial_matrix, goal, heuristic_used))
    open_list = PriorityQueue()
    open_list.put(puzzle_start)
    open_list_len = 1
    number_states_explored = 1
    parent_list = {}
    string_to_matrix_mapping = {}
    optimal_path_cost = -1
    max_iter = 5 * 10**4
    current_iter = 0
    while open_list_len > 0 and current_iter < max_iter:
        current_iter += 1
        puzzle_state: Puzzle_State = open_list.get()
        open_list_len -= 1
        puzzle_configuration_string = ''.join(str(val) for row in puzzle_state.puzzle_configuration.mat for val in row)
        string_to_matrix_mapping[puzzle_configuration_string] = puzzle_state.puzzle_configuration.mat
        current_cost = puzzle_state.h_n
        if (puzzle_state.puzzle_configuration.mat == goal.mat).all():
            optimal_path_cost = puzzle_state.g_n
            break
        node_h_n = puzzle_state.h_n
        neighbours = find_neighbours(puzzle_state)

        neighbour_chosen = None
        for neighbour in neighbours:
            if neighbour is None:
                continue
            neighbour_cost = h_n(neighbour, goal, heuristic_used)
            if neighbour_cost <= current_cost:
                neighbour_chosen = neighbour
                current_cost = neighbour_cost
        while neighbour_chosen is None:
            neighbour_chosen = random.choice(neighbours)
        neighbour_string = ''.join(str(val) for row in neighbour_chosen.mat for val in row)
        neighbour_cost = h_n(neighbour_chosen, goal, heuristic_used)
        current_temp = get_temperature(max_temperature, current_iter, cooling_function)
        if current_temp == 0:
            current_temp = 1

        if neighbour_cost < current_cost:
            probability = 1
        else:
            probability = math.e ** (-1*(neighbour_cost - current_cost) / current_temp)

        chosen = np.random.choice(
            [True, False], p=[probability, 1 - probability])
        if chosen:
            number_states_explored += 1
            open_list.put(Puzzle_State(neighbour_chosen, puzzle_state.g_n + 1, neighbour_cost))
            parent_list[neighbour_string] = puzzle_configuration_string

        else:
            open_list.put(Puzzle_State(puzzle_state.puzzle_configuration, puzzle_state.g_n, puzzle_state.h_n))
        open_list_len += 1

    return parent_list, optimal_path_cost, string_to_matrix_mapping, number_states_explored