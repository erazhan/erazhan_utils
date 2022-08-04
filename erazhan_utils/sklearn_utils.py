# -*- coding = utf-8 -*-
# @time: 2022/2/23 3:17 下午
# @Author: erazhan
# @File: sklearn_utils.py

# ----------------------------------------------------------------------------------------------------------------------

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc

# ----------------------------------------------------------------------------------------------------------------------

def show_ml_metric(test_labels, predict_labels, predict_prob):
    accuracy = accuracy_score(test_labels, predict_labels)
    precision = precision_score(test_labels, predict_labels)
    recall = recall_score(test_labels, predict_labels)
    f1_measure = f1_score(test_labels, predict_labels)
    confusionMatrix = confusion_matrix(test_labels, predict_labels)
    fpr, tpr, threshold = roc_curve(test_labels, predict_prob, pos_label=1)
    Auc = auc(fpr, tpr)
    print("------------------------- ")
    print("confusion matrix:")
    print("------------------------- ")
    print("| TP: %5d | FP: %5d |" % (confusionMatrix[1, 1], confusionMatrix[0, 1]))
    print("----------------------- ")
    print("| FN: %5d | TN: %5d |" % (confusionMatrix[1, 0], confusionMatrix[0, 0]))
    print(" ------------------------- ")
    print("Accuracy:       %.2f%%" % (accuracy * 100))
    print("Recall:         %.2f%%" % (recall * 100))
    print("Precision:      %.2f%%" % (precision * 100))
    print("F1-measure:     %.2f%%" % (f1_measure * 100))
    print("AUC:            %.2f%%" % (Auc * 100))
    print("------------------------- ")
    return (Auc)

if __name__ == "__main__":
    pass