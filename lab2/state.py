from utils import Matrix

class Puzzle_State:
    def __init__(self, puzzle_configuration: Matrix, g_n, h_n):
        self.puzzle_configuration = puzzle_configuration
        self.g_n = g_n
        self.h_n = h_n

    def __lt__(self, other):
        if (self.g_n + self.h_n) == (other.g_n + other.h_n):
            return self.g_n < other.g_n
        return (self.g_n + self.h_n) < (other.g_n + other.h_n)

class Puzzle_State_BFS:
    def __init__(self, puzzle_configuration: Matrix, g_n, h_n):
        self.puzzle_configuration = puzzle_configuration
        self.g_n = g_n
        self.h_n = h_n

    def __lt__(self, other):
        if self.h_n == other.h_n:
            return self.g_n < other.g_n
        return self.h_n < other.h_n