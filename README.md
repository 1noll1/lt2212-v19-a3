# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Linnea Strand

## Additional instructions

For simplicity I made 'testlines' a required argument. I just chose a random default value (10), but optimally it should be set to a % of the training data – 10 % or so. If you have any suggestions on how to do this in a neat way, do tell me!

**Example commands:**
1. gendata.py brown_rga.txt outputfile 250 -E1000
2. train.py outputfile_train model
3. test.py outputfile_test model.p

## Reporting for Part 4

**Note: In test.py, since smoothing would be terribly cumbersome, all unknown labels are assigned the lowest probability of the distribution returned by pred_log_proba.**

In lines 500-1000 there are considerably less unrecognized classes than in 1-500, which is most likely the reason behind the higher accuracy/lower perplexity in the former.

 Commands | Accuracy  | Perplexity | No. unrecognized classes 
 -------- | --------- | ---------- | ------------------------
 50 -E500 -N2 | 11.25 % | 73.60189119985937 | 234 
 50 -E500 -N3 | 11.925795053003533 %  | 72.83159073041722 | 210 
 50 -S500 -E1000 -N2 | 14.788732394366196 %  | 60.59327328879238  | 186 
 50 -S500 -E1000 -N3 | 12.376237623762377 %  | 67.4001238193053  | 254 
 10 -E100 -N3 | 6.493506493506493 %  | 59.9286003149944  | 53 
 10 -E100 -N4 | 13.125 % | 46.65997234791141 | 44
 10 -E100 -N5 | 12.217194570135746 % | 48.17509472681101 | 61


## Reporting for Part Bonus 

(Delete if you aren't doing the bonus.)
