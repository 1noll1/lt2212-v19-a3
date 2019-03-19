import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

parser = argparse.ArgumentParser(description="Train a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str,
                    help="The file name containing the features.")
parser.add_argument("modelfile", type=str,
                    help="The name of the file to which you write the trained model.")

args = parser.parse_args()

def train_me():
    '''Separate classes from vectors and train the model
    '''
    print("Loading data from file {}.".format(args.datafile))
    data = pd.read_csv(args.datafile)

    classes = list(data.iloc[:, -1])
    vectors = data.iloc[:, :-1]

    logreg = LogisticRegression(solver='lbfgs', multi_class='multinomial',max_iter=1000)
    print("Training {}-gram model.".format(args.ngram))
    model = logreg.fit(vectors,classes)
    print("Writing table to {}.".format(args.modelfile))
    pickle.dump(model, open(args.modelfile + '.p', 'wb'))

train_me()

