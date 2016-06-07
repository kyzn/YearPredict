import numpy as np
import pandas as pd


def load_data():
    """Return the MNIST data as a tuple containing the training data,
    the validation data, and the test data.

    The ``training_data`` is returned as a tuple with two entries.
    The first entry contains the actual song features.  This is a
    numpy ndarray with 463,715 entries.  Each entry is, in turn, a
    numpy ndarray with 90 values, representing the timbre features.

    The second entry in the ``training_data`` tuple is a numpy ndarray
    containing 463,715 entries.  Those entries are just the year
    values (1922...2011) for the corresponding songs contained in the first
    entry of the tuple.

    The ``test_data`` is similar, except it contains only 51,630 songs.

    This is a nice data format, but for use in neural networks it's
    helpful to modify the format of the ``training_data`` a little.
    That's done in the wrapper function ``load_data_wrapper()``, see
    below.
    """

    #Open the file
    df=pd.read_csv('YearPredictionMSD.txt', sep=',',header=None)

    #Divide into training-test
    trn = df.values[:463715,:]
    tst = df.values[463715:,:]

    #Get training years (both actual years and mapped to 0-1) and features.
    trn_ftr     = trn[:,1:]
    tst_ftr     = tst[:,1:]
    trn_yrs_int = trn[:,0].astype(int)
    tst_yrs_int = tst[:,0].astype(int)

    #Use numpy for speed
    trn_ftr     = np.array(trn_ftr)
    tst_ftr     = np.array(tst_ftr)
    trn_yrs_int = np.array(trn_yrs_int)
    tst_yrs_int = np.array(tst_yrs_int)

    trn_yrs_int-=1922
    tst_yrs_int-=1922

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


    # training_inputs = [np.reshape(x, (90, 1)) for x in trn_ftr]
    # training_results = [vectorized_result(y) for y in trn_yrs_int]
    # training_data = zip(training_inputs, training_results)

    # test_inputs = [np.reshape(x, (90, 1)) for x in tst_ftr]
    # test_data = zip(test_inputs, tst_yrs_int)

    return (training_data, test_data)

def vectorized_result(j):
    """Return a 89-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a year
    (1922..2011) into a corresponding desired output from the neural
    network."""
    e = np.zeros((90, 1))
    e[j] = 1.0
    return e