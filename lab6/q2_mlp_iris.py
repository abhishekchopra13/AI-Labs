# Tensorflow and Keras
import tensorflow as tf

# Helper libraries
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tabulate import tabulate

class_names = {0: 'Iris setosa', 1: 'Iris versicolor', 2: 'Iris virginica'}


def evaluate_metrics(test_images, test_labels):
    # predict probabilities for test set
    predicted_probs = model.predict(test_images, verbose=0)
    # predict crisp classes for test set
    predicted_classes = tf.argmax(predicted_probs, axis=1)
    # reduce to 1d array
    predicted_probs = tf.reshape(predicted_probs, [-1])
    predicted_classes = tf.reshape(predicted_classes, [-1])

    # accuracy: (tp + tn) / (p + n)
    acc = accuracy_score(test_labels, predicted_classes)
    # precision tp / (tp + fp)
    precision = precision_score(test_labels, predicted_classes, average=None)
    # recall: tp / (tp + fn)
    recall = recall_score(test_labels, predicted_classes, average=None)
    # f1: 2 tp / (2 tp + fp + fn)
    f1 = f1_score(test_labels, predicted_classes, average=None)

    return acc, precision, recall, f1


def print_metrics(test_acc, precision, recall, f1):
    digits = [class_names[flower] for flower in range(3)]
    print(f"Accuracy of the model: {test_acc}")
    print(tabulate(zip(digits, precision, recall, f1),
                   headers=['Class (Flower)', 'Precision', 'Recall', 'F1'],
                   tablefmt='orgtbl'))


if __name__ == '__main__':
    # Load the dataset
    iris = load_iris()
    train_x, test_x, train_y, test_y = train_test_split(iris.data, iris.target, test_size=0.20)

    # Accuracies achieved with different number of neurons
    accuracy = []
    neurons = [x for x in (2 ** num for num in range(0, 10))]

    # Creating and training neural networks with different number of neurons
    for num_neurons in neurons:
        print(f"\n{'-' * 80}\nTraining on {num_neurons} neurons.")
        # Define the model
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(num_neurons, input_shape=(4,), activation='relu'),
            tf.keras.layers.Dense(num_neurons, activation='relu'),
            tf.keras.layers.Dense(3)
        ])

        # Compile the model and fit training data into the model
        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])
        model.fit(train_x, train_y, epochs=200)

        # Evaluate model and get metrics
        test_accuracy, test_precision, test_recall, test_f1 = evaluate_metrics(test_x, test_y)
        print_metrics(test_accuracy, test_precision, test_recall, test_f1)
        accuracy.append(test_accuracy)

    # Plot accuracy vs number of neurons graph
    plt.title("Accuracy vs. Number of Neurons")
    plt.xlabel("Number of Neurons")
    plt.ylabel("Accuracy")
    plt.plot(neurons, accuracy, color='red', marker='x')
    for i in range(len(accuracy)):
        plt.annotate(f'({neurons[i]}, {accuracy[i]})', (neurons[i], accuracy[i]))
    plt.savefig('iris_acc_vs_neurons.png')
    plt.show()
