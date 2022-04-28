# finalProject-jh470

## DecisionTreesFinalProject

DecisionTreesFinalProject contains the '__main__' that will run the algorithm. It has the four necessary lists: allattr, a list of attributes, attr, the same list of attributes that can be altered, attrvals, a list of lists of the attribute values, and classif_list, a list of classifications. Other constants include the numrows and percent which are necessary for creating the data and determining the size of the train and test set. 

First, it creates the data. Then, it splits the Data into a trainset and testset, Next, I use the ID3 method on the trainset to create the Decision Tree. Finally, to show the efficacy and accuracy of the algorithm I do a two part process. To begin, I count the number of correct classifications and divide by the total number of rows, which should equal 1.0 for a perfectly classified dataset (100% accuracy). Then, I change exactly one classification of the testset to purposely get less than 100% accuracy. Doing so should give a result less than 100%. 


## Data
The Data class makes a data object and has three methods (unique_combinations, expand, and split). First, I make the unique combinations by following the self-made tree. Then, I expand the dataset to the desired number of rows using np.random.choice. Finally, I split the data into a train set and a test set. 

## Node 
The Node class creates the Node object made up of attribute, parent_value, childlist, and the classification. It has a repr function to print and a correponding method to print in a tree like manner. 

## ID3 
ID3 has two methods, the ID3_method and the calc_entropy method. ID3_method is the recursive ID3 algorithm that incorporates finding the information gain and choosing the attribute with the maximum information gain to make that the node. It also keeps track (adds the information about the parent value). The calc_entropy method calculates the entropy of the input data. 

## Classify
The classify file holds the recursive classify method and several helper functions to determine what the decision tree created using the train data would choose following each line of the test data. It gets the index of where the attribute from the decision tree is located to then get the attribute value in the test data. Then, it gets the child node. Finally, it continues this until it hits a leaf node where it returns the classification. 
