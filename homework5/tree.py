import csv
import math


class DataSet:
    """
    This class reads the dataset from a csv file, given the file path as a string.
    It exposes the following class members:

        attributes: a list of strings representing the name of each attribute
        domains: a list of lists indicating the possible values each attribute
                 in self.attributes can take in the provided data
        examples: a list of lists, with each element representing a datapoint
    """
    def __init__(self, path_to_csv):
        with open(path_to_csv, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.attributes = next(csvreader)
            self.examples = [row for row in csvreader]
            self.domains = [list(set(x)) for x in zip(*self.examples)]

    def set_attrs(self, attrs):
        self.attributes = attrs

    def set_examples(self, exs):
        self.examples = exs

    def set_domains(self, doms):
        self.domains = doms


class Node:
    """
    This class represents an internal node of a decision tree.
    `test_attr` is the index of the attribute to test at this node.
    `test_name` is the human-readable name of that attribute.
    The Node stores a dictionary `self.children` that maps values of the test
    attribute to subtrees, where each subtree is either a Node or a Leaf.
    """
    def __init__(self, test_attr, test_name=None):
        self.test_attr = test_attr
        self.test_name = test_name or test_attr
        self.children = {}

    def classify(self, example):
        """Classify an example based on its test attribute value."""

        # TODO: Implement the classify function here and in the Leaf class
        pass

    def add_child(self, val, subtree):
        """Add a child node, which could be either a Node or a Leaf."""
        self.children[val] = subtree

    def show(self, level=1):
        """Print a human-readable representation of the tree"""
        print('Test:', self.test_name)
        for (val, subtree) in self.children.items():
            print(' ' * 4 * level, "if", self.test_name, '=', val, '==>', end=' ')
            if isinstance(subtree, Leaf):
                subtree.show()
            else:
                subtree.show(level + 1)


class Leaf:
    """A Leaf holds only a predicted class, with no test."""
    def __init__(self, pred_class):
        self.pred_class = pred_class

    def classify(self, example):
        # TODO: Implement the classify function here
        pass

    def show(self):
        """This will be called by the Node `show` function"""
        print('Predicted class:', self.pred_class)


def learn_decision_tree(dataset, target_name, feature_names, depth_limit):
    """
    Trains a decision tree on the provided dataset.
    The `target_name` parameter is the name of the attribute to be predicted.
    The `feature_names` are the names of input attributes that should be used to split the data.
    Finally, `depth_limit` is a parameter to control overfitting by cutting off the tree after
    a certain depth and predicting the plurality class at that split.

    This function should return a decision tree learned from the data.
    """
    domains = dataset.domains
    target = dataset.attributes.index(target_name)
    features = [dataset.attributes.index(name) for name in feature_names]

    def plurality_value(self, examples):
        pass

    def decision_tree_learning(examples, attrs, parent_examples=(), depth=0):
        """
        This function signature is written to match the pseudocode
        on p. 702 of Russell and Norvig. We recommend following that
        pseudocode to implement your decision tree.
        Note that we are adding an argument for the current depth, so you can
        keep track of the depth limit.

        This function should return the decision tree that has been learned.
        """

        # TODO: Implement the logic for learning the decision tree
        # You must also implement the entropy and information gain functions below.
        # We recommend adding your own helper functions below too, but don't remove
        # any of the provided code.
        tree = None
        print(information_gain(examples, create_children(examples)))
        '''
        if len(examples) == 0:
            plurality_value(parent_examples)
        #else if all examples have the same classification
        elif len(attrs) == 0:
            plurality_value(examples)
        else:
            A = max(information_gain(attrs, examples))
            root = Tree()
            root.data = A
            for value in A:
                subtree = decision_tree_learning(exs, attrs - A, examples, depth)
        '''
        #print(entropy(examples))
        #for x in features:
            #information_gain(examples, examples[x])
        return tree

    def count_majority(examples, i):
        yes_counter = 0
        no_counter = 0
        for example in examples:
            if example[i] == 'Yea':
                yes_counter += 1
            elif example[i] == 'Nay':
                no_counter += 1
        if yes_counter > no_counter:
            return True
        return False

    def create_children(examples):
        new_split = []
        for example in examples:
            if count_majority(examples, 4) == True: 
                if (example[4] == 'Yea' or example[4] == 'Not Voting' or example[4] == 'Present' or example[4] == ''):
                    new_split.append(example)
            else:
                if (example[4] == 'Nay' or example[4] == 'Not Voting' or example[4] == 'Present' or example[4] == ''):
                    new_split.append(example)
        print(new_split)
        return new_split

    def find_probability(examples, party):
        party_counter = 0

        for example in examples:
            if example[target] == party:
                party_counter += 1

        return party_counter

    def entropy(examples):
        """Takes a list of examples and returns their entropy with respect to the target attribute"""

        # TODO: Implement the entropy function
        republican_counter = find_probability(examples, 'Republican')
        democrat_counter = find_probability(examples, 'Democrat')

        p1 = republican_counter / len(examples)
        p2 = democrat_counter / len(examples)

        return ((p1 * math.log2(p1)) + (p2 * math.log2(p2))) * -1


    def information_gain(parent, children):
        """
        Takes a `parent` set and a subset `children` of the parent.
        Returns the information gain due to splitting `children` from `parent`.
        """

        # TODO: Implement the information gain

        parent_entropy = entropy(parent)

        # yes = child1
        # no = child2
        children_entropy = entropy(children)
        children_prob = (find_probability(children, 'Republican') + find_probability(children, 'Democrat')) / (find_probability(parent, 'Republican') + find_probability(parent, 'Democrat'))
        parent_entropy -= (children_entropy * children_prob)
        print((find_probability(children, 'Republican') + find_probability(children, 'Democrat')))


        return parent_entropy


    return decision_tree_learning(dataset.examples, features)


if __name__ == '__main__':
    """
    You can use this area to test your implementation and to generate
    output for the assignment. The autograder will ignore this area.
    """

    ############################
    ###### Example usage: ######
    ############################

    data = DataSet("./congress_small.csv")

    #print("attributes ", data.attributes)
    #print("examples ", data.examples)
    #print("domains ", data.domains)

    # An example of learning a decision tree to predict party affiliation
    # based on the values of votes 4-7
    t = learn_decision_tree(
        data,
        "class",
        ["vote4", "vote5", "vote6", "vote7"],
        2
    )
    #print(t)
    #print(t)
    #t.show()