import textblob.classifiers
from textblob.classifiers import NaiveBayesClassifier
import csv
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize



###module 1 for testing and traing of 1 gram words

train1=[]
test1=[]
def training1():
    with open('training_file_1gram.csv', 'r', encoding='utf-8') as fp:
        rows = csv.reader(fp)
        for row in rows:
            tup = ()
            tup = (row[0], row[1])
            train1.append(tup)

def testing1():
    with open('gold_testing_1gram.csv', 'r', encoding='utf-8') as fp:  # test the module
        rows1 = csv.reader(fp)
        for row in rows1:
            tup = ()
            tup = (row[0], row[1])
            test1.append(tup)
    #cl1 = NaiveBayesClassifier(train1[:500])
    #print(cl.accuracy(test1[:500]))
def classify1():
    training1()
    testing1()
classify1()
cl1 = NaiveBayesClassifier(train1[:500])




###module 2 for testing and traing of 5 gram words

train5=[]
test5=[]
def training5():
    with open('training_file_5gram.csv','r',encoding='utf-8') as fp:
        rows=csv.reader(fp)
        for row in rows:
            tup=()
            tup=(row[0],row[1])
            train5.append(tup)


def testing5():
    with open('gold_testing_1gram.csv','r',encoding='utf-8') as fp:
        rows1=csv.reader(fp)
        for row in rows1:
            tup=()
            tup=(row[0],row[1])
            test5.append(tup)
    #cl2 = NaiveBayesClassifier(train5[:500])
    #print(cl.accuracy(test5[500:700]))
def classify5():
    training5()
    testing5()
classify5()
cl2 = NaiveBayesClassifier(train5[:500])



###module 3 for short test formation
symp_sent=""
disease_sent=""
drug_sent=""
file1= open("data_txt.txt", "r")
data=""
for f in file1:
    data+=f
data_sent=sent_tokenize(data)#tokenize the file for taking sentences as whether symptom ,disease or none
for i in range(0,len(data_sent)):
    #if(cl1.classify(data_sent[i])=="Disease-inside" or cl2.classify(data_sent[i])=="Disease-inside"):
        #print(data_sent[i])
    #print(cl1.classify(data_sent[i]))
    #print(cl2.classify(data_sent[i]))
    if(cl1.classify(data_sent[i])=="Symptom-begin" or  cl2.classify(data_sent[i])=="Symptom-begin") :
        #print(data_sent[i])
        symp_sent+=(data_sent[i])
    if (cl1.classify(data_sent[i]) == "Symptom-inside" or cl2.classify(data_sent[i]) == "Symptom-inside"):
        #print(data_sent[i])
        symp_sent += (data_sent[i])

    if(cl1.classify(data_sent[i])=="Disease-begin" or cl2.classify(data_sent[i])=="Disease-begin"):
        #print(data_sent[i])
        disease_sent+=(data_sent[i])
    if (cl1.classify(data_sent[i]) == "Disease-inside" or cl2.classify(data_sent[i]) == "Disease-inside"):
        #print(data_sent[i]
        disease_sent += (data_sent[i])
    if (cl1.classify(data_sent[i]) == "Drug-begin" or cl2.classify(data_sent[i]) == "Drug-begin") :
        #print(data_sent[i])
        drug_sent+=(data_sent[i])
    if (cl1.classify(data_sent[i]) == "Drug-inside" or cl2.classify(data_sent[i]) == "Drug-inside"):
        #print(data_sent[i])
        drug_sent += (data_sent[i])




print("Disease::::::::::::")
print(disease_sent)
print()
print("Symptom::::::::::::")
print(symp_sent)
print()
print("Drugs::::::::::::::")
print(drug_sent)
