
'''
File contains ID3 and Calc entropy functions

attr: attributes/features, current available attributes
data: dataset from data class that has list of attributes and classes vals
allattr: list of possible values of features
attrvals: list of lists of possible values of particular feature
class_list: list of possible unique outcomes/classifications
'''

import math
from Node import Node
#import numpy as np
from Data import Data
from Covidtestdata import Covidtestdata
#from DessertData import DessertData

# Does this need to be a class?

'''
4 attributes in the dataset:
    - meal_consumption = 0  # ['Ate', 'Fasted']
    - satiety_level = 1  # ['Full', 'Hungry']
    - nutritional_value = 2  # ['Healthy', 'Unhealthy']
    - enticement_level = 3  # ['Tasty', 'Unenticing']

2 Classes:
    - Dessert: eat dessert ("dessert")
    - Water = drink water ("water")


'''

def ID3_method(attr, data, allattr, attrvals, classif_list):
    print('attr', attr)
    print('data', len(data.attr_classes))
    print('allattr', allattr)
    print('attrvals', attrvals)
    print('classif', classif_list)

    # Base Case 1:
    if attr == []:
        node = Node()       # leaf node Base case

        # loop through data and keep track of classification showed up most
        # frequently. count and store in list. put most frequent one
        count_list = [0 for x in classif_list]
        # Loop through to get the counts
        for i, (row, clasif) in enumerate(zip(data.attr_classes, classif_list)):
            if classif_list[row[-1]] == clasif:
                count_list[i] += 1
        max_count = max(count_list)  # Max count
        max_index_count = count_list.index(max_count)  # Index of the max_count

        # look at data and pick most freq occurring class
        node.classification = classif_list[max_index_count]
        return node

    # Entropy for whole data
    H = calc_entropy(data)

    # Base Case 2:
    if H == 0:
        node = Node()

        count_list = [0 for x in classif_list]
        # Loop through to get the counts
        for i, (row, clasif) in enumerate(zip(data.attr_classes, classif_list)):
            if classif_list[row[-1]] == clasif:
                count_list[i] += 1
        max_count = max(count_list)  # Max count
        max_index_count = count_list.index(max_count)  # Index of the max_count

        # look at data and pick most freq occ class
        node.classification = classif_list[max_index_count]
        return node

    '''   
   Changes: 
   need list of list for info gain 
   Want to know which feature goes with which value 
   once we know that can populate the nodes 
   array of ig
   features that they all go to 
   separate routine that tells the top 1-3 ig and which feature they belong to
   populate the yes or no (
   
   info gain for each value out of breathing, then from those values which 
   feature goes with which value. 
   
   # Think about what you need to do not how to do it
    '''

    # Make node
    node = Node()

    # List comprehension to initialize information gain of each attribute
    info_gain = [H for x in attr]

    for i, ea_attr in enumerate(attr):

        k = allattr.index(ea_attr)    # Gets corresponding attribute from allatr
        subset = []
        for j, ea_attr_val in enumerate(attrvals[k]):

            # List comprehension: keep rows that have entries matching attr_val
            # Attribute matches value looking at (i)
            subset = [sublist for sublist in data.attr_classes \
                      if attrvals[k][sublist[k]] == ea_attr_val]         #
            # problem

            subset = Data(len(subset), subset)
            # Calculate information gain of specific attribute by summing
            # across each attribute_value
            info_gain[i] -= (len(subset.attr_classes)/len(data.attr_classes))\
                            * calc_entropy(subset)

        #info_gain[i] += H     # Subtract entropy from this attr from H(S)


    max_value = max(info_gain)              # Max info gain
    max_index = info_gain.index(max_value)  # Index of the max_info gain
    node.attribute = attr[max_index]   # Name of the max info gain attribute

    k = allattr.index(node.attribute)  # Gets corresponding attribute from
    # allatr

    # remove node.attribute from attr list
    attr.remove(node.attribute)

    for j, ea_attr_val in enumerate(attrvals[k]):



        # List comprehension: keep rows that have entries matching attr_val
        # Attribute matches value looking at (k)
        subset = [sublist for sublist in data.attr_classes \
                  if attrvals[k][sublist[k]] == ea_attr_val]  # problem

        # Test section:
        #print(ea_attr_val, type(ea_attr_val))
        #print([last[-1] for last in subset], 'list')


        subset = Data(len(subset), subset)  # make subset a data object

        child_node = ID3_method(attr.copy(), subset, allattr, attrvals,
                                classif_list)       # shouldn't throw error

        child_node.parent_value = ea_attr_val      # know what node you come fr

        # append child
        node.childlist.append(child_node)
        # This is where to fix, update childlist

    return node



'''
Returns Entropy: the amount of information gain there is at each node
- entropy of a set S is the average information gain per sample, 
--> H(S) = sum -p(x)log(p(x)) 
where X are the classifications (e.g., dessert, water)
and p(x) is the proportion of set S that are classified as x
H(S) = 0 when S is perfectly classified 
'''

def calc_entropy(data): #, class_list):
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

    return entropy

