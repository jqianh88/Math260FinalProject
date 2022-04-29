

from ID3 import ID3_method
from Data import Data
from classify import classify
import csv


if __name__ == '__main__':
    base = True
    if base:
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



    print()


    extra = True
    if extra:
        print('But what about real-world data?!')
        # Removed id, url, date_fetched, price, and carat from the dataset

        # Open file
        with open('diamonds_dataset.csv', 'r') as file:

            # Create reader object by passing the file object to reader method
            reader = csv.reader(file)

            allattr = []
            attr = []

            array = []
            classif_list =[]

            # Get the first row in the csv excluding the last column
            for i, row in enumerate(reader, start=0):
                if i == 0:
                    # Obtain the attribute lists, allattr and attr:
                    # ['shape', 'cut', 'color', 'clarity', 'report', 'type']
                    allattr = row[:-1]
                    attr = row[:-1]
                else:
                    array.append(row)
                    if row[-1] not in classif_list:
                        classif_list.append(row[-1])

        num_cols = len(allattr)       # Get number of attributes
        num_rows = len(array)         # Get number of rows

        # Pre-allocate attrvals so there is not a local variable issue later
        attrvals = [[] for _ in range(num_cols)]

        # Pre-allocate temp values (attrvals and the class values)
        temp_vals = [[] for _ in range(num_cols+1)]

        # Loop through to populate temp_vals
        for i, row in enumerate(array):

            '''
            Loop through the observations in each row and append to their
            respective list in temp_vals if it is not already there
            '''
            k = num_cols
            for j, el in enumerate(row):

                # If element not already in the particular attrvals sublist
                if el not in temp_vals[j]:
                    temp_vals[j].append(el)

            # Omit the last sublist to have the attrvals list of lists
            attrvals = temp_vals[:-1]

        # Pre-allocate data with a list (num rows) of lists (attribute numbers)
        data = [[x for x in range(num_cols+1)] for y in range(num_rows)]

        '''
        Convert array into matrix full of ints by looping through the data, 
        then through each row. If the element matches the value in the 
        available values when looping through the sublist of temp_vals, assign 
        the index to that location. 
        '''
        for i, row in enumerate(array):
            for j, el in enumerate(row):
                for k, attrval in enumerate(temp_vals[j]):
                    if el == attrval:
                        data[i][j] = k

        data = Data(num_rows, data)             # turn data into a data object

        # Creating the Decision Tree for the Diamond set
        gen_tree = ID3_method(attr, data, allattr, attrvals, classif_list)

        # Printing out the Decision Tree for the Diamond set
        print('This is the Diamond Classification Decision Tree!')
        print()
        print(gen_tree)
        print()
        print('The Diamond decision tree is complete.')
        print()

        print('How accurate is the ID3 algorithm with the Diamonds?!')
        correct_count = 0  # initialize count

        # Loop through for ea line in the dataset
        for dataline in data.attr_classes:

            # Call classify func for the classification from the Decision Tree
            classification_q = classify(gen_tree, dataline, allattr, attrvals)

            """        
            If the classification from the dataset matches classification from
            the tree, then increment
            """
            if classification_q == classif_list[dataline[-1]]:
                correct_count += 1  # increment for correctly classified
        efficacy = correct_count / num_rows  # percent correct
        print(f'We have {efficacy * 100}% accuracy!')
        print('Thank you for your time! Have a great day!')






