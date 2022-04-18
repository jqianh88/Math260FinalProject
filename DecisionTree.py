import math
from Node import Node


class DecisionTree:
    '''
    Class Attributes
    features: question
    classes: classification (water, dessert)
    '''

    # Creating the tree
    def __init__(self, traindata):
        self.root = self._create_node(traindata)

        self.node = None  # nodes

        #self.label_classes = list(set(classes))  # unique Set of outcomes

        # Count the number of times each outcome/class appears
        #self.countlabel_classes = [list(classes).count(x) for x in
        # self.label_classes]







    # Method to test the decision tree and output its accuracy
    def test(self, testdata):
        return 0

    def classify(self, features):
        pass



    def _create_node(self, data, response=None):
        if len(data) == 0:
            return None

        no, yes = 0, 1
        feature_info = data.get_max_info(response)
        node = Node(feature_info)
        new_data = data.remove_feature(feature_info)
        node.yes = self._create_node(new_data, yes)
        node.no = self._create_node(new_data, no)



