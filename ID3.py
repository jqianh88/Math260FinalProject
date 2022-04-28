'''
This file contains the ID3 and entropy methods. ID3 contains the routine
that calculates information gain.
'''

import math
from Node import Node
from Data import Data
from Covidtestdata import Covidtestdata

'''
The ID3_method recursively returns each node in the decision tree by 
calculating the information gain of the entire dataset and subtracting from 
it the sum of information gains of each attribute to find the name of the 
attribute with the largest information gain to be the next node. The child 
node and parent node's value are stored. This is performed recursively. 

Inputs: 

attr: the same list of attributes that can be altered 
data: a data object 
allattr: a list of attributes
attrvals: a list of lists of the attribute values
classif_list: a list of classifications 

Outputs: 

A node in the tree. 
'''

def ID3_method(attr, data, allattr, attrvals, classif_list):

    # Base Case 1: if the attribute list is empty
    if attr == []:
        node = Node()       # leaf node Base case

        # List comprehension to initialize a list of 0s
        count_list = [0 for x in classif_list]
        # Loop through to get the counts
        for i, (row, clasif) in enumerate(zip(data.attr_classes, classif_list)):
            if classif_list[row[-1]] == clasif:
                count_list[i] += 1
        max_count = max(count_list)  # Max count
        max_index_count = count_list.index(max_count)  # Index of the max_count

        # Pick most frequently occurring classification in the data
        node.classification = classif_list[max_index_count]

        return node

    # Entropy for the entire dataset
    H = calc_entropy(data, classif_list)

    # Base Case 2: if the entropy of the dataset is 0.
    if H == 0:

        # Create Node
        node = Node()

        # List comprehension to initialize a list of 0s
        count_list = [0 for x in classif_list]

        '''        
        Loop through the rows of data to count number of each 
        classification in the classification list
        '''
        for i, (row, clasif) in enumerate(zip(data.attr_classes, classif_list)):

            # Condition: the class from row of data matches clas_if list entry
            if classif_list[row[-1]] == clasif:
                count_list[i] += 1                  # Increment if matches
        max_count = max(count_list)                 # Class with max count
        max_index_count = count_list.index(max_count)  # Index of the max_count

        # Pick most frequently occurring classification in the data
        node.classification = classif_list[max_index_count]

        return node

    # Make node
    node = Node()

    # List comprehension to initialize info gain to entropy for each attribute
    info_gain = [H for x in attr]

    for i, ea_attr in enumerate(attr):

        # Get corresponding attribute from allatr (nonchanging list of attrs)
        k = allattr.index(ea_attr)
        subset = []
        for j, ea_attr_val in enumerate(attrvals[k]):

            '''            
            List comprehension to keep rows in the data that have the matching 
            attribute value with attrvals at the index of interest (k) 
            '''
            subset = [sublist for sublist in data.attr_classes \
                      if attrvals[k][sublist[k]] == ea_attr_val]

            # Convert subset to a data object
            subset = Data(len(subset), subset)

            '''
            Calculate information gain of specific attribute by summing
            across each attribute_value
            '''
            info_gain[i] -= (len(subset.attr_classes)/len(data.attr_classes))\
                            * calc_entropy(subset, classif_list)



    max_value = max(info_gain)              # Max info gain in the ig list
    max_index = info_gain.index(max_value)  # Index of the max_info gain
    node.attribute = attr[max_index]   # Name of the max info gain attribute

    # Get corresponding attribute from allatr (nonchanging list of attrs)
    k = allattr.index(node.attribute)

    # Remove maximum info gain attribute from attr list (changing attr list)
    attr.remove(node.attribute)

    for j, ea_attr_val in enumerate(attrvals[k]):
        '''            
        List comprehension to keep rows in the data that have the matching 
        attribute value with attrvals at the index of interest (k) 
        '''
        subset = [sublist for sublist in data.attr_classes \
                  if attrvals[k][sublist[k]] == ea_attr_val]

        # Convert subset to a data object
        subset = Data(len(subset), subset)

        # Recursion step
        child_node = ID3_method(attr.copy(), subset, allattr, attrvals,
                                classif_list)

        # Add parent value information to the child_node
        child_node.parent_value = ea_attr_val      # know what node you come fr

        # Append child
        node.childlist.append(child_node)
    return node


'''
The calc_entropy method calculates the entropy of a data object stored as a 
list of lists (rows of data). 

Inputs: 
data is the data object made up of a list of lists. 
classif_list is a list of strings composed of the possible classifications. 

Outputs: 
This method returns the entropy of the given dataset as a float using the 
formula H(S) = sum -p(x)log(p(x)), where S is the dataset p(x) is the  
proportion of a set S that are classified as x. H(S) = 0 when S is 
perfectly classified.
'''

def calc_entropy(data, classif_list):
    # Base case: If there is not data then entropy is 0, perfectly classified.
    if len(data.attr_classes) == 0:
        return 0
    tot_rows = len(data.attr_classes)  # num of rows
    entropy = 0                        # initialize

    """
    List comprehension to initialize a list of 0s for the number of 
    occurrences of each possible classification. 
    """
    class_list = [0 for x in classif_list]

    """
    Loop through & increment (count) how many times each classification occurred
    """
    for i, class_count in enumerate(class_list):
        # Loop through each row in the data
        for row in data.attr_classes:
            # Increment when it matches the index (also the value)
            if row[-1] == i:
                class_list[i] += 1
                # Increment for the

    """
    Another more obscured way:
    
    for row in data.attr_classes:
        class_list[row[-1]] += 1
    """

    # Loop through to calculate entropy for each class in the list of classes
    for clas_count in class_list:
        prop = float(clas_count/tot_rows)        # Calc the proportion

        # Base case: if the proportion is 0 then entropy is 0.
        if prop == 0:
            class_entropy = 0

        else:
            # Apply entropy formula for the class
            class_entropy = -prop * math.log2(prop)

        # Adding the class entropy to the entropy of the list/dataset
        entropy += class_entropy

    return entropy







'''def calc_entropy(data): #, class_list):   #old way
    # If no data no entropy
    if len(data.attr_classes) == 0:
        return 0
    tot_rows = len(data.attr_classes)  # num of rows
    entropy = 0  # initialize
    count_dessert = 0       # initialize  # delete
    count_water = 0            # initialize  # delete
    #count_list = [0 for x in class_list]

    # List of the number of rows that have that class value
    class_list = []

    # Loop through to get the counts
    for row in data.attr_classes:
        if row[-1] == 0:
            count_water += 1
        else:
            count_dessert += 1

    # Replace for loop above with generalized form. Which option is most freq.

    # Append counts of each classification value
    class_list.append(count_water)
    class_list.append(count_dessert)

    # Calc entropy for each class in the list of classes by looping through
    #for clas_count in count_list:
    for clas_count in class_list:
        prop = float(clas_count/tot_rows)        # proportion

        if prop == 0:
            class_entropy = 0
        else:

            # Apply entropy formula for the class
            class_entropy = -prop * math.log2(prop)

        # adding the class entropy to the entropy of the list/dataset
        entropy += class_entropy

    return entropy'''