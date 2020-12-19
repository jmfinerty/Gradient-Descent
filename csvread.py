# reads synthetic data file "synthetic-[number].csv"
# returns array where last row is y, first row is x
def read_syn(number):
    return read_csv("synthetic-" + str(number) + ".csv")


# reads data from a specific csv file
# assumes col 1 = x, col 2 = y
# returns array where last row is y list, first row is x list
def read_csv(filename):
    f = open(filename)
    x, y = [], []
    for line in f.readlines():
        x.append(float(line.split(",")[0].rstrip()))
        y.append(float(line.split(",")[1].rstrip()))
    return [x, y]
