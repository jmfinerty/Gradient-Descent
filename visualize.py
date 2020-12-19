import matplotlib.pyplot as plt
import numpy as np
from csvread import read_syn, read_csv
from gdmath import h


# draws a simple scatter plot of given data
# plots hypothesis, if given
def plot_scatter(data, weights=None):
    x, y = data[0], data[1]
    plt.scatter(x, y, color="black", s=4)  # plot points
    plt.axvline(x=0, color="gray")  # plot axes
    plt.axhline(y=0, color="gray")
    plt.xlabel("X")  # label axes
    plt.ylabel("Y")
    plt.grid(True, color="lightgray", linestyle="--")  # draw gridlines

    if weights:
        predictions = np.linspace(min(x), max(x))
        plt.plot(predictions, h(predictions, weights), color="red")

    plt.show()  # show popup graph


# The functions below are not used, but were used
# at the beginning of work on this assignment
# before the gradient-descent process was implemented.
# They have been left in largely for debugging and testing purposes.


# draws a simple scatter plot of data in a specific synthetic data file
def plot_scatter_syn(number):
    data = read_syn(number)
    plot_scatter(data)


# draws a simple scatter plot of data in a specific csv file
def plot_scatter_csv(filename):
    data = read_csv(filename)
    plot_scatter(data)
