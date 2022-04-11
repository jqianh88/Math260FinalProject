'''
1) Make decision tree
2) produce data
3) split data into train and test
4) Give to IDE3 code to generate decision tree
5) Code that tests this decision tree


'''

import numpy as np

from sklearn.datasets import make_regression, make_classification, make_blobs
import pandas as pd
import matplotlib.pyplot as plt


#5 desserts: ice cream, smoothie, milkshake, cake, cupcake cone
# How to create a dataset for a classification problem
variables, target  = make_classification(
                    n_samples = 1000,
                    n_features = 3,
                    n_informative = 7,
                    n_redundant = 3,
                    n_repeated = 2,
                    n_classes = 4,
                    # Distribution of classes 20% Output1
                    # 20%> output 2, 30% output 3 and 4
                    weights = [.3,.25, .25, .1, .1],
                    random_state = 8)

# Features: what is the dessert, What is it held in, is it frozen, made out of
# fruit

# informative features: 3 What is it held in, is it frozen, made out of fruit

# number of rdundant and clsses = 0
# Weights: The proportion of samples for each output/class = [







if __name__ == '__main__':
    pass