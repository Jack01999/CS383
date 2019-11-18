import csv
import math
import numpy as np
from sklearn.cluster import KMeans

def to_numerical(votes):
    num_vote = []
    for vote in votes:
        if vote == 'Yea' or vote == 'Aye':
            num_vote.append(1)
        elif vote == 'Nay' or vote == 'No':
            num_vote.append(0)
        else:
            num_vote.append(0.5)
    return num_vote

def to_string(votes):
    """
        Implement the inverse of to_numerical here.
        (hint: Change this if you make changes to to_numerical.)
    """
    num_vote = []
    for vote in votes:
        if vote == 1:
            num_vote.append("Yea")
        elif vote == 0:
            num_vote.append("Nay")
        else:
            num_vote.append("Not Voting")
    return num_vote

class CongressionalKMeans():
    def __init__(self, path_to_csv, k, seed=0):
        """
        A model for clustering members of congress based on 
        their voting records. Complete this constructor in order
        to load the voting records from the file given by
        path_to_csv.
        (hint 1: See get_votes for the desired format.)
        (hint 2: Use to_binary function to convert data into numeric format 
                 appropriate for k-means clustering)
        (hint 3: You can use the DataSet constructor in tree.py for inspiration,
                 but you will need to do some things differently. You also do not
                 need all of the attributes, only the voting record.)

        Args:
            path_to_csv (str): The path to a congressional data set
            k (int): The number of clusters to fit
            seed (int): The random seed
        """
        np.random.seed(seed)
        self.k = k
        with open(path_to_csv, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.attributes = next(csvreader) # The first array with attributes ("Name, State, District, Party, Vote1, ...")
            self.nonBinarys = [] # Hold the first four elements in each row ("Name, State, District, Party")
            self.beforeConversion = [row for row in csvreader]
            self.votes = [] # Hold all of the votes elements in each row ("Yea, Nay, etc"), these will be converted to 0s and 1s
            
            ##### TODO complete the constructor #####
            for rows in self.beforeConversion:
                self.nonBinarys.append(rows[:4])
                self.votes.append(to_numerical(rows[4:]))
            self.votes = np.array(self.votes)

    def get_votes(self):
        """
        Returns an (N, M) numpy array containing all votes 2018,
        where N is the number of congresspeople andM is the number 
        of resolutions. Each vote should have a numerical value. (See to_numerical)
        (hint: You shouldn't have to do anything except access an
               instance variable in this function. All of the work
               should be done in the constructor)
        """
        return self.votes

    def fit(self):
        """
        Fit the dataset using k-means clustering.
        (hint: Store any variables you need for other parts
               of the assignment as instance variables. No return
               value is necessary.)
        """
        self.kmeans = KMeans(n_clusters=self.k, random_state=0).fit(self.get_votes())

    def predict(self, i):
        """
        Predict the cluster for the i-th congressperson.
        Return a single number representing the cluster ID.
        (hint 1: you must call fit() first)
        (hint 2: see the documentation for sklearn.cluster.KMeans.predict())
        (hint 3: remember to store anything you need in fit())

        Args:
            i (int): The index of the congressperson to predict.

        Returns:
            (int): The cluster that the i-th congressperson belongs to.
        """
        X = self.get_votes()[i]
        return self.kmeans.predict([X])

    def get_cluster_center(self, i):
        """
        Return a numpy array of size (N,) containing center of the i-th cluster.
        (hint: see the documentation for sklearn.cluster.KMeans.cluster_centers_)
        """

        return np.array(self.kmeans.cluster_centers_[i])

    def get_median_voter(self, i):
        """
        Return an numpy array of size (N,) containing the the most likely
        vote for each vote for the given cluster.
        (hint: Use np.round on the cluster center to convert votes to 0 or 1 (or other values that you use).)
        """
        return np.round(self.get_cluster_center(i))
        
    def test_congress(self):
        republican_correct = 0 
        democrat_correct = 0
        republicans = 0
        democrats = 0
        for x in range(len(self.votes)):
            # check republicans = 0
            if self.nonBinarys[x][3] == 'Republican':
                republicans += 1
                if self.predict(x) == 0:
                    republican_correct += 1
                else:
                    print("Misclassification at congressperson ID: ", x)
                    print(self.beforeConversion[x])
            # check democrats = 1
            if self.nonBinarys[x][3] == 'Democrat':
                democrats += 1
                if self.predict(x) == 1:
                    democrat_correct += 1

        print("Number of correctly classified Republicans:", republican_correct)
        print("Number of total Republicans:", republicans)
        print("Percent of correctly classified Republicans to total Republicans:", republican_correct / republicans * 100, "%")

        print("Number of correctly classified Democrats:", democrat_correct)
        print("Number of total Democrats:", democrats)
        print("Percent of correctly classified Democrats to total Democrats:", democrat_correct / democrats * 100, "%")
        return (republican_correct + democrat_correct)/len(self.votes) * 100

    def test_median(self):
        correct = 0
        for x in range(len(self.get_cluster_center(1))):
            if np.round(self.get_cluster_center(0)[x]) != np.round(self.get_cluster_center(1)[x]):
                correct += 1
                print(x)

        return correct / len(self.get_cluster_center(1)) * 100

                

if __name__ == '__main__':
    """
    You can use this area to test your implementation and to generate
    output for the assignment. The autograder will ignore this area.
    """
    kmeans = CongressionalKMeans('congress_data.csv', 4)
    kmeans.fit()
    print(kmeans.test_congress())
    #print(kmeans.test_median())
    #print(kmeans.predict(0))
    #print(kmeans.predict(2))
