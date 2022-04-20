
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
#from Data import Data
#from DessertData import DessertData

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
        node.classification = '' # look at data and pick most freq occ class
        return node

    # Base Case 2:
    if calc_entropy(data) == 0:
        node = Node()
        node.classification = ''
        return node

    # Base Case 2: Original
    # Loop through data, if all class is the same then same as above
    if all(x == data.classes[0] for x in
           data.classes) or len(data.classes) == 1:
        node = Node()  # leaf node Base case

        # look at data and pick most freq occ class
        node.classification = data.classes[0]

        return node

    # Make node
    node = Node()

    # Entropy for whole data
    H = calc_entropy(data)

    # List comprehension to initialize information gain of each attribute
    info_gain = [0.0 for x in attr]

    for i, ea_attr in enumerate(attr):
        for j, ea_attr_val in enumerate(attrvals[i]):

            # List comprehension: keep rows that have entries matching attr_val
            subset = [sublist for sublist in data if sublist[j] == ea_attr_val]

            # Calculate information gain of specific attribute by summing
            # across each attribute_value
            info_gain[i] -= (len(subset)/len(data))*calc_entropy(subset)

        info_gain[i] += H     # Subtract entropy from this attr from H(S)

    max_value = max(info_gain)              # Max info gain
    max_index = info_gain.index(max_value)  # Index of the max_info gain
    node.attribute = allattr[max_index]   # Name of the max info gain attribute

    for i, ea_attr_val in enumerate(attrvals[max_index]):

        # List comprehension: keep rows that have entries matching attr_val
        subset = [sublist for sublist in data if sublist[i] == ea_attr_val]

        # Recursive step to get subsequent nodes
        child_node = ID3_method(attr.remove(allattr[max_index]), subset,
                                allattr,
                         attrvals, classif_list)


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

def calc_entropy(data):

    tot_rows = len(data)  # num of rows
    entropy = 0  # initialize
    count_dessert = 0       # initialize
    count_water = 0            # initialize

    # List of the number of rows that have that class value
    class_list = []

    # Loop through to get the counts
    for row in data:
        if row[-1] == 0:
            count_water+=1
        else:
            count_dessert +=1

    # Append counts of each classification value
    class_list.append(count_water)
    class_list.append(count_dessert)

    # Calc entropy for each class in the list of classes by looping through
    for clas_count in class_list:
        prop = float(clas_count/tot_rows)        # proportion

        # Apply entropy formula for the class
        class_entropy = -prop * math.log2(clas_count / tot_rows)

        # adding the class entropy to the entropy of the list/dataset
        entropy += class_entropy


    return entropy

