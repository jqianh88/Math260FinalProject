# import random
import numpy as np


# import pandas as pd


class DessertData:
    '''
    Class attributes:
    features: The combination of nodes or questions of the hand drawn decision
              tree stored as a list of lists.
    classes: The dessert stored as a list.


    '''
    # Dessert Classes - Constants
    Dessert = 0
    Water = 1

    # Dessert Features - Constants
    meal_consumption = 0  # ['Ate', 'Fasted']
    satiety_level = 1  # ['Full', 'Hungry']
    nutritional_value = 2  # ['Healthy', 'Unhealthy']
    enticement_level = 3  # ['Tasty', 'Unenticing']

    yes = 1
    no = 0

    '''
    Perfect
    Expand/contract 
    Noise
    '''

    def __init__(self, numrows, features=None, classes=None):
        if features is None:
            all_combinations = self.unique_combos()  # generate all combos
            self.features = self.expand(all_combinations, numrows)  # expand
        else:
            self.features = features  # numrows needs to match len classes

        if classes is None:
            answer = self.choice_answer()  # resulting class
            self.classes = answer
        else:
            self.classes = classes  # 3 classes

    # method to get answer
    def choice_answer(self):
        Dessert = 1
        Water = 0
        no, yes = 0, 1
        classes = [0. for _ in self.features]
        for i, observation in enumerate(self.features):
            [meal, satiety, nutritional, enticement] = observation
            if meal == yes and satiety == yes and nutritional == yes:
                classes[i] = Dessert
            elif meal == yes and satiety == no and enticement == yes:
                classes[i] = Dessert
            elif meal == no and satiety == yes and \
                    nutritional == yes:
                classes[i] = Dessert
            elif meal == no and satiety == yes and \
                    nutritional == no:
                classes[i] = Dessert
            else:
                classes[i] = Water
        return classes

    # Method for unique combinations
    def unique_combos(self):
        ate, full, healthy, tasty = 1, 1, 1, 1
        fasted, hungry, unhealthy, unenticing = 0, 0, 0, 0

        rows = [[ate, full, healthy, tasty],
                [ate, full, healthy, unenticing],
                [ate, full, unhealthy, tasty],
                [ate, full, unhealthy, unenticing],
                [ate, hungry, healthy, tasty],
                [ate, hungry, healthy, unenticing],
                [ate, hungry, unhealthy, tasty],
                [ate, hungry, unhealthy, unenticing],
                [fasted, full, healthy, tasty],
                [fasted, full, healthy, unenticing],
                [fasted, full, unhealthy, tasty],
                [fasted, full, unhealthy, unenticing],
                [fasted, hungry, healthy, tasty],
                [fasted, hungry, healthy, unenticing],
                [fasted, hungry, unhealthy, tasty],
                [fasted, hungry, unhealthy, unenticing]]

        return np.array(rows)

    # Method to expand the perfect DessertData
    def expand(self, all_combinations, numrows):
        sampleInd = np.random.choice(all_combinations.shape[0], numrows,
                                     replace=numrows > 16)
        expanded = all_combinations[sampleInd]
        return expanded

    # Method to add noise to the clean DessertData
    def addnoise(self, noiselevel):
        pass

    # Method to create two DessertData objects from one DessertData Object
    def split(self, percent):

        return DessertData(self.features, self.classes), DessertData(
            self.features, self.classes)

    '''
    Starting Strategy to make the Data 


    num_observations = 100
    # Space allocation: filled with '_' for list of list to flip
    observations = [['_']*4 for _ in range(num_observations)]
    classes = ['_' for _ in range(num_observations)]


    # For loop to populate 100 observations
    for i, observation in enumerate(observations):
        for j, feature in enumerate(observation):
            if random.random() >= 0.5:
                observation[j] = "yes"

            else:
                observation[j] = "no"


    '''
    '''
    For loop to fix the tree so that if the 3rd question is healthy then tasty 
    is ? which means location 2 (starting from 0) is flipped and [3] = '?'
    If the 3rd question is tasty then healthy aka [2]= '?' 
    '''

    '''
    for i, observation in enumerate(observations):
        if observation[0] == "yes" and satiety == "yes" or \
                observation[0] == "no" and satiety == "yes":
            enticement = "?"
        else:
            nutritional = "?"

    '''

    '''   
     For loop to classify the features aka add in the classes corresponding
    to the features 
    '''

    '''
    for i, observation in enumerate(observations):
        if observation[0] == yes and satiety == yes and \
                nutritional == yes and enticement == '?':
            classes[i] = 'Dessert'
        elif observation[0] == yes and satiety == no and \
                nutritional == '?' and enticement == yes:
            classes[i] = 'Dessert'
        elif observation[0] == no and satiety == yes and \
                nutritional == yes and enticement == '?':
            classes[i] = 'Dessert'
        elif observation[0] == no and satiety == yes and \
                nutritional == no and enticement == '?':
            classes[i] = 'Dessert'
        else:
            classes[i] = 'Water'
'''