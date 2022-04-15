class Node:

    '''
    Class attributes:
    question: the node asks a question
    Will answer yes or no
    '''

    def __init__(self, question = None):
        self.yes = None
        self.no = None
        if question is None:
            self.question = ""
        self.question = question