# finalProject-jh470

## DecisionTreesFinalProject

DecisionTreesFinalProject contains the '__main__' that will run the algorithm. It has the four necessary lists: allattr, a list of attributes, attr, the same list of attributes that can be altered, attrvals, a list of lists of the attribute values, and classif_list, a list of classifications. Other constants include the numrows and percent which are necessary for creating the data and determining the size of the train and test set. 

First, it creates the data. Then, it splits the Data into a trainset and testset, Next, I use the ID3 method on the trainset to create the Decision Tree. Finally, to show the efficacy and accuracy of the algorithm I do a two part process. To begin, I count the number of correct classifications and divide by the total number of rows, which should equal 1.0 for a perfectly classified dataset (100% accuracy). Then, I change exactly one classification of the testset to purposely get less than 100% accuracy. Doing so should give a result less than 100%. 


## Data

