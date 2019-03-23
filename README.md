# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Linnea Strand

## Additional instructions

For simplicity I made 'testlines' a required argument. I just chose a random default value (10), but optimally it should be set to a % of the training data – 10, 25 % or so. If you have any suggestions on how to do this in a neat way, do tell me!

**Example commands:**
1. gendata.py brown_rga.txt outputfile 250 -E1000
2. train.py outputfile_train model
3. test.py outputfile_test model.p

-POS for bonus part.

## Reporting for Part 4

**Note: In test.py, since smoothing would be terribly cumbersome, all unknown labels are assigned the lowest probability of the distribution returned by pred_log_proba.**

Presented below is the result of my experiments, but because the train lines are chosen at random, you might get a very different answer if you run in yourselves! This also means my runs with different size grams aren't completely fair - the test data changes. 

However, some of these experiment turn out as expected; more test data -> higher accuracy. Trigrams are also more accurate than both 2 and 4 grams when S to E is only 100 lines, which to be expected. When N is equal to or more than 4, there are simply too many "unique" grams, meaning they have very low probability of appearing in both the training and test data.

What's going on in the 500 line data – I actually have no idea.

 Commands | Accuracy  | Perplexity | No. unrecognized classes 
 -------- | --------- | ---------- | ------------------------
 50 -E500 -N2 | 11.827956989247312 % | 73.11494637354558 | 221 
 50 -E500 -N3 | 11.770726714431934 %  | 68.68841078110083 | 195 
 50 -E500 -N4 | 14.033457249070633 %  | 70.75733860144607 | 217 
 100 -E500 -N2 | 13.240250361097738 % | 67.76737489554277 | 448 
 100 -E500 -N3 | 13.007380073800737 %  | 67.56102201728008 | 437 
 100 -E500 -N4 | 13.960749330954506 %  | 66.74428177788408 | 471
 10 -E100 -N2 | 7.853403141361256 %  | 52.776329742864746  | 71 
 10 -E100 -N3 | 13.740458015267176 %  | 44.93628822918378  | 91 
 10 -E100 -N4 | 9.844559585492227 % | 52.84378963173467 | 59
 25 -E100 -N2 | 9.506398537477148 %  | 50.34846038799879  | 205 
 25 -E100 -N3 | 11.211573236889691 %  | 48.65698771568221  | 200 
 25 -E100 -N4 | 10.036496350364963 % | 50.7892735102192 | 211

## Reporting for Part Bonus 

What happens when we use parts of speech instead of simple word representations?
Obviously, our dimensionality decreases significantly. The number of possible features is now reduced to the number of parts of speech – naturally quite few. First of all, this frees a lot of computational power for us to use. Moreover, it makes for more accurate generalisations. There are simply fewer possible patterns to keep track of. As there are ways fewer unrecognised classes and more reoccuring patterns, our model is now way less "perplexed".

 Commands | Accuracy  | Perplexity | No. unrecognized classes 
 -------- | --------- | ---------- | ------------------------
 10 -E100 -N2 -POS | 21.468926553672315 % | 9.957578770049116 | 10 
 10 -E100 -N3 -POS | 25.157232704402517 %  | 8.101553201727222 | 9 
 10 -E100 -N4 -POS | 18.902439024390244 %  | 9.279334998979055 | 1 
 
 50 -E500 -N2 -POS | 27.8503046127067 %  | 7.127667757014879 | 6
 50 -E500 -N3 -POS | 30.190311418685123 % | 6.553241245979299 | 2
 50 -E500 -N4 -POS | 31.556683587140437 % | 6.640151718730408 | 3
