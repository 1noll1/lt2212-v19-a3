import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
import math
from collections import Counter

parser = argparse.ArgumentParser(description="Test a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str,
                    help="The file name containing the features in the test data.")
parser.add_argument("modelfile", type=str,
                    help="The name of the saved model file.")

args = parser.parse_args()

def fetch_model():
    print("Loading model from file {}.".format(args.modelfile))
    model = open(args.modelfile, 'rb')
    pickled = pickle.load(model)

    classes = pickled.classes_
    print('Number of classes in model:', len(classes))

    return pickled, classes

def test_data():
    '''Separate test vectors from their classes
    '''
    print("Loading data from file {}.".format(args.datafile))
    data = pd.read_csv(args.datafile)
    test_classes = list(data.iloc[:, -1])

    vectors = data.iloc[:, :-1]

    return vectors, test_classes

def perplex_me(vectors, model, test_classes):
    '''Calculate perplexity of the model.
    If the true label is unknown to the classifier, assume class with the lowest probability.
    '''
    classes = model.classes_
    log_probs = model.predict_log_proba(vectors)
    class_index = {class_: number for number, class_ in enumerate(classes)}

    summies = 0
    unknown = 0

    for i, probdist in enumerate(log_probs):
        label = test_classes[i]
        if label in classes:
            log_prob = log_probs[i][class_index[label]]
            summies += log_prob
        else:
            log_prob = min(log_probs[i])
            summies += log_prob
            unknown += 1

    summies = (-1/len(test_classes)) * summies
    print('Summy is:', summies)
    print('Unrecognised classes in test data:', unknown)
    perplexity = 2**summies

    return perplexity

def test_me(model, vectors, classes):
    print("Testing {}-gram model.".format(args.ngram))

    acc = model.score(vectors, classes)
    print("Accuracy is {} %".format(acc * 100))

    perplexity = perplex_me(vectors, model, classes)

    print("Perplexity is {}".format(perplexity))

model, classes = fetch_model()
vectors, test_classes = test_data()
test_me(model, vectors, test_classes)
