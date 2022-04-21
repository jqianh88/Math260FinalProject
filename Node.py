
class Node:

    '''
    Class attributes:
    Creates empty node and overwrites
    '''

    def __init__(self, attribute = '', parent_value = '', childlist = [],
                 classification = ''):
        self.attribute = ''
        self.parent_value = ''
        self.childlist = []
        self.classification = ''


    # for printing
    def __repr__(self):
        S = printNode(self, 0)

        return S


def printNode(current_Node, level_current_node):
    S = ''
    if current_Node.classification != '':
        S += level_current_node * '\t' + current_Node.parent_value + '\n'
        S +=(level_current_node+1) * '\t' + current_Node.classification + '\n'
        return S
    else:
        S += level_current_node * '\t' + current_Node.parent_value + '\n'
        S += (level_current_node+1) * '\t' + current_Node.attribute + '\n'

        for child in current_Node.childlist:
            S += printNode(child, level_current_node + 2)
        return S






