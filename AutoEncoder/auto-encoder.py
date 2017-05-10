import numpy as np
import pickle, gzip

with gzip.open('./mnist.pkl.gz') as fp:
    training_data, valid_data, test_data = pickle.load(fp,encoding='latin1')
print(print(training_data[0]))


