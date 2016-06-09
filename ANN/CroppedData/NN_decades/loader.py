import numpy as np
import pandas as pd

def load_data():

    #Open the file
    df=pd.read_csv('CroppedData.txt', sep=',',header=None)

    #Divide into training-test
    trn = df.values[:80000,:]
    tst = df.values[80000:,:]

    trn_ftr     = trn[:,1:]
    tst_ftr     = tst[:,1:]
    trn_yrs_int = ((trn[:,0].astype(int))-1922)//10
    tst_yrs_int = ((tst[:,0].astype(int))-1922)//10

    training_data = (trn_ftr,trn_yrs_int)
    test_data     = (tst_ftr,tst_yrs_int)

    return (training_data, test_data)


def load_data_wrapper():
    """Return the Million Song Dataset as a tuple
    containing the training data and the test data.

    training_data and test_data each looks like (can be accessed as) this:
    data[x][y][z], where:
    x is the index of the example, it is one piece of data
    y is 0 to access features, and 1 to access target y values
    z only exists if y is 0, and it is index for each feature"""

    tr_d, te_d = load_data()

    training_inputs = [np.reshape(x, (90, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    test_inputs = [np.reshape(x, (90, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])

    return (training_data, test_data)

def vectorized_result(j):
    """Return a 9-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a year
    (1922..2011) into a corresponding desired output from the neural
    network."""
    e = np.zeros((9, 1))
    e[j] = 1.0
    return e