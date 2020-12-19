# Given current weights, get predicted value for x
# e.g. weights = [12, 2, 3] : x = 3
#  h(x) = 12 + 2x + 3x^2 = 45
def h(x, weights):
    h_x = weights[0]
    for w in range(len(weights[1:])):
        h_x += weights[w+1] * (x ** (w+1))  # w+1 as theta_0 was initial value
    return h_x


def get_updated_weight_value(data, weights, weight_index, alpha):
    m = len(data[0])
    sigma = 0
    for d in range(m):
        x = data[0][d]
        y = data[1][d]
        sigma += (h(x, weights) - y) * (x ** weight_index)
    return weights[weight_index] - (alpha * (1/m) * sigma)


# updates each weight in the weight list
def update_weights(data, weights, alpha):
    new_weights = []
    for w in range(len(weights)):
        new_weights.append(get_updated_weight_value(data, weights, w, alpha))
    return new_weights


# gradient descent
def GD(data, alpha, iterations, max_order):
    max_order += 1  # +1 for theta_0 term
    # For no particular reason, starting weights = .9, .8, .7...
    weights = [(1 - 1/i) for i in range(1, max_order+1)]
    for _ in range(iterations):
        weights = update_weights(data, weights, alpha)
    return weights


# mean-squared-error
def MSE(data, weights):
    mse = 0
    for d in range(len(data[0])):
        x = data[0][d]
        y = data[1][d]
        error = h(x, weights) - y
        mse += error**2
    return mse / len(data[0])
