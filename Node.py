class Node:

    def __init__(self, question = None):
        self.yes = None
        self.no = None
        if question is None:
            self.question = ""
        self.question = question