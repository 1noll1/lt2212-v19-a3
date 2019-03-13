import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

parser = argparse.ArgumentParser(description="Test a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str,
                    help="The file name containing the features in the test data.")
parser.add_argument("modelfile", type=str,
                    help="The name of the saved model file.")

args = parser.parse_args()

def fetch_model():
    model = open(args.modelfile, 'rb')
    pickled = pickle.load(model)
    return pickled

def test_data():
    '''Separate vectors from their classes
    '''
    data = pd.read_csv(args.datafile)
    classes = list(data.iloc[:, -1])
    vectors = data.iloc[:, :-1]

    return vectors, classes

def testy(model, vectors, classes):
    '''Hmm... Needs a neat entropy formula.
    '''
    acc = model.score(vectors, classes)

    predictions = model.predict_log_proba(vectors)
    print(predictions)

    print("Accuracy is {}".format(acc))

    print("Perplexity is...")

model = fetch_model()
vectors, classes = test_data()
testy(model, vectors, classes)

print("Loading data from file {}.".format(args.datafile))
print("Loading model from file {}.".format(args.modelfile))

print("Testing {}-gram model.".format(args.ngram))


