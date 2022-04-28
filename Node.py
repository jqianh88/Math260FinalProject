# This file creates the Node class (a new node) and includes a printing method.

class Node:

    """
    Class attributes:
    attribute: The string node name or "attribute".
    parent_value: The string value associated with the "parent" node.
    childlist: The list of child nodes and their associated parent values.
    classification: The classification (the outcome).
    """

    def __init__(self, attribute = '', parent_value = '', childlist = [],
                 classification = ''):
        self.attribute = ''                 # question
        self.parent_value = ''              # Answer to the question
        self.childlist = []                 # List of child nodes
        self.classification = ''            # leaf node



    def __repr__(self):
        S = printNode(self, 0)

        return S

# Method to print the Tree of nodes
def printNode(current_Node, level_current_node):
    S = ''
    if current_Node.classification != '':
        S += level_current_node * '\t' + str(current_Node.parent_value) + '\n'
        S +=(level_current_node+1) * '\t' + str(current_Node.classification) + \
            '\n'
        return S
    else:
        # if the parent value is empty
        if current_Node.parent_value == '':
            S += level_current_node * '\t' + 'root' + '\n'
        else:
            S += level_current_node * '\t' + str(current_Node.parent_value) + '\n'
        S += (level_current_node+1) * '\t' + str(current_Node.attribute) + '\n'

        for child in current_Node.childlist:
            S += printNode(child, level_current_node + 2)
        return S






