'''
File contains ID3 and Calc entropy functions

attr: attributes/features
data: dataset
allattr: list of possible values of features
attrvals: list of lists of possible values of particular feature
class_list: list of possible unique outcomes/classifications
'''

import math
from Node import Node


def ID3(attr, data, allattr, attrvals, class_list):
    if attr == []:
        node = Node()       # leaf node Base case
        node.classification = '' # look at data and pick most freq occ class
        return node

    # Loop through data, if all class is the same then same as above
    for row in data:
        classification = []
        if all(x == classification[0] for x in classification):
            node = Node()  # leaf node Base case
            node.classification = ''  # look at data and pick most freq occ class
            return node

    H = calc_entropy(data)

    # List comprehension to initialize information gain of each attribute
    info_gain = [0.0 for x in allattr]

    # Loop through all attributes that are possible after splitting on node
    # Need to fix
    for i, (ea_attr, row) in enumerate(zip(attr, data)):
        subset =[]
        for j, (ea_val, row) in enumerate(zip(attrvals)):
            # need to change this: ex if value == sunny --> subset this
            if ea_val == attrvals[j]:
                subset.extend()                #data for that value
        info_gain[i] += calc_entropy(data)      # increment entropy of full data

    [ob for ob in data if ob[attr_num] == value] = subset
    node.attribute = allattr[chosen_attr]

    for ea_val in attr:
        subset = []
        attr = attr.remove(chosen_attr)
        child_node = ID3(attr, subset, allattr, attrvals)
        current_node = node.children.append(child_node)










'''
Returns Entropy: the amount of information gain there is at each node
- entropy of a set S is the average information gain per sample, 
--> H(S) = sum -p(x)log(p(x)) 
where X are the classifications (e.g., dessert, water)
and p(x) is the proportion of set S that are classified as x
H(S) = 0 when S is perfectly classified 
'''

def calc_entropy(data):

    tot_rows = len(data)  # num of rows, based on classes list or all data
    entropy = 0  # initialize
    count_dessert = 0
    count_water = 0

    # List of the number of rows that have that class value
    class_list = []

    # For loop that goes through the list or data to found the # of rows
    for i, val in enumerate(data):

        if data[i] == 0:            # for water
            count_water += 1
        if data[i] == 1:            # for dessert
            count_dessert += 1
    class_list.append(count_water)
    class_list.append(count_dessert)
    # Calc entropy for each class in the list of classes
    for clas in class_list:
        prop = float(clas/tot_rows)        # proportion
        # Apply entropy formula for the class
        class_entropy = -prop * math.log2(clas / tot_rows)

        # adding the class entropy to the entropy of the list/dataset
        entropy += class_entropy


    return entropy

