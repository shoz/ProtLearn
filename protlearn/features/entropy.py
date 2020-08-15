# Author: Thomas Dorfer <thomas.a.dorfer@gmail.com>

import numpy as np
from collections import Counter
from utils.validation import check_input

def entropy(X, standardize='none', start=1, end=None):
    """Compute the Shannon entropy of proteins or peptides.

    Parameters
    ----------

    X : string, fasta, or a list thereof 

    start : int, default=1
        Determines the starting point of the amino acid sequence.

    end : int, default=None
        Determines the end point of the amino acid sequence.
        
    standardize : string, default='none'

    'none' : unstandardized array will be returned
    'zscore' : array is standardized to have a mean of 0 and standard deviation 
               of 1 (unit variance).
    'minmax' : array is scaled (normalized) to have a range of [0, 1].

    Returns
    -------

    ent :  ndarray of shape (n_samples, 1) if len(X) > 1
           float if len(X) == 1
    
    amino_acids : amino acid order of aac array

    Notes
    -----

    Start and end positions can be specified to determine the entropy of
    a particular amino acid stretch within the protein.

    """
    
    # input handling
    X = check_input(X)
    
    # initialize empty array with shape (n_samples, 1)
    ent = np.zeros((len(X),1))
    
    # compute shannon entropy
    for i, seq in enumerate(X):
        # check that input is alphabetical
        if str.isalpha(seq) == True:
            pass
        else:
            raise ValueError('Data must be alphabetical!')
        
        seq = seq[start-1:end] # positional information
        cnt = Counter(seq)
        ent_aa = {k: (cnt[k]/len(seq))*np.log2(cnt[k]/len(seq)) for k in cnt.keys()}
        ent[i] = -sum(ent_aa.values())
        
    if standardize == 'none':
        if len(ent) == 1:
            return ent[0][0]
        else:
            return ent
    else:
        if standardize == 'zscore':
            scaler = StandardScaler().fit(ent)
            return scaler.transform(ent)
        
        elif standardize == 'minmax':
            scaler = MinMaxScaler().fit(ent)
            return scaler.transform(ent)