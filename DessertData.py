# import random
import numpy as np
import math


# import pandas as pd


class DessertData:
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


    '''
    test data: 
    self._features = ["Fever", "Cough", "Breathing"]
    self._classes = [0,1,0,1,1,0,1,1,1,1,0,1,0,0]

    '''

    dt_final = False
    if dt_final:
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

                self.info_gain = self.ig_method()
    else:
        def __init__(self, features = None, classes = None):
            if features is None:
                self.features = self.unique_combos()  # generate covid data
            else:
                self.features = features  # numrows needs to match len classes

            if classes is None:
                answer = self.choice_answer()  # resulting class
                self.classes = answer
            else:
                self.classes = classes  # 2 classes

            self.info_gain = self.ig_method()




    # method to get answer
    def choice_answer(self):
        Dessert = 1
        Water = 0
        no, yes = 0, 1

        classes = [0. for _ in self.features]

        dt_final = False
        if dt_final:
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
        else:
            # Test case with known classes
            classes =  [0,1,0,1,1,0,1,1,1,1,0,1,0,0]

        return classes


    # Method for unique combinations
    def unique_combos(self):
        dt_final = False
        if dt_final:
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

        else:
            fever, cough, breathproblem = 1,1,1
            nofever, nocough, breathnormal = 0,0,0
            rows =  [[nofever, nocough, breathnormal],
                    [fever, cough, breathproblem],
                    [fever, cough, breathnormal],
                    [fever, nocough, breathproblem],
                    [fever, cough, breathproblem],
                    [nofever,cough,breathnormal],
                    [fever,nocough,breathproblem],
                    [fever,nocough,breathproblem],
                    [nofever,cough,breathproblem],
                    [fever,cough,breathnormal],
                    [nofever,cough,breathnormal],
                    [nofever,cough,breathproblem],
                    [nofever,cough,breathproblem],
                    [fever,cough,breathnormal]]

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


    # Calculate the Entropy
    # self.entropy = self.calc_entropy([x for x in range(len(self.classes))])

    '''
    Returns Entropy: the amount of information gain there is at each node
    - entropy of a set S is the average information gain per sample, 
    --> H(S) = sum -p(x)log(p(x)) 
    where X are the classifications (e.g., dessert, water)
    and p(x) is the proportion of set S that are classified as x
    H(S) = 0 when S is perfectly classified 
    '''

    def calc_entropy(self, data):

        tot_rows = len(data)  # num of rows, based on classes list or all data
        entropy = 0  # initialize
        count_dessert = 0
        count_water = 0

        # List of the number of rows that have that class value
        class_list = []

        # For loop that goes through the list or data to found the # of rows
        for i, val in enumerate(data):

            if data[i] == 0:            # for water
                count_water += 1
            if data[i] == 1:            # for dessert
                count_dessert += 1
        class_list.append(count_water)
        class_list.append(count_dessert)
        # Calc entropy for each class in the list of classes
        for clas in class_list:
            prop = float(clas/tot_rows)        # proportion
            # Apply entropy formula for the class
            class_entropy = -prop * math.log2(clas / tot_rows)

            # adding the class entropy to the entropy of the list/dataset
            entropy += class_entropy


        return entropy



    '''
      Calculates the information gain of splitting a set S based on a specific 
      features (when we create a new node in the tree)

      Info_gain(S,feature), = H(S) - sum p(t)H(t) where t in T are the tubsets 
      of the data created by the split, and p(t) is the proportion of the 
      number of elements in each subsset to the number of elements in set S
      S = dataframe?
      '''
    def ig_method(self):
        total_rows = len(self.features)
        unique_features = self.features[0]

        # Entropy of the whole dataset
        total_entropy = self.calc_entropy(self.classes)
        # Obtain all values under a column (which is a feature)

        # initialize list of lists holding all values of given features (col)
        all_feat_vals = [[]*4 for _ in range(len(unique_features))]


        # Loop to obtain all values under a given feature
        for i, row in enumerate(self.features):
            print(row)
            for j, val in enumerate(row):
                print(val, 'val')
                all_feat_vals[j].append(val)
                print(all_feat_vals)

        subset_entropy = 0                  # initialization
        subset_feat = [[] for x in range(len(unique_features))]
        print(subset_feat, 'k')
        #
        # initialization
        info_gain = []
        # Loop through the list of lists of all the values under a col
        # [[values for feat 1],[values for feat 2],[values for feat 3]]
        for i, feat_val_list in enumerate(all_feat_vals):
            print(feat_val_list, 'list of a feature_s values')
            # Access each entry for a given column (feature),
            # its corresponding class value (outcome), and the row in full data
            for (feat_val, class_val, row)  in zip(feat_val_list,
                                                    self.classes,
                                                   self.features):
                print(row, 'row')
                # if the feature value and the class value are the same
                # append the rows from the full dataset
                if feat_val == class_val:
                    subset_feat[i].extend([row])     # may need append instead
                    print(subset_feat, 'subsetdata')
            # proportion of feat val == outcome divided by total num of outcomes
            prop = len(subset_feat)/float(len(self.features))

            subset_entropy = prop*self.calc_entropy(subset_feat)
            info_gain.append(subset_entropy)
        ig_list = [(total_entropy - x) for x in info_gain]



        return ig_list            #list of info gains for each feature

    '''
    entropy: entropy of all the classes, doesn't matter what it is 
    - list of you are looking at. 
    - entropy, go through list, and figure out entropy 



#for featureval in [0,1]:


                # indeces of the feature that satisfy condition
                #ind_feat = [row for row in range(len(self.features)) if
                #                   self.features[row][feature] == featureval]
                #print(ind_feat)
                # class value corresponding to the indeces of the features
                #val_corr = [self.classes[ind] for ind in ind_feat]

                # Summation part of the formula (proportion * entropy)
                #sumfeature += (len(val_corr)/total_rows) * \
                        #self.calc_entropy(val_corr)

            #info_gain.append(self.calc_entropy(self.classes) - sumfeature)
        #print(info_gain, 'info')
    '''


    def get_max_info(self):

        return None

        #unique_features =
        #return info_gain


    def remove_feature(self, feature_info):
        # thinking that feature_info is a list

        pass









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