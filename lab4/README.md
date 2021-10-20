### CS561
### Artifical Intelligence Lab
### Indian Institute of Technology Patna
### 2021-22

# Assignment 4

## Team Details:

Team Code: `1801cs03_1801cs07_1801cs46`

Team Name: `MnMnM`

Team Members:

| Name              | Roll Number |
| ----------------- | ----------- |
| Abhishek Chopra   | 1801CS03    |
| Amish Mittal      | 1801CS07    |
| Shashwat Mahajan  | 1801CS46    |

## Notes

1. Both Multivariate and Multinomial versions are implemented
2. Add-one smoothing is implemented
3. 5-fold cross validation result is calculated

### Contents 

* Decision Trees
	* DecisionTree.py : implementation of various models to classify
	* Makefile : installs all dependencies
	* Utils.py : input processing
	* featureablationreport.txt : contains accuracy for each class with all possible feature combinations
	* kfold10cvreport.txt : contains avg. values of precision, recall and F-score for gini-index based models
	* main.py : driver code
	* modelreport.txt : contains precision, recall, F-score, confusion-matrix results for all the models
	* testdata.txt : contains testdata
	* traindata.txt : contains traindata

## Instructions to run the code

1. Download the training dataset from `http://cogcomp.org/Data/QA/QC/train_5500.label`.
2. Download the test dataset from `http://cogcomp.org/Data/QA/QC/TREC_10.label`.
3. Run:
```
python main.py 
```

### Sample Output :

	Check 
	1) modelreport.txt
	2) featureablationreport.txt
	3) kfold10cvreport.txt


______________________
Thanking You!

MnMnM