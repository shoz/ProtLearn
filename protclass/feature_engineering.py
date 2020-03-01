# Author: Thomas Dorfer <thomas.a.dorfer@gmail.com>

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def length(X, method='int'):
    """Compute the length of proteins or peptides.
    
    The number of amino acids that a protein or peptide is comprised of will be
    counted and returned as either an integer array or a one-hot-encoded array.

    Parameters
    ----------
    X : Pandas DataFrame 
        The column containing protein or peptide sequences must be labeled
        'Sequence'.

    method : string, default='int'

        'int' : compute array of protein/peptide lengths
        'ohe' : compute one-hot encoded array of protein/peptide lengths

    Returns
    -------

    lengths : ndarray of shape (n_samples, ) if method = 'int'.
              ndarray of shape (n_samples, n_unique_lengths) if method = 'ohe'

    """

    # list of protein/peptide lengths
    all_len = [len(X['Sequence'][i]) for i in range(X.shape[0])]
    
    # one-hot-encoded lengths of proteins/peptides
    len_span = max(all_len) - min(all_len)
    len_ohe = np.zeros((X.shape[0], len_span+1))
    len_unique = np.arange(min(all_len), max(all_len)+1)

    # fill array with ones based on sequence lengths (columns)
    for i in range(len(all_len)):    
        seq_len = all_len[i]
        j = np.where(len_unique == seq_len)[0][0]
        len_ohe[i,j] = 1

    # delete columns with all zeros
    zero_cols = np.where(~len_ohe.any(axis=0))[0]
    len_ohe = np.delete(len_ohe, zero_cols, axis=1)

    return {
            'int': lambda: np.asarray(all_len), 
            'ohe': lambda: len_ohe,
    }.get(method, lambda: None)()


def composition(X, method='relative', round_fraction=3):
    """Compute the amino acid composition of proteins or peptides.

    The frequency of each of the 20 amino acids in a protein or peptide are 
    counted and returned using the following column order:

    'A','C','D','E','F','G','H','I','K','L',
    'M','N','P','Q','R','S','T','V','W','Y'

    Parameters
    ----------
    X : Pandas DataFrame 
        The column containing protein or peptide sequences must be labeled
        'Sequence'.

    method : string, default='relative'

        'relative' : compute relative amino acid composition
        'absolute' : compute absolute amino acid composition

    round_fraction : int, default=3
        This applies only if method='relative'. For shorter peptides with only 
        a few amino acids, the rounding of amino acid fractions will not have a 
        big impact. However, with longer proteins, decimal places become 
        increasingly more significant and can thus be increased.

    Returns
    -------
    comp :  Pandas DataFrame of shape (n_samples, 20)

    Notes
    -----
    The returned dataframe 'comp' can easily be converted into a numpy array 
    with the command 'np.asarray(comp)', if desired.

    """

    # list of amino acids repesenting array columns
    amino_acids = ['A','C','D','E','F','G','H','I','K','L',
                   'M','N','P','Q','R','S','T','V','W','Y']

    # initialize empty array with shape (n_samples, 20)
    comp_arr = np.zeros((X.shape[0], len(amino_acids)))

    # fill array with frequency of amino acids per protein/peptide
    for i in range(X.shape[0]):
        seq = [aa for aa in X['Sequence'][i]]
        values, counts = np.unique(seq, return_counts=True)
        indices = [amino_acids.index(j) for j in values]
        comp_arr[i,indices] = counts

    if method == 'absolute':
        return pd.DataFrame(comp_arr, columns=amino_acids)

    elif method == 'relative':
        all_len = [len(X['Sequence'][i]) for i in range(X.shape[0])]
        comp_rel = [np.round((comp_arr[i]/all_len[i]), round_fraction)\
                    for i in range(comp_arr.shape[0])]
        
        return pd.DataFrame(np.asarray(comp_rel), columns=amino_acids)
        

def aaindex1(X, standardize='None'):
    """ Compute amino acid indices from aaindex1

    AAindex1 ver.9.2 (release Feb, 2017) is a set of 20 numerical int_values
    representing different physicochemical and biological properties of amino
    acids. Currently, it contains 566 such indices.

    Parameters
    ----------

    X : Pandas DataFrame 
        The column containing protein or peptide sequences must be labeled
        'Sequence'.

    standardize : string, default='None'

        'None' : unstandardized index matrix will be returned
        'zscore' : index matrix is standardized across columns (indices) to have
                   a mean of 0 and standard deviation of 1 (unit variance).
        'minmax' : index matrix is scaled (normalized) across columns (indices)
                   to have a range of [0, 1].

    Returns
    -------
    arr_index1 : ndarray of shape (n_samples, 566) if standardize='None'
        Column size could vary when standardize != 'None'.

    Notes
    -----
    For standardization, columns (indices) containing NaNs will be removed.
    Thus, the resulting index matrix might have a reduced column size.

    The returned dataframe 'arr_index1' can easily be converted into a numpy 
    array with the command 'np.asarray(comp)', if desired.

    """
    
    # load AAIndex1 data
    aaind1 = pd.read_csv('docs/AAIndex/AAIndex1.csv')
    descriptions = aaind1['Description'].values

    # initialize empty array with shape (n_samples, n_aa1_indices)
    aaind_arr = np.zeros((len(X), aaind1.shape[0]))

    # fill array with mean of indices per protein/peptide
    for i, seq in enumerate(range(len(X))):
        sequence = X['Sequence'][seq]
        tmp_arr = np.zeros((aaind1.shape[0], len(sequence)) )

        # fill temporary array with indices for each amino acid of the sequence
        # and compute their mean across all rows
        for j, aa in enumerate(sequence):
            tmp_arr[:,j] = np.asarray(aaind1[aa])

        # fill rows with mean vector of tmp_arr
        aaind_arr[i,:] = tmp_arr.mean(axis=1)

    if standardize == 'None':
        return pd.DataFrame(aaind_arr, columns=descriptions)

    else:
        # finding and removing columns with n_aa1_indices
        inds_nan = np.argwhere(np.isnan(aaind_arr))
        cols_nan = np.unique(inds_nan[:,1])
        aaind_arr = np.delete(aaind_arr, cols_nan, axis=1)
        descriptions = np.delete(descriptions, cols_nan)

        # standardization
        if standardize == 'zscore':
            scaler = StandardScaler().fit(aaind_arr)
            aaind_arr = scaler.transform(aaind_arr)
            
            return pd.DataFrame(aaind_arr, columns=descriptions)

        elif standardize == 'minmax':
            scaler = MinMaxScaler().fit(aaind_arr)
            aaind_arr = scaler.transform(aaind_arr)

            return pd.DataFrame(aaind_arr, columns=descriptions)