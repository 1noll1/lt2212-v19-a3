# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Linnea Strand

## Additional instructions

I made 'testlines' a required argument, for simplicity. I just chose a random default value (10), but optimally it should be set to a % of the training data – 10 % or so. 

## Reporting for Part 4

Note: In test.py, since smoothing would be terribly cumbersome, any unknown labels are assigned the lowest probability of the distribution returned by pred_log_proba.

Example commands:
gendata.py brown_rga.txt outputfile 250 -E1000
train.py outputfile_train model
test.py outputfile_test model.p

| Commands | Accuracy  | Perplexity | No. unrecognized classes |
| gendata.py brown_rga.txt outputfile 50 -E500 -N2 | 11.25 % | 73.60189119985937 | 234 |
| 50 -E500 -N3 | 11.925795053003533 %  | 72.83159073041722 | 210 |
| ... | ...  | ...  | ... |

## Reporting for Part Bonus 

(Delete if you aren't doing the bonus.)
