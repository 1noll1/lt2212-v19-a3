# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Linnea Strand

## Additional instructions

I made 'testlines' a required argument, for simplicity. I just chose a random default value (10), but optimally it should be set to a % of the training data – 10 % or so. 

## Reporting for Part 4

Note: In test.py, since smoothing would be terribly cumbersome, any unknown labels are assigned the lowest probability of the distribution returned by pred_log_proba.

As is to be expected, trigrams are more accurate than bigrams. Also, in lines 500-1000 there are considerably less unrecognized classes than in 1-500, which is most likely the reason behind the higher accuracy/lower perplexity in the former.

Example commands:
gendata.py brown_rga.txt outputfile 250 -E1000
train.py outputfile_train model
test.py outputfile_test model.p

/***
| Commands | Accuracy  | Perplexity | No. unrecognized classes |
| 50 -E500 -N2 | 11.25 % | 73.60189119985937 | 234 |
| 50 -E500 -N3 | 11.925795053003533 %  | 72.83159073041722 | 210 |
| 50 -S500 -E1000 -N2 | 14.788732394366196 %  | 60.59327328879238  | 186 |
| 50 -S500 -E1000 -N2 | ...  | ...  | ... |
| 50 -S500 -E1000 -N2 | ...  | ...  | ... |
***/

## Reporting for Part Bonus 

(Delete if you aren't doing the bonus.)
