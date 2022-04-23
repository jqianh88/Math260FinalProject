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
from classify import classify
from Covidtestdata import Covidtestdata
#from DecisionTree import DecisionTree
from Node import Node



'''
outline 
- 


'''



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


    #allattr = ['fever', 'cough', 'breathing']
    #attr = ['fever', 'cough', 'breathing']
    #attrvals = [['nofever', 'fever'], ['nocough', 'cough'], ['nobreath',
    #                                                         'breathing']]
    #classif_list = ['negative', 'positive']
    #attrvals = [[0,1], [0,1], [0,1]]
    #classif_list = [0,1]

    #numrows = 14
    #percent = 1
    # make them strings, and make them strings in the data
    # get print working

    # Need to match up list to list tie in or dictionary
    # list of dictionaries, or list of tuples (use tuples), 1 entry dictionary
    # Tuple = (key, value)
    # whenever you create/update --> each child contains the feature and the
    # feature value corresponding to that choice , each child is now a tuple
    # of the feature and feature value (link between those two nodes (the list)


    # cleandataset with feat and class
    # numrows for dt_final # data is dessert data object
    data = Data(numrows)




    # Split data into train and test sets
    trainset, testset = data.split(percent, numrows)


    # attr starts out just like allattr
    # gentree is the node that is the tree
    gen_tree = ID3_method(attr, trainset, allattr, attrvals, classif_list)
    temp = gen_tree.parent_value
    print(temp, 'sep')
    print(gen_tree, 'final')




    correct_count = 0       # initialize count

    # Loop through the entire test data set for each row to determine if
    # correctly classified
    for dataline in testset:
        classification_q = classify(gen_tree, dataline)     # Call classify func

        # If the test data classification and the training data created tree
        # classification match
        if classification_q == classif_list[dataline[[-1]]]:
            correct_count += 1                      # increment for correctly
            # classified
    efficacy = correct_count/len(testset)           # percent correct
    print(efficacy)





