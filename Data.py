import numpy as np

class Data:

    """
    Class attributes:

    numrows: the number of rows in the data
    attr_classes: the combination of the attributes and the corresponding
    classification, where the classification is the last element in the list.
    """

    # Creates the data object
    def __init__(self, numrows, attr_classes=None): #, random = True
        self.attr_classes = []
        if attr_classes is None:
            self.attr_classes = self.unique_combos()  # generate all combos
            self.attr_classes = self.expand(numrows)  # expand
        else:
            self.attr_classes = attr_classes

    # This method makes the unique rows corresponding to the self-made tree.
    def unique_combos(self):

        # Assign 0 or 1 to the attribute value if no or yes, respectively.
        ate, full, healthy, tasty, dessert = 1, 1, 1, 1, 1
        fasted, hungry, unhealthy, unenticing, water = 0, 0, 0, 0, 0

        data = [[ate, full, healthy, tasty, dessert],
                [ate, full, healthy, unenticing, dessert],
                [ate, full, unhealthy, tasty, dessert],
                [ate, full, unhealthy, unenticing, water],
                [ate, hungry, healthy, tasty, dessert],
                [ate, hungry, healthy, unenticing, dessert],
                [ate, hungry, unhealthy, tasty, water],
                [ate, hungry, unhealthy, unenticing, water],
                [fasted, full, healthy, tasty, water],
                [fasted, full, healthy, unenticing, water],
                [fasted, full, unhealthy, tasty, water],
                [fasted, full, unhealthy, unenticing, water],
                [fasted, hungry, healthy, tasty, dessert],
                [fasted, hungry, healthy, unenticing, dessert],
                [fasted, hungry, unhealthy, tasty, dessert],
                [fasted, hungry, unhealthy, unenticing, dessert]]

        return np.array(data)

    """   
    The expand method expands the perfect Data by random sampling the perfect
    dataset to make a dataset of numrows length. 
    Inputs: self, the data object
            numrows, the total number of rows as an int. 
    Output: expanded, a data object. 
    """
    def expand(self, numrows):   # , random)
        np.random.seed(0)
        sampleInd = np.random.choice(
            self.attr_classes.shape[0], numrows, replace = numrows > 16)

        expanded = self.attr_classes[sampleInd]

        return expanded

    """
    The split method to creates two Data objects by splitting one data object. 
    Inputs: percent, a float. 
            numrows, an int. 
    Outputs: Two data objects, one for training and the other for testing. 
    """

    def split(self, percent, numrows):
        trainnumrows = int(percent * numrows)          # make it an int
        train_data = self.attr_classes[:trainnumrows]  # all rows up to 90%
        test_data = self.attr_classes[trainnumrows:]   # last 10%
        return Data(len(train_data), train_data), \
               Data(len(test_data), test_data)













