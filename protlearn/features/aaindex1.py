# Author: Thomas Dorfer <thomas.a.dorfer@gmail.com>

import numpy as np
import pandas as pd
from Bio.Alphabet import IUPAC
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pkg_resources

PATH = pkg_resources.resource_filename('protlearn', 'data/')

def aaindex1(X, standardize='none', start=1, end=None):
    """Compute amino acid indices from AAIndex1.

    AAindex1 ver.9.2 (release Feb, 2017) is a set of 20 numerical values
    representing various physicochemical and biological properties of amino
    acids. Currently, it contains 566 indices, of which 553 contain no NaNs.
    The indices will be collected for each amino acid in the sequence, 
    then averaged across the sequence. 

    Parameters
    ----------

    X : string, fasta, or a list thereof 

    standardize : string, default='none'

        'none' : unstandardized index matrix will be returned
        'zscore' : index matrix is standardized across columns (indices) to have
                   a mean of 0 and standard deviation of 1 (unit variance).
        'minmax' : index matrix is scaled (normalized) across columns (indices)
                   to have a range of [0, 1].

    start : int, default=1
        Determines the starting point of the amino acid sequence.

    end : int, default=None
        Determines the end point of the amino acid sequence.

    Returns
    -------

    arr : ndarray of shape (n_samples, 553-566) 

    Notes
    -----

    Columns (indices) containing NaNs will be removed. Thus, the resulting index
    matrix will have a column size between 553-566.

    """
    
    # input handling
    X = check_input(X)
    
    # AAIndex1 length
    LEN = 566
    
    # list of amino acids (IUPAC extended)
    amino_acids = IUPAC.IUPACProtein().letters
    
    # load AAIndex1 data and get index names
    aaind1 = pd.read_csv(PATH+'aaindex1.csv')
    desc = aaind1['Description'].values
    
    # convert to dict for better performance
    aaind1 = {aa: aaind1[aa].to_numpy() for aa in amino_acids}

    # initialize empty array with shape (n_samples, 566)
    arr = np.zeros((len(X), LEN))

    # fill array with mean of indices per protein/peptide
    for i, seq in enumerate(X):
        if type(seq) != str:
            seq = str(seq.seq)
        if str.isalpha(seq) == True:
            pass
        else:
            raise TypeError('Data type must be string!')
            
        seq = seq[start-1:end] # positional information
        tmp_arr = np.zeros((LEN, len(seq)) )

        # fill temporary array with indices for each amino acid of the sequence
        # and compute their mean across all rows
        for j, aa in enumerate(seq):
            tmp_arr[:,j] = aaind1[aa]

        # fill rows with mean vector of tmp_arr
        arr[i,:] = tmp_arr.mean(axis=1)

    # find columns with NaNs
    inds_nan = np.argwhere(np.isnan(arr))
    if len(inds_nan) != 0:
        cols_nan = np.unique(inds_nan[:,1])
        cols_nan = np.hstack(cols_nan)
    
    if standardize == 'none' or arr.shape[0] == 1:
        # remove columns with NaNs
        if len(inds_nan) != 0:
            arr = np.delete(arr, cols_nan, axis=1)
            desc = np.delete(desc, cols_nan)
        return arr, desc

    else:
        # remove columns with NaNs and all zeros
        cols_all = []
        cols_zeros = np.where(~arr.any(axis=0))[0]
            
        if len(inds_nan) != 0 and len(cols_zeros) != 0:
            cols_all = np.array((cols_nan, cols_zeros))
            cols_all = np.hstack(cols_all)

        elif len(inds_nan) != 0 and len(cols_zeros) == 0:
            cols_all = cols_nan

        elif len(inds_nan) == 0 and len(cols_zeros) != 0:
            cols_all = cols_zeros

        if len(cols_all) > 0:
            arr = np.delete(arr, cols_all, axis=1)
            desc = np.delete(desc, cols_all)

        # standardization
        if standardize == 'zscore':
            scaler = StandardScaler().fit(arr)
            arr = scaler.transform(arr)
            
            return arr, desc

        # normalization
        elif standardize == 'minmax':
            scaler = MinMaxScaler().fit(arr)
            arr = scaler.transform(arr)

            return arr, desc