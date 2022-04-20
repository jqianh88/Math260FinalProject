
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
        self.root = ID3_method(attribute, data, allattr, attrvals,
                              classification)

    # for printing
    def __repr__(self):
        S = print(self.root.Node())

    def printNode(self, current_Node, level_current_node):
        if current_Node is leaf:
            S += level_current_node * '\t' + current_Node.parent_value + '\n'
            S +=(level_current_node+1) * '\t' + current_Node.classification +\
            '\n'
            return S
        if not leaf:
            S += level_current_node * '\t' + current_Node.parent_value + '\n'
            S +=(level_current_node+1) * '\t' + current_Node.split_attribute +\
            '\n'
            return S

        for child in current_Node.childlist:
            S += print_Node(child, level +  2)

        return S


    def test_print(self):
        self.root = Node()
        self.root.attr = 'ate_meal'
        child1 = self.parent_value = 'hungry'
        self.root.append(child1)

        # Create and link properly
