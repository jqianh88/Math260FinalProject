class DessertData:
    '''
    Class attributes:



    '''

    def __init__(self, features = None, classes = None):
        if features is None:
            self.features = [[]]
        else:
            self.features = features      # numrows needs to match len classes

        if classes is None:
            self.classes = []
        else:
            self.classes = classes      # 6 classes

    def expand(self, numrows):
        pass


    def addnoise(self, noiselevel):
        pass


    def split(self, percent):


        return DessertData(self.features, self.classes), DessertData(
            self.features, self.classes)