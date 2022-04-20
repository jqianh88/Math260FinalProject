# import random
import numpy as np
import math


# import pandas as pd


class Data:
    '''
    Class attributes:
    features: The combination of nodes or questions of the hand drawn decision
              tree stored as a list of lists.
    classes: The dessert stored as a list.

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


   # attr_classes: holds the combination of attrs with the element as the class



    def __init__(self, numrows, attr_classes=None):

            if attr_classes is None:
                all_combinations = self.unique_combos()  # generate all combos
                self.attr_classes = self.expand(numrows)  # expand
            else:
                self.attr_classes = attr_classes  # numrows needs to match len classes


    # Method for unique combinations
    def unique_combos(self):

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


    # Method to expand the perfect Data by random sampling the perfect
    # dataset to make a dataset of numrows length
    def expand(self, numrows):

        expanded = self.unique_combos()[np.random.choice(
            self.unique_combos().shape[0],numrows, replace= numrows>16)]

        return expanded


    # Method to create two DessertData objects from one DessertData Object
    def split(self, percent, numrows):
        trainnumrows = int(percent * numrows)  # make it an int
        train_data = self.attr_classes[:trainnumrows]  # all rows up to 90%
        test_data = self.attr_classes[trainnumrows:]   # last 10%
        return train_data, test_data



    def remove_feature(self, feature_info):
        # thinking that feature_info is a list

        pass









