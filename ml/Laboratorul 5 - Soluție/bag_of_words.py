
import numpy as np

class Bag_of_words:

    def __init__(self): 
        self.words = []
        self.vocabulary_length = 0

    def build_vocabulary(self, data):
        for document in data:
            for word in document:
                # word = word.lower()
                if word not in self.words: 
                    self.words.append(word)

        self.vocabulary_length = len(self.words)
        self.words = np.array(self.words)
        
    def get_features(self, data):
        features = np.zeros((len(data), self.vocabulary_length))

        for document_idx, document in enumerate(data):
            for word in document:
                if word in self.words:
                    features[document_idx, np.where(self.words == word)[0][0]] += 1
        return features