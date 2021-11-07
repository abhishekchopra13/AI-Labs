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


print(XorPerceptron()(0, 0))
print(XorPerceptron()(0, 1))
print(XorPerceptron()(1, 0))
print(XorPerceptron()(1, 1))
