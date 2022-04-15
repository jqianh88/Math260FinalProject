'''
1) Make decision tree
2) produce data
3) split data into train and test
4) Give to IDE3 code to generate decision tree
5) Code that tests this decision tree

'''

# import numpy as np
from DessertData import DessertData
from DecisionTree import DecisionTree







if __name__ == '__main__':
    # Constants
    numrows = 20
    noiselevel = 0
    percent = .9
    # maybe for loop

    # cleandataset with feat and class
    data = DessertData(numrows)                    # data is dessert data object

    #Add noise
    data.addnoise(noiselevel)

    trainset, testset = data.split(percent)     # Splitting data
    decision = DecisionTree(trainset)           # Decision tree

    probability = decision.test(testset)

    # make sure I can push to git