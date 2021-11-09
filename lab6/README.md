### CS561
### Artificial Intelligence Lab
### Indian Institute of Technology Patna
### 2021-22

# Assignment 6

## Team Details:

Team Code: `1801cs03_1801cs07_1801cs46`

Team Name: `MnMnM`

Team Members:

| Name              | Roll Number |
| ----------------- | ----------- |
| Abhishek Chopra   | 1801CS03    |
| Amish Mittal      | 1801CS07    |
| Shashwat Mahajan  | 1801CS46    |

## Question 1: XOR Neural Network

### Running the Code
```python q1_xor_nn.py```

### Sample Output
```
Finding A XOR B using neural network.
CASE 1: A = 0, B = 0
A XOR B = 0

CASE 2: A = 0, B = 1
A XOR B = 1

CASE 3: A = 1, B = 0
A XOR B = 1

CASE 4: A = 1, B = 1
A XOR B = 0

```

## Question 2: Part 1: IRIS Classifier
### Training the model
```python q2_mlp_iris.py```

### Error Analysis for 512 neurons
**Accuracy of the model: 0.9666666666666667**

| Class (Flower)   |   Precision |   Recall |       F1 |
|------------------|-------------|----------|----------|
| Iris setosa      |    1        | 1        | 1        |
| Iris versicolor  |    1        | 0.909091 | 0.952381 |
| Iris virginica   |    0.909091 | 1        | 0.952381 |


### Accuracy vs. Number of Neurons Graph
![alt text](./iris_acc_vs_neurons.png?raw=true "IRIS")

## Question 2: Part 2: MNIST Classifier
### Training the model
```python q2_mlp_mnist.py```

### Error Analysis for 512 neurons
**Accuracy of the model: 0.9805**

|   Class (Digit) |   Precision |   Recall |       F1 |
|-----------------|-------------|----------|----------|
|               0 |    0.98778  | 0.989796 | 0.988787 |
|               1 |    0.978374 | 0.996476 | 0.987342 |
|               2 |    0.98912  | 0.968992 | 0.978953 |
|               3 |    0.958773 | 0.990099 | 0.974184 |
|               4 |    0.987616 | 0.974542 | 0.981035 |
|               5 |    0.989667 | 0.966368 | 0.977879 |
|               6 |    0.985417 | 0.987474 | 0.986444 |
|               7 |    0.989087 | 0.969844 | 0.979371 |
|               8 |    0.969543 | 0.980493 | 0.974987 |
|               9 |    0.972414 | 0.978196 | 0.975296 |

### Accuracy vs. Number of Neurons Graph
![alt text](./mnist_acc_vs_neurons.png?raw=true "MNIST")

______________________
Thanking You!

MnMnM


















