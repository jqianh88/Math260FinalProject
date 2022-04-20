'''
1) Make decision tree
2) produce data
3) split data into train and test
4) Give to IDE3 code to generate decision tree
5) Code that tests this decision tree

'''

# import numpy as np
import ID3
from Data import Data
#from DecisionTree import DecisionTree
from Node import Node







if __name__ == '__main__':
    # Constants
    numrows = 100
    noiselevel = 0
    percent = .9
    # maybe for loop



    # Create 3 lists: by hand for now, later will get it from data
    allattr = ['meal', 'satiety', 'nutritional', 'enticement' ]
    attrvals = [['fasted', 'ate'], ['hungry', 'full'],
                ['unhealthy', 'healthy'], ['unenticing', 'tasty']]
    class_list = ['water', 'dessert']

    # cleandataset with feat and class
    # numrows for dt_final # data is dessert data object
    data = Data(numrows)

    fulldata = data.expand(numrows)
    #gen_tree = Node()

    # Split data into train and test sets
    trainset, testset = data.split(percent, numrows)
    decision = Node(trainset)           # Decision tree

    #probability = decision.test(testset)

