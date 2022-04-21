'''
1) Make decision tree
2) produce data
3) split data into train and test
4) Give to IDE3 code to generate decision tree
5) Code that tests this decision tree

'''

# import numpy as np
from ID3 import ID3_method
from Data import Data
from Covidtestdata import Covidtestdata
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
    attr = ['meal', 'satiety', 'nutritional', 'enticement']
    attrvals = [['fasted', 'ate'], ['hungry', 'full'],
                ['unhealthy', 'healthy'], ['unenticing', 'tasty']]
    classif_list = ['water', 'dessert']


    allattr = ['fever', 'cough', 'breathing']
    attr = ['fever', 'cough', 'breathing']
    attrvals = [['no', 'yes'], ['no', 'yes'], ['no', 'yes']]
    classif_list = ['negative', 'positive']
    numrows = 14
    percent = 1

    # cleandataset with feat and class
    # numrows for dt_final # data is dessert data object
    data = Covidtestdata(numrows)



    # Split data into train and test sets
    trainset, testset = data.split(percent)

    # attr starts out just like allattr
    # gentree is the node that is the tree
    gen_tree = ID3_method(attr, trainset, allattr, attrvals, classif_list)

    print(gen_tree)





