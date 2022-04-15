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
        self.features = features            # Questions
        self.classes = classes              # Outcomes
        self.label_classes = list(set(classes))      # unique Set of outcomes

        # Count the number of times each outcome/class appears
        self.countlabel_classes = [list(classes).count(x) for x in
                                   self.label_classes]
        self.node = None       # nodes

        # Calculate the Entropy
        self.entropy = self.calc_entropy([x for x in range(len(self.classes))])


    '''
    Returns Entropy: the amount of information gain there is at each node
    - entropy of a set S is the average information gain per sample, 
    --> H(S) = sum -p(x)log(p(x)) 
    where X are the classifications (e.g., dessert, water)
    and p(x) is the proportion of set S that are classified as x
    H(S) = 0 when S is perfectly classified 
    '''

    def calc_entropy(self, features, classes):

        entropy = sum(-p(x)*math.log(p(x)))
        return entropy

    '''
    Calculates the information gain of splitting a set S based on a specific 
    features (when we create a new node in the tree)
    
    Info_gain(S,feature), = H(S) - sum p(t)H(t) where t in T are the tubsets 
    of the data created by the split, and p(t) is the proportion of the 
    number of elements in each subsset to the number of elements in set S
    S = dataframe?
    '''
    def information_gain(self, data):

        info_gain = self.calc_entropy(data)
        return info_gain



    # Method to test the decision tree and output its accuracy
    def test(self, testdata):
        return 0


    def classify(self, features):
        pass

    def _create_node(self, data, response = None):
        if len(data) == 0:
            return None

        no, yes = 0, 1
        feature_info = data.get_max_info()
        node = Node(feature_info)
        new_data = data.remove_feature(feature_info)
        node.yes = self._create_node(new_data, yes)
        node.no = self._create_node(new_data,no)


