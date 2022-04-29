

from ID3 import ID3_method
from Data import Data
from classify import classify


if __name__ == '__main__':
    # Constants
    numrows = 10000
    noiselevel = 0
    percent = .9

    # Create 4 lists: by hand for now, later will get it from data

    allattr = ['meal', 'satiety', 'nutritional', 'enticement']

    # attr starts out starts as allattr, but can be altered
    attr = ['meal', 'satiety', 'nutritional', 'enticement']

    # attrvals are the possible values of each attribute in allattr or attr
    attrvals = [['fasted', 'ate'], ['hungry', 'full'],
                ['unhealthy', 'healthy'], ['unenticing', 'tasty']]

    # classif_list are the possible classifications or outcomes
    classif_list = ['water', 'dessert']

    # Data Object
    data = Data(numrows)                # numrows, random = T or F

    # Split data into train and test sets
    trainset, testset = data.split(percent, numrows)

    # Creating the Decision Tree
    gen_tree = ID3_method(attr, trainset, allattr, attrvals, classif_list)

    # Printing out the Decision Tree
    print('Thank you for your interest in the Food Choice Decision Tree!')
    print()
    print(gen_tree)
    print()
    print('The decision tree is complete.')
    print()

    print('Now we look at the accuracy of the ID3 algorithm!')
    correct_count = 0       # initialize count
    for dataline in testset.attr_classes:

        # Call classify func
        classification_q = classify(gen_tree, dataline, allattr, attrvals)

        """        
        If the test data classification and the training data 
        classification from the tree are equal then increment 
        """
        if classification_q == classif_list[dataline[-1]]:
            correct_count += 1            # increment for correctly classified
    efficacy = correct_count/len(testset.attr_classes)        # percent correct
    print(f'We have {efficacy*100}% accuracy!')
    print()

    # Begin purposeful display of not perfect classification
    print('What if we purposefully flip one classification in the test data \n'
          'so that it does not follow the tree?')
    correct_count = 0         # Initialize the number of correct classifications

    """
    Change a single classification in a row of the test data so it doesn't 
    follow the logic of the tree.
    """
    testset.attr_classes[0][4] = 0

    """
    Loop through the entire test data set for each row to determine if
    correctly classified
    """
    for dataline in testset.attr_classes:

        # Call classify function
        classification_q = classify(gen_tree, dataline, allattr, attrvals)

        """        
        If the test data classification and the training data 
        classification from the tree are equal then increment 
        """
        if classification_q == classif_list[dataline[-1]]:
            correct_count += 1              # increment for correctly classified
    efficacy = correct_count/len(testset.attr_classes)        # percent correct
    print(f' We get {efficacy * 100}% accuracy, as expected!')





