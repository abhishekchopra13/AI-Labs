import numpy as np

BLANK_KEY = -1
ROW_SIZE = 3
COL_SIZE = 3

class Matrix:
    def __init__(self, mat = []):
        if mat == []:
            self.mat = np.arange(ROW_SIZE*COL_SIZE).reshape(ROW_SIZE, COL_SIZE)
            self.mat = self.mat + 1
            self.mat[ROW_SIZE - 1, COL_SIZE - 1] = BLANK_KEY
            self.blank = (ROW_SIZE - 1, COL_SIZE - 1)
        else:
            self.mat = mat
            for i in range (0, ROW_SIZE):
                for j in range(0, COL_SIZE):
                    if mat[i, j] == BLANK_KEY:
                        self.blank = (i, j)
                        break
            if self.blank is None:
                raise ValueError(f"No blank found in given matrix {mat}")

    def up(self):
        if self.blank[0] == ROW_SIZE - 1:
            print("No tile can be moved up.")
        else:
            self.mat[self.blank] = self.mat[self.blank[0] + 1, self.blank[1]]
            self.blank[0] = self.blank[0] + 1
            self.mat[self.blank] = BLANK_KEY

    def down(self):
        if self.blank[0] == 0:
            print("No tile can be moved down.")
        else:
            self.mat[self.blank] = self.mat[self.blank[0] - 1, self.blank[1]]
            self.blank[0] = self.blank[0] - 1
            self.mat[self.blank] = BLANK_KEY

    def left(self):
        if self.blank[1] == COL_SIZE - 1:
            print("No tile can be moved left.")
        else:
            self.mat[self.blank] = self.mat[self.blank[0], self.blank[1] + 1]
            self.blank[1] = self.blank[1] + 1
            self.mat[self.blank] = BLANK_KEY

    def right(self):
        if self.blank[1] == 0:
            print("No tile can be moved left.")
        else:
            self.mat[self.blank] = self.mat[self.blank[0], self.blank[1] - 1]
            self.blank[1] = self.blank[1] - 1
            self.mat[self.blank] = BLANK_KEY