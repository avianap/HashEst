import itertools
import pandas as pd
import numpy as np
import random
from sklearn.metrics import jaccard_similarity_score
from hashest import get_words

class jaccard_maker:
    def __init__(self, string_dict):
        self.string_dict = string_dict

    def string_dict_to_occur_dict(self):
        """ Calculates a word occurance dataframe from a dictionary of strings
        Args:
            string_dict (dict): dict with keys (representing column numbers starting from 0) mapped to values (strings)
        Returns:
            dictionary: nested dictionary with outer keys (representing column numbers starting from 0) and inner dictionary key representing each unique word in the vocabulary and values representing a binary for whether that word occurs in the sentence

        Example:
            string_dict = {0: "The cat is grey", 1: "The dog is brown"}
            vocab_dict = {"the":1, "cat":2, "is":3, "grey":4, "dog":5, "brown":6}
            
            occur_dict = {0: {1:1, 2:1, 3:1, 4:1, 5:0, 6:0}, 1: {1:1, 2:0, 3:1, 4:0, 5:1, 6:1}}
            
        """
        tokenized_dict = {k:get_words.tokenize(v) for (k,v) in self.string_dict.items()}
        vocab = tuple(set(itertools.chain.from_iterable(tokenized_dict.values())))
        vocab_dict = {v:x+1 for x, v in zip(range(len(vocab)),vocab)}
        coded_dict = {k: [vocab_dict[x] for x in v] for k,v in tokenized_dict.items()}
        occur_dict = {k: {i:int(i in v) for i in vocab_dict.values()} for k,v in coded_dict.items()}
        return(occur_dict)

    def direct_jaccard(self, occur_dict):
        """ Calculates a jaccard matrix of size m x m from a word occurence dictionary of size m x n
        Args: 
            occur_dict (dictionary): nested dictionary of length m with dictionaries as values containing keys = words in vocab and values = occurence boolean
        Returns:
            pandas.DataFrame of size m x m containing jaccard similarities between each row and column combination
        """
        jac_df = pd.DataFrame(np.zeros((len(occur_dict), len(occur_dict)))) 
        for x in itertools.product(occur_dict.keys(), occur_dict.keys()): 
            coded_arrays = {0:np.array([k*v for k,v in occur_dict[x[0]].items()]), 1:np.array([k*v for k,v in occur_dict[x[1]].items()])}
            coded_arrays_nonzero = {k:v[np.nonzero(v)] for k,v in coded_arrays.items()}
            intersection = len(np.intersect1d(coded_arrays_nonzero[0], coded_arrays_nonzero[1]))
            union = len(coded_arrays_nonzero[0]) + len(coded_arrays_nonzero[1]) - intersection
            jac_df.iat[x[0],x[1]] = intersection/union
        return(jac_df)

    def permute_jaccard(self, occur_dict, permutations):
        """ Calculates a jaccard matrix of size m x m from a word occurence nested dictionary using min row numbers from multiple row order permutations
        Args:
            occur_dict (dictionary): word occurence nested dictionary 
            permutations (int): number of times to permute row numbers
        Returns:
            pandas.DataFrame of size m x m containing jaccard similarities between each row and column combination
        """
        row_num = [x+1 for x in range(len(occur_dict[1]))]
        perm_dict = {k:np.array([]) for k in occur_dict.keys()}
        for i in range(0,permutations):
            random.shuffle(row_num)
            row_num_dict = {k:np.array(list(itertools.chain(occur_dict[k].values())))*row_num for k,v in occur_dict.items()}
            min_row_num_dict = {k:np.ma.min(np.ma.masked_equal(v,0)) for k,v in row_num_dict.items()}
            perm_dict = {k:np.append(v,min_row_num_dict[k]) for k,v in perm_dict.items()}
        jac_df = pd.DataFrame(np.zeros((len(perm_dict),len(perm_dict))))
        for x in itertools.product(perm_dict.keys(),perm_dict.keys()):
            co_occur = (perm_dict[x[0]]==perm_dict[x[1]]).astype(int)
            jac_df.iat[x[0],x[1]] = sum(co_occur)/len(co_occur)
        return(jac_df)

