
"""
The classify method recursively gets the classification of the tree by
following each step down the tree based on the training data.
Inputs: node: a decision tree made up of nodes made from the train data.
        dataline: a row in the test data
        allattr: a list of attributes
        attrvals: a list of lists of the attribute values.

Output: The classification from the decision tree as a string.
"""


def classify(node, dataline, allattr, attrvals):

    # Base Case: return classification if it is not empty
    if node.classification != '':
        return node.classification

    """
    Get the column number in dataline whose value is equal to the attribute 
    value in the allattr list. 
    """
    column_num = get_column_num(allattr, node.attribute)

    # Get the attribute value
    attr_value = dataline[column_num]

    # Get the child node
    child_node = get_child_node(node.childlist, attr_value, attrvals)

    # Recursively call classify
    return classify(child_node, dataline, allattr, attrvals)


"""
The get_column_num method finds the index of where the attribute value (string) 
of the node is equal to the allattr list. 
Inputs: allattr, the list of attributes 
        attribute, the attribute of the node (string).
Outputs: the index as an int. 
"""


def get_column_num(allattr, attribute):

    """
    List comprehension that finds the index where the attribute of the node
    matches the allattr list.
    """
    index = [ind for ind, attr in enumerate(allattr) if attr == attribute]
    return index
'''    
Old way: 

for index, attr in enumerate(allattr):
    if attr == attribute:
        return index
'''


"""
The get_child_node method gets the child node to be classified. 
Inputs: childlist, node.childlist,
        attr_value, a 1x1 numpy array attribute value from a row in test data 
        attrvals, a list of lists of the attribute values.  
Output: A node in the tree of Node.Node type. 
"""


def get_child_node(childlist, attr_value, attrvals):

    """
    Loop through the nodes in childlist and check if the parent value in the
    tree matches the attr_value, the value in the row of the test data.
    """
    for node in childlist:

        # Convert the parent_value to an int
        temp = convert_parent_value(node.parent_value, attrvals)

        # If the parent value in the node matches the test data value
        if temp == attr_value:
            return node


"""
This method converts the string version of the parent value to an int. 
Inputs: The parent_value, he attribute value of the parent as a string. The 
list of lists holding all the values of each attribute, attrvals. 
Output: The index as an int. 
"""


def convert_parent_value(parent_value, attrvals):

    """
    Loop through attrvals (list of lists) and loop through each sublist to
    determine the index of the value in attrvals that matches the
    parent_value (the value of the parent node).
    """
    for avals in attrvals:
        for index, attr_value in enumerate(avals):
            if parent_value == attr_value:
                return index

