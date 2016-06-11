import numpy as np
import pandas as pd

def load_data(target):
    """Return the MSD as a tuple containing the training data,
    and the test data.

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
    
    data = df.values #make a copy

    #make every year into 0-89
    data[:,0]-=1922

    #make every feature into 0-1
    for i in xrange(1,91):
        mn,mx = min(data[:,i]), max(data[:,i])
        data[:,i]-=mn
        data[:,i]/=(mx-mn)
    

    #Divide into training-test
    trn = data[:463715,:]
    tst = data[463715:,:]



    trn_ftr     = trn[:,1:]
    tst_ftr     = tst[:,1:]
    trn_yrs_int = (trn[:,0].astype(int))
    tst_yrs_int = (tst[:,0].astype(int))


    if(target==9): #guess decades not years
        trn_yrs_int = trn_yrs_int // 10
        tst_yrs_int = tst_yrs_int // 10


    training_data = (trn_ftr,trn_yrs_int)
    test_data     = (tst_ftr,tst_yrs_int)

    return (training_data, test_data)


def load_data_wrapper(target):
    """Return the Million Song Dataset as a tuple
    containing the training data and the test data.

    training_data and test_data each looks like (can be accessed as) this:
    data[x][y][z], where:
    x is the index of the example, it is one piece of data
    y is 0 to access features, and 1 to access target y values
    z only exists if y is 0, and it is index for each feature

    set target="90" to guess years,
        target="9"  to guess decades.

    """

    tr_d, te_d = load_data(target)

    training_inputs = [np.reshape(x, (90, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y,target) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    test_inputs = [np.reshape(x, (90, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])

    return (training_data, test_data)

def vectorized_result(j,target):
    """Return a 90-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a year
    (1922..2011) into a corresponding desired output from the neural
    network."""
    if (target==9):
        e = np.zeros((9, 1))
    else:
        e = np.zeros((90, 1))
    e[j] = 1.0
    return e