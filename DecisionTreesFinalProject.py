'''
1) Make decision tree
2) produce data
3) split data into train and test
4) Give to IDE3 code to generate decision tree
5) Code that tests this decision tree

'''

import numpy as np
from DessertData import DessertData







if __name__ == '__main__':
    # Constants
    numrows = 10
    noiselevel = 0.1
    percent = .9
    # maybe for loop

    # cleandataset with feat and class
    data = DessertData()                    # data is dessert data object

    # Expand and add noise
    data.expand(numrows)
    data.addnoise(noiselevel)

    decision = DecisionTree(data.features, data.classes)  # Decision tree
    trainset, testset = data.split(percent)     # Splitting data
    decision.train(trainset)                    # Train the set
    probability = decision.test(testset)        # Probability correct
