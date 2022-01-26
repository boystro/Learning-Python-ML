import numpy as np
import pandas as pd


def gradient_descent(x, y):
    m = b = 0
    iterations = 10000
    n = len(x)
    learning_rate = .000210625

    for i in range(iterations):
        y_predicted = m*x +b
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n) * sum(x * (y-y_predicted))
        bd = -(2/n) * sum(y-y_predicted)
        m -= learning_rate*md
        b -= learning_rate*bd
        print("m {}, b {}, cost {}, iteration {}".format( m, b, cost, i))


df = pd.read_csv('003_GD.csv')
x = df.math
y = df.cs

gradient_descent(x, y)