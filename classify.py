'''
The classify method tests what the tree answers that was created by the
training data versus the actual test data.
Inputs: a node created from the train data and a dataline from the test data
outputs: A float of the percent classified correctly between the train and
test data



Ea column matches (allattr) label with same exact words using in node
attribute
 a node attribute

 traverse through the tree, go from root
 look at node attribute go to look at that column and the value --> you
 choose which edge to take
 which child has edge attribute
 then recursively do that node --> column --> figure out edge --> get to a leaf
 then leaf needs to match classvalue of line[-1]

 y o n



 if node.classification != '' == leaf node

 root --> look at dataline for the column
I get the value from that column of that data line
That value = edge and the edge sits in parent value of the child node
knowing value --> new node
then recursive


'''


def classify(node, dataline, allattr, attrvals):

    # return classification {Base case}
    if node.classification != '':
        return node.classification
    # dataline Column is equal to the attribute in the list
    column_num = get_column_num(allattr, node.attribute)
    value = dataline[column_num]
    new_node = get_new_node(node.childlist, value, attrvals)



    return classify(new_node, dataline, allattr, attrvals)




def get_column_num(allattr, attribute):

    # Can use list comprehension, or indexing (use index command)
    for index, attr in enumerate(allattr):
        if attr == attribute:
            return index


def get_new_node(childlist, value, attrvals):

    # Better way to do this
    # Childlist is a list of nodes, value = edge, node is in childlist
    for node in childlist:

        # pointerback
        # I need attr values list, -- what
        temp = convert_parent_value(node.parent_value, attrvals)
        if temp == value:
            return node

# This converts node.parent_value from a string version of attrvals to int (0/1)
def convert_parent_value(parent_value, attrvals):
    # hungry: look at attrvals, find corresponding index, loop through list
    # if matches, return index

    for avals in attrvals:
        for index, value in enumerate(avals):
            if parent_value == value:
                return index

