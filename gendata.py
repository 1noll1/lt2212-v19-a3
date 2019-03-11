import os, sys
import glob
import argparse
import numpy as np
import pandas as pd
import re
from nltk import ngrams
import random

'''Definitely not done
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
    if args.endline < args.startline: #make me work
        raise ValueError("Endline value must be greater than startline!")

if args.testlines and args.endline and args.startline:
    #pick a random number in range(startline,endline) to use as test data
    num_range = [i for i in range(args.startline, args.endline)]
    random.shuffle(num_range)
    print("Test sentences: {}".format(num_range))

print("Constructing {}-gram model.".format(args.ngram))
print("Writing table to {}.".format(args.outputfile))

def collect_data(): 
    '''Starting symbol: <s>
    '''
    vocab = ['<s>']

    testlines = []
    trainlines = []

    # output_feature_table = []

    with open(args.inputfile) as f:
        position = 0 #keep track of line index
        if args.startline:
            for i in range(args.startline): #start at later line
                line = f.readline()
        for line in f:
            position += 1
            line = [word.split("/")[0] for word in line.split()] #all cred to user Kevin@StackOverflow: https://stackoverflow.com/questions/15365046/python-removing-pos-tags-from-a-txt-file
            vocab.extend(line)
            if args.testlines:
                if position in num_range: #select lines to use as test data
                    testlines.extend(line)
                else:
                    trainlines.extend(line)
            # if position == args.endline: #pick line to be used as output feature table
            #     output_feature_table.extend(line)

    # print(output_feature_table)

    vocab = set(vocab)
    empty_vector = np.zeros(len(vocab), dtype=int)
    #print(len(vocab))
    #print(vocab)
    word_index = {j:i for i,j in enumerate(vocab)}

    one_hot = {w: np.zeros(len(vocab), dtype=int) for w in vocab}

    for word in list(one_hot): #iterate over vocabulary keys while it's changing
        i = word_index[word]
        #print(one_hot[word])
        one_hot[word][i] = 1 
    #print(one_hot)

    return vocab, one_hot
    #print(word_index)

def construct_ngrams(text, N=None):
    vocab, one_hot = collect_data()
    N = args.ngram
    grams = ngrams(vocab, N, pad_left=True, pad_right=False, left_pad_symbol='<s>')
    #print(grams)
    # print(list(grams))

    onehot_vectors = []

    for gram in grams:
        #print(gram)
        wordy = [gram[2]]
        vector = [one_hot[w] for w in gram[:-1]]
        vector.extend(wordy)
        onehot_vectors.append(vector)

    return onehot_vectors
    # print(onehot_vectors)

def gen_output(dataset, setname):
    filename = args.outputfile + '{}'.format('_' + setname)
    # train_file = args.outputfile + '{}'.format('_train')
    # test_file = args.outputfile + '{}'.format('_test')

    data = pd.DataFrame(dataset)   
    # train_data = pd.DataFrame(trainset)
    # test_data = pd.DataFrame(testset)

    #print(df)
    data.to_csv(filename, index=False)
    # train_data.to_csv(train_file, index=False)
    # test_data.to_csv(test_file, index=False)
    
vocab = collect_data()
# construct_ngrams(vocab)
data = construct_ngrams(vocab)
for i in ['train', 'test']:
    # construct_ngrams(data, N)
    gen_output(construct_ngrams(vocab), i)

    
# THERE ARE SOME CORNER CASES YOU HAVE TO DEAL WITH GIVEN THE INPUT
# PARAMETERS BY ANALYZING THE POSSIBLE ERROR CONDITIONS.
