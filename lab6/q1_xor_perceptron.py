class XorPerceptron:
    __w1 = 1
    __w2 = 1

    # Input Layer
    def __input(self, a, b):
        return self.__w1 * a, self.__w2 * b

    # Output Layer
    def __output(self, inputs):
        return inputs[0] + inputs[1]

    # Activation Layer
    def __activation(self, output):
        return output % 2

    # Defining call method
    def __call__(self, a, b):
        return self.__activation(self.__output(self.__input(a, b)))


print("Finding A XOR B using perceptron.")
print(f'CASE 1: A = 0, B = 0\nA XOR B = {XorPerceptron()(0, 0)}\n')
print(f'CASE 2: A = 0, B = 1\nA XOR B = {XorPerceptron()(0, 1)}\n')
print(f'CASE 3: A = 1, B = 0\nA XOR B = {XorPerceptron()(1, 0)}\n')
print(f'CASE 4: A = 1, B = 1\nA XOR B = {XorPerceptron()(1, 1)}\n')
