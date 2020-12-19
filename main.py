from csvread import read_syn
from gdmath import GD, MSE
from visualize import plot_scatter


def main():

    alpha = .0001
    iterations = 10000

    for file in (1, 2, 3):  # synthetic-1.csv, synthetic-2...
        data = read_syn(file)
        mse_list = []
        for order in (1, 2, 4, 7):  # do GD for 1st, 2nd,... order equations
            weights = GD(data, alpha, iterations, order)
            mse = MSE(data, weights)
            mse_list.append(round(mse, 4))
            print("\n===================\n")
            print(" FILE:          ", file)
            print(" EQ ORDER:      ", order)
            print(" FINAL WEIGHTS: ", [round(w, 4) for w in weights])
            print(" MEAN-SQ-ERROR: ", round(mse, 4))
            print(" Close plot to continue.")
            plot_scatter(data, weights)
        print("\n===================\n")
        print("synthetic-", file, " - ", sep='', end='')
        print("Polynomial 1 - ", mse_list[0], " MSE, ", sep='', end='')
        print("Polynomial 2 - ", mse_list[1], " MSE, ", sep='', end='')
        print("Polynomial 4 - ", mse_list[2], " MSE, ", sep='', end='')
        print("Polynomial 7 - ", mse_list[3], " MSE", sep='', end='\n')
        print("\n===================\n")


main()
