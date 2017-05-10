import sys
import csv
from sklearn import model_selection, neighbors, tree
import matplotlib.pyplot as ptl
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

inFN = sys.argv[1]
outFN = sys.argv[2]

X = []
y = []
semi = []

with open(inFN) as fIn:
    inputR = csv.reader(fIn)
    for st in inputR:
        semi.append(st)
        
res = []
X1 = []
X2 = []

for rowD in semi:
    for xd in rowD:
        res.append(float(xd))
    X.append([res[0], res[1]])
    X1.append(res[0])
    X2.append(res[1])
    y.append(int(res[2]))
    res = []



ptl.scatter(X1, X2, c=y)
ptl.show()


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.4, random_state=31, stratify = y)

fOut = open(outFN, 'w')

rep = ""
parame = [{'kernel': ['linear'], 'C': [0.1, 0.5, 1, 5, 10, 50, 100]}]
clf = GridSearchCV(SVC(), parame, cv=5, scoring='accuracy')
clf.fit(X_train, y_train)
Tr_score = clf.score(X_train, y_train)
Te_Score = clf.score(X_test, y_test)
par = "linear"
rep = "svm_" + par + ", " + str(Tr_score) + "," + str(Te_Score) + "\n"
fOut.write(rep)
    
rep = ""
parame = [{'kernel': ['poly'], 'C': [0.1, 1, 3], 'degree': [4, 5, 6], 'gamma': [0.1, 1]}]
clf = GridSearchCV(SVC(), parame, cv=5, scoring='accuracy')
clf.fit(X_train, y_train)
Tr_score = clf.score(X_train, y_train)
Te_Score = clf.score(X_test, y_test)
par = "polynomial"
rep = "svm_" + par + ", " + str(Tr_score) + "," + str(Te_Score) + "\n"
fOut.write(rep)
    
rep = ""
parame = [{'kernel': ['rbf'], 'C': [0.1, 0.5, 1, 5, 10, 50, 100], 'gamma': [0.1, 0.5, 1, 3, 6, 10]}]
clf = GridSearchCV(SVC(), parame, cv=5, scoring='accuracy')
clf.fit(X_train, y_train)
Tr_score = clf.score(X_train, y_train)
Te_Score = clf.score(X_test, y_test)
par = "rbf"
rep = "svm_" + par + ", " + str(Tr_score) + "," + str(Te_Score) + "\n"
fOut.write(rep)
    
rep = ""
parame = {'C': [0.1, 0.5, 1, 5, 10, 50, 100]}
clf = GridSearchCV(LogisticRegression(), parame, cv=5, scoring='accuracy')
clf.fit(X_train, y_train)
Tr_score = clf.score(X_train, y_train)
Te_Score = clf.score(X_test, y_test)
par = "logistic"
rep = par + ", " + str(Tr_score) + "," + str(Te_Score) + "\n"
fOut.write(rep)
    
rep = ""
parame = [{'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 'leaf_size': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]}]
clf = GridSearchCV(neighbors.KNeighborsClassifier(), parame, cv=5, scoring='accuracy')
clf.fit(X_train, y_train)
Tr_score = clf.score(X_train, y_train)
Te_Score = clf.score(X_test, y_test)
par = "knn"
rep = par + ", " + str(Tr_score) + "," + str(Te_Score) + "\n"
fOut.write(rep)
    
rep = ""
parame = [{'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 'min_samples_split': [2, 3, 4, 5, 6, 7, 8, 9, 10]}]
clf = GridSearchCV(tree.DecisionTreeClassifier(), parame, cv=5, scoring='accuracy')
clf.fit(X_train, y_train)
Tr_score = clf.score(X_train, y_train)
Te_Score = clf.score(X_test, y_test)
par = "decision_tree"
rep = par + ", " + str(Tr_score) + "," + str(Te_Score) + "\n"
fOut.write(rep)
    
rep = ""
parame = [{'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 'min_samples_split': [2, 3, 4, 5, 6, 7, 8, 9, 10]}]
clf = GridSearchCV(RandomForestClassifier(), parame, cv=5, scoring='accuracy')
clf.fit(X_train, y_train)
Tr_score = clf.score(X_train, y_train)
Te_Score = clf.score(X_test, y_test)
par = "random_forest"
rep = par + ", " + str(Tr_score) + "," + str(Te_Score) + "\n"
fOut.write(rep)
    

'''
kf = KFold(n_splits=2)

sss = model_selection.StratifiedShuffleSplit(n_splits=5, test_size=0.4, random_state=31)

for train_index, test_index in sss.split(X, y):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
''' 

fOut.close()
print "Done"