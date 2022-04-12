class DessertData:
    '''
    Class attributes:



    '''
    # Constants
    CAKE = 1
    ICECREAM = 2
    SMOOTHIE = 3
    MILKSHAKE = 4
    CUPCAKECONE = 5

# make all the combinations
    # vessel, frozen, fruit,

    # Build big matrix of stuff , 1:n-1 = features, Last column (Classes),
    # create constants: cup, plate, cone,--> 0, 1, 2 or 1, 2, 3
    # fruit --> 0, 1

    def __init__(self, features = None, classes = None):
        if features is None:
            self.features = [[]]
        else:
            self.features = features      # numrows needs to match len classes

        if classes is None:
            self.classes = [DessertData.CAKE, DessertData.ICECREAM]
        else:
            self.classes = classes      # 6 classes




    def expand(self, numrows):
        pass


    def addnoise(self, noiselevel):
        pass


    def split(self, percent):


        return DessertData(self.features, self.classes), DessertData(
            self.features, self.classes)