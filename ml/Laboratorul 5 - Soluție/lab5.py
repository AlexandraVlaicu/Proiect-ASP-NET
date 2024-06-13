import numpy as np
from sklearn import preprocessing
from sklearn import svm
from sklearn.metrics import f1_score, classification_report
import pdb

from bag_of_words import *


# load data
training_data = np.load('data/training_sentences.npy')
training_labels = np.load('data/training_labels.npy')
test_data = np.load('data/test_sentences.npy')
test_labels = np.load('data/test_labels.npy')


bow_model = Bag_of_words()
bow_model.build_vocabulary(training_data) 

def compute_accuracy(gt_labels, predicted_labels):
    accuracy = np.sum(predicted_labels == gt_labels) / len(predicted_labels)
    return accuracy

def normalize_data(train_data, test_data, type=None):
    scaler = None
    if type == 'standard':
        scaler = preprocessing.StandardScaler()

    elif type == 'min_max':
        scaler = preprocessing.MinMaxScaler()

    elif type == 'l1':
        scaler = preprocessing.Normalizer(norm='l1')

    elif type == 'l2':
        scaler = preprocessing.Normalizer(norm='l2')

    if scaler is not None:
        scaler.fit(train_data)
        scaled_train_data = scaler.transform(train_data)
        scaled_test_data = scaler.transform(test_data) 
        return (scaled_train_data, scaled_test_data)
    else:
        print("No scaling was performed. Raw data is returned.")
        return (train_data, test_data)

train_features = bow_model.get_features(training_data)
test_features = bow_model.get_features(test_data) 
print(train_features.shape)
print(test_features.shape)
scaled_train_data, scaled_test_data = normalize_data(train_features, test_features, type='l2')

svm_model = svm.SVC(C=100, kernel='linear')
svm_model.fit(scaled_train_data, training_labels)
predicted_labels_svm = svm_model.predict(scaled_test_data) 
model_accuracy_svm = compute_accuracy(np.asarray(test_labels), predicted_labels_svm)
print('f1 score', f1_score(np.asarray(test_labels), predicted_labels_svm))
print("SVM model accuracy: ", model_accuracy_svm * 100)
print(classification_report(np.asarray(test_labels), predicted_labels_svm))
coefs = np.squeeze(np.array(svm_model.coef_))
idx = np.argsort(coefs)  
print('the first 10 negative words are', bow_model.words[idx[:10]])
 
print('the first 10 positive words are', bow_model.words[idx[-10:]])
