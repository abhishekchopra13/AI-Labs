import numpy as np
from copy import deepcopy

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

def up(self2: Matrix):
    self = deepcopy(self2)
    if self.blank[0] == ROW_SIZE - 1:
        return None
    else:
        self.mat[self.blank] = self.mat[self.blank[0] + 1, self.blank[1]]
        self.blank = (self.blank[0] + 1, self.blank[1])
        self.mat[self.blank] = BLANK_KEY
        return self

def down(self2: Matrix):
    self = deepcopy(self2)
    if self.blank[0] == 0:
        return None
    else:
        self.mat[self.blank] = self.mat[self.blank[0] - 1, self.blank[1]]
        self.blank = (self.blank[0] - 1, self.blank[1])
        self.mat[self.blank] = BLANK_KEY
        return self

def left(self2: Matrix):
    self = deepcopy(self2)
    if self.blank[1] == COL_SIZE - 1:
        return None
    else:
        self.mat[self.blank] = self.mat[self.blank[0], self.blank[1] + 1]
        self.blank = (self.blank[0], self.blank[1] + 1)
        self.mat[self.blank] = BLANK_KEY
        return self

def right(self2: Matrix):
    self = deepcopy(self2)
    if self.blank[1] == 0:
        return None
    else:
        self.mat[self.blank] = self.mat[self.blank[0], self.blank[1] - 1]
        self.blank = (self.blank[0], self.blank[1] - 1)
        self.mat[self.blank] = BLANK_KEY
        return self

def printMat(self):
    for i in range(0, 3):
        for j in range(0, 3):
            if self[i, j] == -1:
                print("B ", end='')
            else:
                print(f"T{self[i, j]} ", end='')
        print("")


def string_to_mat(str):
    mat = np.arange(9).reshape(3, 3)
    flag = 0
    i = 0
    while i < len(str):
        if str[i] == '-':
            mat[i//ROW_SIZE, i%COL_SIZE] = -1
            i = i + 1
            flag = 1
        else:
            if flag == 1:
                mat[(i-1)//ROW_SIZE, (i-1)%COL_SIZE] = int(str[i])
            else:
                mat[i//ROW_SIZE, i%COL_SIZE] = int(str[i])
        i = i + 1
    return mat

def mat_to_string(mat):
    return ''.join(str(val) for row in mat for val in row)
