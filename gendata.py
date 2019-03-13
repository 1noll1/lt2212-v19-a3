import os, sys
import glob
import argparse
import numpy as np
import pandas as pd
import re
from nltk import ngrams
import random

'''Definitely not done :::))))
'''

parser = argparse.ArgumentParser(description="Convert text to features")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int,
                    default=0,
                    help="What line of the input data file to start from. Default is 0, the first line.")
parser.add_argument("-E", "--end", metavar="E", dest="endline",
                    type=int, default=None,
                    help="What line of the input data file to end on. Default is None, whatever the last line is.")
parser.add_argument("inputfile", type=str,
                    help="The file name containing the text data.")
parser.add_argument("outputfile", type=str,
                    help="The name of the output file for the feature table.")
parser.add_argument("-T", "--testlines", type=int, metavar="T",
                    help="Number of randomly selected lines within range -S and -E will be designated as testing data.")

args = parser.parse_args()

print("Loading data from file {}.".format(args.inputfile))
print("Starting from line {}.".format(args.startline))
if args.endline:
    print("Ending at line {}.".format(args.endline))
else:
    print("Ending at last line of file.")

if args.endline and args.startline:
    if args.endline < args.startline: #make me work please?
        raise ValueError("Endline value must be greater than startline!")

if args.testlines and args.endline and args.startline:
    #pick random numbers in range(startline,endline) to use as test data
    num_range = [i for i in range(args.startline, args.endline)]
    num_range = random.sample(num_range, args.testlines)
    print("Test sentences on lines: {}".format(num_range))

print("Constructing {}-gram model.".format(args.ngram))

def collect_data(): 
    '''Starting symbol: <s>
    If line is among the T random lines in num_list, add it to the test data.
    Otherwise add it to training.
    '''
    vocab = ['<s>']
    testlines = []
    trainlines = []

    with open(args.inputfile) as f:
        position = 0 #keep track of line index
        for i in range(args.startline): #start at later line
            position += 1
            line = f.readline()
        while position < args.endline:
            line = f.readline()
            position += 1
            line = [word.split("/")[0] for word in line.split()] #all cred to user Kevin@StackOverflow: https://stackoverflow.com/questions/15365046/python-removing-pos-tags-from-a-txt-file
            vocab.extend(line)
            if position in num_range: #select lines to use as test data
                testlines.extend(line)
            else:
                trainlines.extend(line)

    return vocab, trainlines, testlines

def encode_onehot(vocab):
    '''Make hot one encodings of all words in vocab
    '''
    empty_vector = np.zeros(len(vocab), dtype=int)
    word_index = {j:i for i,j in enumerate(vocab)}

    one_hot = {w: np.zeros(len(vocab), dtype=int) for w in vocab}

    for word in list(one_hot): #iterate over vocabulary keys while it's changing
        i = word_index[word]
        #print(one_hot[word])
        one_hot[word][i] = 1 

    return one_hot

def construct_vectors(text, one_hot, N=None):
    '''Create one hot encoded ngrams:
    [hot, hot, class]
    '''
    #print(text)
    N = args.ngram
    grams = ngrams(text, N, pad_left=True, pad_right=False, left_pad_symbol='<s>')

    onehot_vectors = []

    for gram in list(grams):
        #print(gram)
        wordy = gram[-1]
        vector = []
        for w in gram[:-1]:
            vector += list(one_hot[w])
        vector.append(wordy)
        onehot_vectors.append(vector)   

    return onehot_vectors
    # print(onehot_vectors)

def gen_output(vector, j):
    filename = args.outputfile + '_{}'.format(j)
    print('Generating data frame...')
    data = pd.DataFrame(vector)

    # data = pd.DataFrame(data)   
    print("Writing table to {}.".format(filename))
    data.to_csv(filename, index=False)
    

vocab, trainlines, testlines = collect_data()
one_hot = encode_onehot(vocab)

for i,j in [(trainlines, 'train'), (testlines, 'test')]:
    vector = construct_vectors(i, one_hot, N=None)
    gen_output(vector, j)


