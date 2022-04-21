
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
    # Base Case 1:
    if attr == []:
        node = Node()       # leaf node Base case

        # loop through data and keep track of classification showed up most
        # frequently. count and store in list. put most frequent one
        node.classification = '' # look at data and pick most freq occ class
        return node

    # Entropy for whole data
    H = calc_entropy(data)

    # Base Case 2:
    if H == 0:
        node = Node()

        # same loop as above to get most frequent
        node.classification = ''
        return node

    '''   
    # Base Case 2: Original
    # Loop through data, if all class is the same then same as above
    if all(x == data.classes[0] for x in data.classes) \
            or len(data.classes) == 1:
        node = Node()  # leaf node Base case

        # look at data and pick most freq occ class
        node.classification = data.classes[0]

        return node
    '''

    # Make node
    node = Node()

    # List comprehension to initialize information gain of each attribute
    info_gain = [H for x in attr]

    for i, ea_attr in enumerate(attr):
        print(i, ea_attr, 'i, attr')
        k = allattr.index(ea_attr)    # Gets corresponding attribute from allatr
        for j, ea_attr_val in enumerate(attrvals[k]):
            print(j, ea_attr_val, 'j, eaattr')
            # List comprehension: keep rows that have entries matching attr_val
            # Attribute matches value looking at (i)
            subset = [sublist for sublist in data.attr_classes \
                      if sublist[k] == ea_attr_val]         # problem

            print(subset, 'subset')
            subset = Covidtestdata(len(subset), subset)
            # Calculate information gain of specific attribute by summing
            # across each attribute_value
            info_gain[i] -= (len(subset.attr_classes)/len(data.attr_classes))\
                            * calc_entropy(subset)

        #info_gain[i] += H     # Subtract entropy from this attr from H(S)

    print(info_gain, 'ig')

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
                  if sublist[k] == ea_attr_val]  # problem

        subset = Covidtestdata(len(subset), subset)  # make subset a data object

        child_node = ID3_method(attr.copy(), subset, allattr, attrvals,
                                classif_list)       # shouldn't throw error

        child_node.parent_value = ea_attr_val      # know what node you come fr
        # append child
        node.childlist.append(child_node)

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

        # Apply entropy formula for the class
        class_entropy = -prop * math.log2(clas_count / tot_rows)

        # adding the class entropy to the entropy of the list/dataset
        entropy += class_entropy

    return entropy

